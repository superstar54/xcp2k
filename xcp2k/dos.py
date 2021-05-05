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
from ase.data.colors import cpk_colors, jmol_colors
from ase.data import covalent_radii, atomic_numbers, chemical_symbols

orbitals = ['s', 'p', 'd', 'f']
colors = ['C{0}'.format(i) for i in range(20)]

class DOS(CP2K):
    """Class to make many of the common tools for CP2K DOS analysis available to
    the user."""

    def __init__(self, directory = '.', prefix = None, **kwargs):

        CP2K.__init__(self,  **kwargs)

        self.directory = directory
        if prefix: self.prefix = prefix
        #
        self.get_number_of_spins()
        self.get_atomic_kinds()
    def read_dos(self, dostype = 'k', prefix = None, nspecies = None, nspin=None, ef=None, sigma=0.003, de=0.01):
        """Return Atom projected DOS for atom index, orbital and nspin.
        dostype: kind-> k, ldos -> list
        kinds = {index : [element  number of atoms], }
        kinds = {1: ['O', 1], 2: ['C', 1]}
        pdos = {index: [ up[s,p,d], down[s,p,d]], }
        dos = {index: [ up, down], }
        totdos = (up, down\)

        """
        if self.nspin==2:
            labels = ['ALPHA_', 'BETA_']
        else:
            labels = ['', '']
        dos = {}
        dos_orbitals = {}
        dos_energies = {}
        for i in range(1, nspecies + 1):
            dos1 = []
            dos_energies1 = []
            for j in range(self.nspin):
                fileinp = os.path.join(self.directory, '{0}-{1}{2}{3}-1.pdos'.format(self.prefix, labels[j], dostype, i))
                print('Reading %s'%fileinp)
                species, efermi, x, y, orbitals = self.read(fpdos = fileinp)
                xmesh, ymesh = self.smearing(x, y, sigma = sigma, de = de)
                dos1.append(ymesh)
                dos_energies1.append(xmesh)
            dos[species] = dos1
            dos_energies[species] = dos_energies1
            dos_orbitals[species] = orbitals
            self.efermi = efermi
        # calculate total dos
        # dos = {}
        # nd = max(len(energies[0]), len(energies[1]))
        # total_dos = np.zeros([self.nspin, nd])
        # for ele, pdos in self.pdos.items():
        #     dos[ele] = np.zeros([self.nspin, nd])
        #     for i in range(self.nspin):
        #         dos[ele][i][0:len(self.energies[i])] += np.sum(pdos[i], axis=1)
        #         total_dos[i] += dos[ele][i]
        # self.dos = dos
        # self.total_dos = total_dos
        return dos_energies, dos, dos_orbitals
    def read_pdos(self, prefix = None, nspecies = None, nspin = None, sigma=0.01, de=0.01):
        '''
        '''
        if prefix: self.prefix = prefix
        if nspecies: self.nspecies = nspecies
        if nspin: self.nspin = nspin
        self.pdos_energies, self.pdos, self.pdos_orbitals = self.read_dos(dostype = 'k', 
                                       prefix = self.prefix, 
                                       nspecies = self.nspecies, 
                                       nspin=self.nspin, 
                                       sigma=sigma, 
                                       de=de)
    def read_ldos(self, prefix = None, nspecies = None, nspin = None, sigma=0.01, de=0.01):
        '''
        '''
        if prefix: self.prefix = prefix
        if nspecies: self.nspecies = nspecies
        if nspin: self.nspin = nspin
        self.ldos_energies, self.ldos, self.ldos_orbitals = self.read_dos(dostype = 'list', 
                                       prefix = self.prefix, 
                                       nspecies = self.nspecies, 
                                       nspin=self.nspin, 
                                       sigma=sigma, 
                                       de=de)
    def read(self, fpdos = None):
        '''
        'fpdos':   the PDOS file generated by CP2K
        return efermi, energies, dos
        '''
        with open(fpdos, 'r') as f:
            lines = f.readlines()
            if 'kind' in lines[0]:
                species = lines[0].split(' kind ')[1].split()[0]
            elif 'list' in lines[0]:
                species = lines[0].split(' list ')[1].split()[0]
            efermi = float(lines[0].split(' = ')[-1].strip().split()[0])
            efermi = efermi*27.211384
            orbitals = lines[1].split()[5:]
            data = np.loadtxt(lines[2:])  # load the rest directly with numpy
            energies = data[:, 1]*27.211384
            dos = data[:, 3:]*27.211384
        return species, efermi, energies, dos, orbitals
    def smearing(self, energies, dos, sigma = 0.1, de=0.01, total = False):
        '''
        'natoms':         the total number of atoms of this kind in the structure
        'sigma':          sigma for the gaussian distribution (default: 0.01)
        'de':     integration step size (default: 0.01)
        '''
        npnts = len(energies)
        emin = min(energies)
        emax = max(energies)
        nmesh = int((emax-emin)/de)+1   
        xmesh = np.linspace(emin, emax, nmesh)
        ymesh = np.zeros((nmesh, len(dos[0, :])))
        fact = de/(sigma*np.sqrt(2.0*np.pi))
        for i in range(nmesh):
            func = np.exp(-(xmesh[i]-energies)**2/(2.0*sigma**2))*fact
            ymesh[i, :] = func.dot(dos[:, :])
        # ymesh /= natoms  # normalize
        # return energies, dos
        return xmesh, ymesh
    def plot_data(self, energies, dos, label, xindex, ax = None, fill = False, color = None):
        lspins = ['up', 'down']
        if ax is None:
            ax = plt.gca()
        for i in range(self.nspin):
            if self.nspin == 2:
                newlabel = '%s-%s' % (label, lspins[i])
            else:
                newlabel = label
            if color is not None:
                ax.plot(energies[i][xindex[i]], (-1)**i*dos[i][xindex[i]], linewidth=0.7, label = newlabel, color = color)
            else:
                ax.plot(energies[i][xindex[i]], (-1)**i*dos[i][xindex[i]], linewidth=0.7, label = newlabel)
            if fill:
                if color is not None:
                    ax.fill_between(energies[i][xindex[i]], (-1)**i*dos[i][xindex[i]], 0, alpha = 0.2, color = color)
                else:
                    ax.fill_between(energies[i][xindex[i]], (-1)**i*dos[i][xindex[i]], 0, alpha = 0.2)
        return ax
    def plot_pdos(self, Emin = -10, Emax = 10, ef = True,
                  ax = None, total = False, select = None, fill = False, 
                  output = None, legend = False, xylabel = True):
        '''
        '''
        pdos_energies = self.pdos_energies.copy()
        if ax is None:
            fig, ax = plt.subplots(figsize = (6, 3))
        # if total:
            # ax = self.plot_data(self.pdos_energies, self.pdos_tot, label = 'pdos', ax = ax, fill = fill)
        for species, pdos in self.pdos.items():
            orbitals = self.pdos_orbitals[species]
            if ef:
                pdos_energies[species] = [x - self.efermi for x in pdos_energies[species]]
            xindex = [(energies>Emin) & (energies<Emax) for energies in pdos_energies[species]]
            if select and species not in select: continue
            number = chemical_symbols.index(species)
            color = jmol_colors[number]
            i = 0
            for orbital in orbitals:
                if select and orbital not in select[species]: continue
                label = '{0}-{1}'.format(species, orbital)
                x = pdos_energies[species]
                y = [y[:, i] for y in pdos]
                ax = self.plot_data(x, y, label = label, ax = ax, xindex = xindex, fill = fill, color = color)
                i += 1
        ax.axvline(0, color = 'b')
        if legend: ax.legend()
        if xylabel:
            ax.set_xlabel('Energy (eV)')
            ax.set_ylabel('PDOS (a.u.)')
        if output is not None:
            plt.savefig('%s'%output)
        return ax
    def plot_ldos(self, Emin = -10, Emax = 10, ef = True,
                  ax = None, total = False, select = None, fill = False, 
                  output = None, legend = False, xylabel = True):
        '''
        '''
        ldos_energies = self.ldos_energies.copy()
        if ax is None:
            fig, ax = plt.subplots(figsize = (6, 3))
        # if total:
            # ax = self.plot_data(self.ldos_energies, self.ldos_tot, label = 'ldos', ax = ax, fill = fill)
        for species, ldos in self.ldos.items():
            orbitals = self.ldos_orbitals[species]
            if ef:
                ldos_energies[species] = [x - self.efermi for x in ldos_energies[species]]
            xindex = [(energies>Emin) & (energies<Emax) for energies in ldos_energies[species]]
            if select and species not in select: continue
            i = 0
            for orbital in orbitals:
                if select and orbital not in select[species]: continue
                label = '{0}-{1}'.format(species, orbital)
                x = ldos_energies[species]
                y = [y[:, i] for y in ldos]
                self.plot_data(x, y, label = label, ax = ax, xindex = xindex, fill = fill)
                i += 1
        ax.axvline(0, color = 'b')
        if legend: ax.legend()
        if xylabel:
            ax.set_xlabel('Energy (eV)')
            ax.set_ylabel('LDOS (a.u.)')
        if output is not None:
            plt.savefig('%s'%output)
        return ax
    def plot_total_pdos(self, eles = None, xlim=[-20, 10], ylim = None, sef=True, output = 'dos-total.jpg'):
        """Plots the NEB band on matplotlib axes object 'ax'. If ax=None
        returns a new figure object."""
        plt.figure()
        if eles:
            dos = {k: self.dos[k] for k, v in self.kinds.items() if v[0] in eles}
        else:
            dos = self.dos
        for j in range(self.nspin):
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
    def plot_cube(self, nc = 6, distance = 10, magnification=1, output='cube', view = False, cell=True, movie=True, elevation=90, colormap = 'hot'):
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
                            opacity=0.5, colormap=colormap)
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