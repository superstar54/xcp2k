from ase import Atoms
from ase.build import fcc111, add_adsorbate, bulk
from ase.io import read, write
adsorbate = Atoms('CO')
adsorbate[1].z = 1.1
a = 3.61
slab = fcc111('Cu', (2, 2, 3), a=a, vacuum=7.0)
slab2 = fcc111('Pt', (2, 2, 3), a=a, vacuum=7.0)
add_adsorbate(slab, adsorbate, 1.8, 'ontop')
images = [slab, slab2]
write('movie.gif', images, interval=500)