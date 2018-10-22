from scipy.constants import physical_constants, c, h, hbar, e

print(physical_constants['Hartree energy in eV'])
print(physical_constants['atomic unit of force'])
print(physical_constants['electron volt'])



a = physical_constants['atomic unit of force'][0]/physical_constants['electron volt'][0]*10**(-10)
print(a)