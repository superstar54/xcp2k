import numpy as np

def highlight_atoms(pov_fid, pov_obj, atomlist, radius_scale=1.2,
                           color='Green', transmit=0.7):
    """Adds a ghost sphere around the specified atom, by writing an extra
    line to the generated .pov file. atomlist contains index numbers,
    radius_scale is the amount to multiply the radius in kwargs['radii']
    by, color is the highlight color, and transmit is a value between 0 and
    1 indicating the transparency. pov is the pov object from the proup
    module.
    """
    for index in atomlist:
        pos = pov_obj.positions[index]
        radius = radius_scale * pov_obj.d[index]
        line = ('sphere{<%.2f,%.2f,%.2f>, %.2f texture{pigment{color '
                '%s transmit %.2f}}} \n' %
                (pos[0], pos[1], pos[2], radius, color, transmit))
        pov_fid.write(line)
def add_vacancy(pov_fid, pov_obj, positions, radius=0.3,
                           color='Red', transmit=0.7):
    """Adds a ghost sphere around the specified atom, by writing an extra
    line to the generated .pov file. atomlist contains index numbers,
    radius_scale is the amount to multiply the radius in kwargs['radii']
    by, color is the highlight color, and transmit is a value between 0 and
    1 indicating the transparency. pov is the pov object from the proup
    module.
    """
    for index in positions:
        # pos = [0, 0, 0]
        pos = np.mean(pov_obj.positions[index], axis=0)
        # radius = radius_scale * pov_obj.d[index]
        line = ('sphere{<%.2f,%.2f,%.2f>, %.2f texture{pigment{color '
                '%s transmit %.2f}}} \n' %
                (pos[0], pos[1], pos[2], radius, color, transmit))
        pov_fid.write(line)


def get_bondpairs(atoms, radius=1.1, rmbonds = []):
    """Get all pairs of bonding atoms
    Return all pairs of atoms which are closer than radius times the
    sum of their respective covalent radii.  The pairs are returned as
    tuples::
      (a, b, (i1, i2, i3))
    so that atoms a bonds to atom b displaced by the vector::
      i c + i c + i c ,
       1 1   2 2   3 3
    where c1, c2 and c3 are the unit cell vectors and i1, i2, i3 are
    integers."""
    from ase.data import covalent_radii
    from ase.neighborlist import NeighborList
    cutoffs = radius * covalent_radii[atoms.numbers]
    nl = NeighborList(cutoffs=cutoffs, self_interaction=False)
    nl.update(atoms)
    bondpairs = []
    for a in range(len(atoms)):
        indices, offsets = nl.get_neighbors(a)
        # print(indices, offsets)
        for a2, offset in zip(indices, offsets):
            flag = True
            for rmpair in rmbonds:
                if atoms[a].symbol == rmpair[0] and atoms[a2].symbol == rmpair[1] \
                  or atoms[a].symbol == rmpair[1] and atoms[a2].symbol == rmpair[0]:
                    flag = False
            # print(a, a2, flag)
            if flag:
                bondpairs.extend([(a, a2, offset)])
    return bondpairs