import numpy as np

from ase.md.md import MolecularDynamics


class VelocityVerlet(MolecularDynamics):
    def __init__(self, atoms, dt, trajectory=None, logfile=None,
                 loginterval=1):
        MolecularDynamics.__init__(self, atoms, dt, trajectory, logfile,
                                   loginterval)
    def run(self, f, steps=50):
    # def run(self, f, steps=50):
        """Integrate equation of motion."""
        # f = self.atoms.get_forces(md=True)
        # f = self.atoms.get_forces()
        # print(f)

        if not self.atoms.has('momenta'):
            self.atoms.set_momenta(np.zeros_like(f))

        for step in range(steps):
            f = self.step(f)
            self.nsteps += 1
            self.call_observers()

    def step(self, f):
        p = self.atoms.get_momenta()
        # print('p0', p)

        p += self.dt * f
        # print('p1', p)
        masses = self.atoms.get_masses()[:, np.newaxis]
        r = self.atoms.get_positions()
        # print('r0', r)

        # if we have constraints then this will do the first part of the
        # RATTLE algorithm:
        self.atoms.set_positions(r + 0.5*self.dt * p / masses)
        r1 = self.atoms.get_positions()
        # print('r1', r1)
        # if self.atoms.constraints:
        #     p = (self.atoms.get_positions() - r) * masses / self.dt

        # # print('p3', p)
        # # We need to store the momenta on the atoms before calculating
        # # the forces, as in a parallel Asap calculation atoms may
        # # migrate during force calculations, and the momenta need to
        # # migrate along with the atoms.
        # # self.atoms.set_momenta(p, apply_constraint=False)
        self.atoms.set_momenta(p)

        # f = self.atoms.get_forces()
        # # f = self.atoms.get_forces(md=True)
        # # print(f)

        # # Second part of RATTLE will be done here:
        # self.atoms.set_momenta(self.atoms.get_momenta() + 0.5 * self.dt * f)
        return f
 
