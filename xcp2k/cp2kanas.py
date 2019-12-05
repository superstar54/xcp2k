from xcp2k import CP2K 
from os.path import join, isfile, split, islink
from ase.visualize import view
import ase.io
import os
import numpy as np

class CP2KAnas(CP2K):
    """Class to make many of the common tools for NEBCP2K analysis available to
    the user. Useful for scripting the output of many jobs. Initialize with
    list of images which make up a single band."""

    def __init__(self, **kwargs):

        CP2K.__init__(self, )
        self._images = None
        self.out = None

    def plot_energies(self, np = None, ax=None):
        """Plots the NEB band on matplotlib axes object 'ax'. If ax=None
        returns a new figure object."""
        if not ax:
            import matplotlib.pyplot as plt
            fig = plt.figure()
            ax = fig.add_subplot(111)
        else:
            fig = None
        if np:
            datas = self.results['energies'][np[0]:np[1]]
        else:
            datas = self.results['energies']
        ax.plot(range(len(datas)), datas, '-o')
        # ax.set_ylim([self.results['energies'][-1], self.results['energies'][0]])
        ax.set_xlabel('steps')
        ax.set_ylabel('energy [eV]')
        ax.set_title('Energy profile {0}'.format(self.prefix))
        plt.savefig('{0}.png'.format(self.prefix))
    #
    def write_image_xyz(self, rotation='10z,-80x', **kwargs):
        self.cell = self.read_cell()
        xyzfile = join(self.directory, self.prefix+'-pos-1.xyz')
        xyzimages = ase.io.iread(xyzfile)
        self.xyzimages = []
        for i, image in enumerate(xyzimages):
            # rotate to the desired direction
            # image.rotate('z', 'x', rotate_cell=True)
            # repeat with keeping old cell
            image.set_cell(self.cell)
            cell = image.get_cell_lengths_and_angles()
            # print(cell)
            # s = image.repeat((1, 3, 3))
            # image.set_cell(cell)  
            # ofname = '{0}-{1:04d}.pov'.format(site, i)
            ofname = 'xyz-{0}-{1:04d}.png'.format(self.prefix, i)
            # write(ofname, image,  run_povray=True, **kwargs)  # set bbox by hand, try and error
            ase.io.write(ofname, image, rotation=rotation, **kwargs)  # set bbox by hand, try and error
            self.xyzimages.append(image)
            # os.system('povray {0:04d}.ini'.format(i))
        #
        os.system('convert -dispose 2 -delay 10  xyz-{0}-*png {0}.gif'.format(self.prefix))
        os.system('rm xyz*png')
    #
    def write_image(self, rotation='10z,-80x'):
        self.read_geometry()
        if self.atoms:
            ase.io.write('{0}.png'.format(self.prefix), self.atoms, rotation=rotation)
            ase.io.write('{0}-top.png'.format(self.prefix), self.atoms)
            ase.io.write('{0}-side.png'.format(self.prefix), self.atoms, rotation='-90x')
    def write_pov(self, rotation='10z,-80x', elecolors = None, **extra_kwargs):
        self.atoms.cell = self.atoms.cell*0.98
        # view(self.atoms)
        self.atoms.wrap()
        # view(self.atoms)
        #
        cell = self.atoms.get_cell_lengths_and_angles()
        kwargs = {
        'scale': 2.0,
        'show_unit_cell': True,
        # 'bbox': [-5, -5, cell[0] + 5, cell[1] + 5],
        # 'camera_type'  : 'perspective', # perspective, ultra_wide_angle
        'transparent'  : False, # Transparent background
        'background'   : 'White',        # color
        'pause': False, 
        'display': False, 
        }
        if elecolors:
            newcolors = np.zeros((len(self.atoms), 3))
            for i in range(len(self.atoms)):
                newcolors[i] = elecolors[self.atoms[i].symbol]
            extra_kwargs['colors'] = newcolors
        kwargs.update(extra_kwargs)
        ase.io.write('pov-{0}-top.pov'.format(self.prefix), self.atoms,  run_povray=True, **kwargs)  # set bbox by hand, try and error
        ase.io.write('pov-{0}-side.pov'.format(self.prefix), self.atoms,  run_povray=True, rotation = '-90x', **kwargs)  # set bbox by hand, try and error
        ase.io.write('pov-{0}.pov'.format(self.prefix), self.atoms,  run_povray=True, rotation=rotation, **kwargs)  # set bbox by hand, try and error


