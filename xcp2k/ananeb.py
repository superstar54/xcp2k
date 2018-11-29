from xcp2k import CP2K 
import numpy as np
from ase import Atoms
from os.path import join, isfile, split, islink
from ase.io import read, write
from ase.neb import fit0
import os
class AnaNEB(CP2K):
    """Class to make many of the common tools for NEBCP2K analysis available to
    the user. Useful for scripting the output of many jobs. Initialize with
    list of images which make up a single band."""

    def __init__(self, directory = '.', prefix = None, nimages = None, **kwargs):

        CP2K.__init__(self, restart=None, mode = 0, env = 'SLURM', ignore_bad_restart_file=False,
                  cpu = 1, atoms=None, command=None,
                 debug=False, **kwargs)

        self.directory = directory
        self.prefix = prefix
        self.nimages = nimages
        #
        self.read_ini()
        #
        self.calcs = [CP2K() for i in range(self.nimages)]
        #
        self.out = None
        self.benergy = np.zeros(self.nimages)
        #
        self.read_images()
    #
    def read_ini(self, ):
        #
        energies = []
        if self.out is None:
            self.out = join(self.directory, 'cp2k.out')
        # print(self.out)
        lines = open(self.out, 'r').readlines()
        for line in lines:
            if line.rfind('GLOBAL| Project name') > -1:
                prefix = line.split()[-1]
            if line.rfind('NUMBER OF NEB REPLICA') > -1:
                nimages = int(line.split()[-1])
            if line.rfind('BAND TOTAL ENERGY [au]') > -1:
                e = float(line.split()[-1])
                energies.append(e)
        self.prefix = prefix
        self.nimages = nimages
        self.band_total_energies = energies
    #
    def read_images(self, ):
        images = []
        cell = self.read_cell()
        for i in range(0, self.nimages):
            self.calcs[i].prefix = self.prefix
            image = read('{0}/{1}-pos-Replica_nr_{2:02d}-1.xyz'.format(self.directory, self.calcs[i].prefix, i + 1))
            image.cell = cell
            self.calcs[i].out = join(self.directory, '{0}-BAND{1:02d}.out'.format(self.calcs[i].prefix, i + 1))
            image.set_calculator(self.calcs[i])
            image.calc.read_energy()
            image.calc.read_forces()
            images.append(image)
        self.images = images
        self.cell = cell
    #
    def read_band_energies(self):
        benergies = []
        for i in range(self.nimages):
            self.benergy[i] = self.images[i].calc.results['energy']
        for i in range(len(self.images[i].calc.results['energies'])):
            energies = []
            try:
                for j in range(self.nimages):
                    energies.append(self.images[j].calc.results['energies'][i])
            except:
                print('read energies error, cp2k run may be interupt')

            benergies.append(energies)
        self.benergies = benergies
    #
    def get_barrier(self, fit=True, raw=False):
        """Returns the barrier estimate from the CP2K, along with the
        Delta E of the elementary reaction. If fit=True, the barrier is
        estimated based on the interpolated fit to the images; if
        fit=False, the barrier is taken as the maximum-energy image
        without interpolation. Set raw=True to get the raw energy of the
        transition state instead of the forward barrier."""
        s, E, Sfit, Efit, lines = self.get_fit()
        dE = E[-1] - E[0]
        if fit:
            barrier = max(Efit)
        else:
            barrier = max(E)
        if raw:
            barrier += self.images[0].get_potential_energy()
        return barrier, dE

    def plot_image_energy(self, ax=None):
        """Plots the NEB band on matplotlib axes object 'ax'. If ax=None
        returns a new figure object."""
        if not ax:
            import matplotlib.pyplot as plt
            fig = plt.figure()
            ax = fig.add_subplot(111)
        else:
            fig = None
        s, E, Sfit, Efit, lines = self.get_fit()
        ax.plot(s, E, 'o')
        for x, y in lines:
            ax.plot(x, y, '-g')
        ax.plot(Sfit, Efit, 'k-')
        ax.set_xlabel('Reaction path [$\AA$]')
        ax.set_ylabel('Energy profile [eV]')
        Ef = max(Efit) - E[0]
        Er = max(Efit) - E[-1]
        dE = E[-1] - E[0]
        ax.set_title('$E_\mathrm{f} \\approx$ %.3f eV; '
                     '$E_\mathrm{r} \\approx$ %.3f eV; '
                     '$\\Delta E$ = %.3f eV'
                     % (Ef, Er, dE))
        return fig
    def plot_band_energy(self, ax=None):
        """Plots the NEB band on matplotlib axes object 'ax'. If ax=None
        returns a new figure object."""
        if not ax:
            import matplotlib.pyplot as plt
            fig = plt.figure()
            ax = fig.add_subplot(111)
        else:
            fig = None
        ax.plot(range(len(self.band_total_energies)), self.band_total_energies, '.-')
        
        ax.set_xlabel('Number of steps')
        ax.set_ylabel('Energy profile [eV]')
        
        ax.set_title(' %.d images '
                     % (self.nimages))
        return fig
    def get_fit(self):
        """Returns the parameters for fitting images to band."""
        images = self.images
        R = [atoms.positions for atoms in images]
        E = self.benergy
        F = [atoms.calc.results['forces'] for atoms in images]
        A = images[0].cell
        pbc = images[0].pbc
        s, E, Sfit, Efit, lines = fit0(E, F, R, A, pbc)
        return s, E, Sfit, Efit, lines

    def write_images(self, name = None, rotation='10z,-80x'):
        #
        for i, image in enumerate(self.images):
            # rotate to the desired direction
            # image.rotate('z', 'x', rotate_cell=True)
            # repeat with keeping old cell
            # s = image.repeat((1, 3, 3))
            # image.set_cell(cell)  image.set_cell(cell)
            cell = image.get_cell_lengths_and_angles()
            ofname = 'temp-{0:04d}.pov'.format(i)
            print('writing', ofname)
            kwargs = {
            'scale': 2.0,
            'show_unit_cell': True,
            'bbox': [-5, -5, cell[0] + 5, cell[1] + 5],
            'pause': False, 
            'display': False, 
            }
            write(ofname, image,  run_povray=True, rotation = rotation, **kwargs)  # set bbox by hand, try and error
            # os.system('povray {0:04d}.ini'.format(i))
            #

        if name:
            filename = '{0}.gif'.format(name)
        else:
            filename = '{0}.gif'.format(self.prefix)
        os.system('convert -delay 20 temp*png {0}'.format(filename))
        os.system('''convert {0}  \
          \( -clone 0 -set delay 200 \) -swap 0 +delete \
          \( +clone   -set delay 100 \) +swap   +delete \
          {0}'''.format(filename))

        os.system('rm temp*.ini temp*png  temp*.pov')

