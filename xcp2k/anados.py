from xcp2k import CP2K 
import numpy as np
from ase import Atoms
from os.path import join, isfile, split, islink
from ase.io import read, write
from ase.neb import fit0
import os
import re
import matplotlib.pyplot as plt
from ase.io.cube import read_cube_data
from ase.data.colors import cpk_colors

import subprocess

from ase.data import covalent_radii
from ase.io.cube import read_cube_data
from ase.data.colors import cpk_colors

orbitals = ['s', 'p', 'd', 'f']
colors = ['b', 'g', 'c', 'm', 'y', 'k']

class AnaDOS(CP2K):
    """Class to make many of the common tools for CP2K DOS analysis available to
    the user."""

    def __init__(self, directory = '.', prefix = None, nimages = None, **kwargs):

        CP2K.__init__(self,  **kwargs)

        self.directory = directory
        if prefix: self.prefix = prefix
        #
        self.get_number_of_spins()
        self.get_atomic_kinds()
        #self.get_dos()
        
    #
    def read_ini(self, ):
        #
        pass
        
        return 0


    def get_pdos(self, prefix = None, kinds = None, spin=None, ef=None, sigma=0.003, de=0.001):
        """Return Atom projected DOS for atom index, orbital and spin.
        kinds = {index : [element  number of atoms], }
        kinds = {1: ['O', 1], 2: ['C', 1]}
        pdos = {index: [ up[s,p,d], down[s,p,d]], }
        dos = {index: [ up, down], }
        totdos = (up, down\)

        """
        if prefix: self.prefix = prefix
        if kinds: self.kinds = kinds
        if spin: self.spin = spin
        if ef: self.ef = ef

        if self.spin==2:
            labels = ['ALPHA_', 'BETA_']
        else:
            labels = ['', '']
        pdos = {}
        energies=[[], []]
        for i, kind in self.kinds.items():
            pdos[i] = []
            for j in range(self.spin):
                file = os.path.join('{0}-{1}k{2}-1.pdos'.format(self.prefix, labels[j], i))
                print(file, self.kinds)
                efermi, xmesh, ymesh = self.cp2k_pdos(fpdos = file, natoms = kind[1], sigma = sigma, de=de, output='smeared-{0}'.format(file))
                pdos[i].append(ymesh)
                print(ymesh.shape)
                energies[j] = xmesh
        self.energies = energies
        self.pdos = pdos
        self.Ef = efermi
        # calculate total dos
        dos = {}
        nd = max(len(energies[0]), len(energies[1]))
        totdos = np.zeros([self.spin, nd])
        for ele, pdos in self.pdos.items():
            dos[ele] = np.zeros([self.spin, nd])
            for i in range(self.spin):
                dos[ele][i][0:len(self.energies[i])] += np.sum(pdos[i], axis=1)
                totdos[i] += dos[ele][i]
        self.dos = dos
        self.totdos = totdos
        return self.pdos
    def cp2k_pdos(self, fpdos = None, natoms=None, sigma = 0.005, de=0.001, total_sum = False, pheader=True, output='smear.dat'):
        '''
        Copyright (c) 2017 Tiziano Muller <tiziano.mueller@chem.uzh.ch>,
        based on a Fortran tool written by Marcella Iannuzzi <marcella.iannuzzi@chem.uzh.ch>
        'fpdos':   the PDOS file generated by CP2K
        'natoms':         the total number of atoms of this kind in the structure
        'sigma':          sigma for the gaussian distribution (default: 0.02)
        'de': '-d':       integration step size (default: 0.001)
        'total-sum':      calculate and print the total sum for each orbital (default: no)
        'no-header':      do not print a header (default: print header)
        'output':         write output to specified file (default: write to standard output)

        return efermi, energies, dos
        '''
        HEADER_MATCH = re.compile(
        r'\# Projected DOS for atomic kind (?P<element>\w+) at iteration step i = \d+, E\(Fermi\) = [ \t]* (?P<Efermi>[^\t ]+) a\.u\.')
        fhandle = open(fpdos, 'r')
        header = HEADER_MATCH.match(fhandle.readline().rstrip())
        efermi = float(header.group('Efermi')) + 0.002
        # header is originally: ['#', 'MO', 'Eigenvalue', '[a.u.]', 'Occupation', 's', 'py', ...]
        header = fhandle.readline().rstrip().split()[1:]  # remove the comment directly
        header[1:3] = [' '.join(header[1:3])]  # rejoin "Eigenvalue" and its unit
        data = np.loadtxt(fhandle)  # load the rest directly with numpy 

        npnts, ncols = data.shape
        ncols -= 3  # ignore energy, occupation and #MO for mesh    

        emin = min(data[:, 1]) - 0.2 # energies are in the second column
        emax = max(data[:, 1]) + 0.2
        nmesh = int((emax-emin)/de)+1   
        # print("Minimum energy:   {:14.3f}".format(emin))
        # print("Maximum energy:   {:14.3f}".format(emax))

        # reproduce exactly the previous Fortran-based code
        xmesh = np.array([emin+i*de for i in range(1, nmesh+1)])
        ymesh = np.zeros((nmesh, ncols))    

        fact = de/(sigma*np.sqrt(2.0*np.pi))
        for mpnt in range(nmesh):
            func = np.exp(-(xmesh[mpnt]-data[:, 1])**2/(2.0*sigma**2))*fact
            ymesh[mpnt, :] = func.dot(data[:, 3:])  

        efermi *= 27.211384
        xmesh *= 27.211384  # convert to eV
        xmesh -= efermi  # put the Fermi energy at 0
        ymesh /= natoms  # normalize    

        fhandle = open(output, 'w')
        if pheader:
            fhandle.write(("#{:>16}" + " {:>16}"*ncols + "\n").format("Energy_[eV]", *header[3:]))
        for mpnt in range(nmesh):
            fhandle.write(("{:16.8f}" + " {:16.8f}"*ncols + "\n").format(xmesh[mpnt], *ymesh[mpnt, :]))
        return efermi, xmesh, ymesh

    def plot_ele_pdos(self, xlim=[-20, 10], sef=True, prefix=None):
        """
        orbital: string ['s', 'p', 'd', 'f'] 
        """
        for i, pdos in self.pdos.items():
            ele = self.kinds[i][0]
            plt.figure()
            for i in range(self.spin):
                if not sef:
                    x = self.energies[i] + self.Ef
                else:
                    x = self.energies[i]
                y = pdos[i]
                no = len(y[0, :])
                for j in range(no):
                    plt.plot(x, y[:, j]*(-1)**i, linewidth=1, color=colors[j])
            if not sef:
                plt.axvline(x=self.Ef, linewidth=0.5, color='r', linestyle='dashed')
            else:
                plt.axvline(x=0.0, linewidth=0.5, color='r', linestyle='dashed')

            plt.axhline(y=0.0, linewidth=0.5, color='k', linestyle='dashed')
            plt.xlabel('Energy - E$_f$ (eV)')
            plt.ylabel('DOS')
            plt.title('{0}'.format(ele))
            plt.xlim([max(xlim[0], min(self.energies[0])), min(xlim[1], max(self.energies[0]))])
            plt.legend(orbitals[0:no])
            plt.grid(True, 'major', 'x', ls='--', lw=.5, c='k', alpha=.3)
            if prefix:
                plt.savefig('{0}dos-{1}.jpg'.format(prefix, ele), dpi = 600)
            else:
                # print(ele)
                plt.savefig('dos-{0}.jpg'.format(ele), dpi = 600)

            plt.close()
    #
    def plot_total_pdos(self, eles = None, xlim=[-20, 10], ylim = None, sef=True, output = 'dos-total.jpg'):
        """Plots the NEB band on matplotlib axes object 'ax'. If ax=None
        returns a new figure object."""
        plt.figure()
        if eles:
            dos = {k: self.dos[k] for k, v in self.kinds.items() if v[0] in eles}
        else:
            dos = self.dos
        for j in range(self.spin):
            legend = []
            if not sef:
                x = self.energies[j] + self.Ef
            else:
                x = self.energies[j]
            for i, y in dos.items():
                ele = self.kinds[i][0]
                legend.append(ele)
                plt.plot(x, y[j][0:len(x)]*(-1)**j, linewidth=1, color=colors[i])
        if not sef:
            plt.axvline(x=self.Ef, linewidth=0.5, color='r', linestyle='dashed')
        else:
            plt.axvline(x=0.0, linewidth=0.5, color='r', linestyle='dashed')        
        plt.axhline(y=0.0, linewidth=0.5, color='k', linestyle='dashed')
        plt.xlabel('Energy - E$_f$ (eV)')
        plt.ylabel('DOS')
        plt.xlim([max(xlim[0], min(self.energies[0])), min(xlim[1], max(self.energies[0]))])
        if ylim:
            plt.ylim(ylim)
        plt.legend(legend)
        plt.grid(True, 'major', 'x', ls='--', lw=.5, c='k', alpha=.3)
        plt.savefig(output, dpi = 600)
        plt.close()

    def get_fermi_level(self):
        """Return the Fermi level."""
        energies = []
        free_energies = []
        cone = physical_constants['Hartree energy in eV'][0]
        #
        if self.out is None:
            self.out = join(self.directory, 'cp2k.out')
        # print(self.out)
        for line in open(self.out, 'r'):
            if line.rfind('Fermi Energy') > -1 and line.rfind('eV') > -1:
                Ef = float(line.split()[-1])
            if line.rfind('Fermi Energy') > -1 and line.rfind('eV') == -1:
                Ef = float(line.split()[-1])*cone
        self.Ef = Ef

    def get_cube(self, prefix = None, roll = [0, 0, 0], repeat = [1, 1, 1], box = True, output = None):
        """

        """
        if prefix: self.prefix = prefix

        file = '{0}.cube'.format(self.prefix)
        data, atoms = read_cube_data(file)
        # repeat
        if repeat:
            data = np.tile(data, repeat)
            atoms *= repeat
        t = np.sum(roll*atoms.cell/data.shape, axis = 0)
        atoms.translate(t)
        data = np.roll(data, roll, axis=[0, 1, 2])

        self.cube = [atoms, data]
    def plot_cube(self, nc = 6, distance = 10, magnification=1, output='cube', view = False, cell=True, movie=True, elevation=90):
        """Plot atoms, unit-cell and iso-surfaces using Mayavi. 

        Parameters: 

        atoms: Atoms object
            Positions, atomiz numbers and unit-cell.
        data: 3-d ndarray of float
            Data for iso-surfaces.
        countours: list of float
            Contour values.
        """ 

        # Delay slow imports: 
        tube_radius = 0.0
        from mayavi import mlab
        if not view:
            mlab.options.offscreen = True
        if cell:
            tube_radius=0.3
        atoms, data = self.cube
        mn = data.min()
        mx = data.max()
        # print('Min: %16.6f' % mn)
        # print('Max: %16.6f' % mx)
        d = (mx - mn) / nc
        contours = np.linspace(mn + d / 2, mx - d / 2, nc).tolist()
        # mlab.plot(atoms, data, contours, output)

        mlab.figure(bgcolor=(1, 1, 1))  # make a white figure    

        # Plot the atoms as spheres:
        for pos, Z in zip(atoms.positions, atoms.numbers):
            mlab.points3d(*pos,
                          scale_factor=covalent_radii[Z],
                          resolution=20,
                          color=tuple(cpk_colors[Z]))   

        # Draw the unit cell:
        
        A = atoms.cell
        for i1, a in enumerate(A):
            i2 = (i1 + 1) % 3
            i3 = (i1 + 2) % 3
            for b in [np.zeros(3), A[i2]]:
                for c in [np.zeros(3), A[i3]]:
                    p1 = b + c
                    p2 = p1 + a
                    mlab.plot3d([p1[0], p2[0]],
                                [p1[1], p2[1]],
                                [p1[2], p2[2]],
                                tube_radius=tube_radius)    

        cp = mlab.contour3d(data, contours=contours, transparent=True,
                            opacity=0.5, colormap='hot')
        # Do some tvtk magic in order to allow for non-orthogonal unit cells:
        polydata = cp.actor.actors[0].mapper.input
        pts = np.array(polydata.points) - 1
        # Transform the points to the unit cell:
        polydata.points = np.dot(pts, A / np.array(data.shape)[:, np.newaxis])
        # print(output)
        if view:
            mlab.view(0, 90)
            return 0

        #
        path = 'figs_cube'
        if not os.path.exists(path):
                os.mkdir(path)
        for azimuth in [0, 90, 180]:
            for elevation in [0, 90, 180]:
                # print(azimuth, elevation)
                mlab.view(azimuth, elevation, distance=distance)
                mlab.savefig('{0}/{1}-{2}-{3}.png'.format(path, output, azimuth, elevation), magnification=magnification)
        if movie:
            fps = 10
            for ang in range(0, 360, 10):
                # print(ang)
                mlab.view(ang, elevation, distance=distance)
                mlab.savefig('{0}/temp_mlabplot_{1:04d}.jpg'.format(path, ang))
            output = '{0}/{1}.mp4'.format(path, output)
            cmd = 'ffmpeg -r {0} -pattern_type glob -i {1}/\'temp_mlabplot_*.jpg\' -c:v libx264 {2}'.format(fps, path,
                                                                            output)
            if os.path.exists(output):
                os.remove(output)
            subprocess.call(cmd, shell=True)
            # Remove temp image files with extension
            os.system('rm {0}/temp_mlabplot_*jpg'.format(path))
        mlab.clf()

if __name__ == '__main__':
    pass
    # ana = AnaDOS('.')