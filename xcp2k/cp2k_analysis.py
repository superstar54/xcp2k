from xcp2k import CP2K 

class CP2KAnas(CP2K):
    """Class to make many of the common tools for NEBCP2K analysis available to
    the user. Useful for scripting the output of many jobs. Initialize with
    list of images which make up a single band."""

    def __init__(self, **kwargs):

        CP2K.__init__(self, restart=None, mode = 0, env = 'SLURM', ignore_bad_restart_file=False,
                 label='cp2k', cpu = 1, atoms=None, command=None,
                 debug=False, **kwargs)

        self._images = None
        self.out = None

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
            barrier += self._images[0].get_potential_energy()
        return barrier, dE

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
        ax.set_title('Energy convergence')
        return fig


    def get_fit(self):
        """Returns the parameters for fitting images to band."""
        images = self._images
        R = [atoms.positions for atoms in images]
        E = [atoms.get_potential_energy() for atoms in images]
        F = [atoms.get_forces() for atoms in images]
        A = images[0].cell
        pbc = images[0].pbc
        s, E, Sfit, Efit, lines = fit0(E, F, R, A, pbc)
        return s, E, Sfit, Efit, lines


