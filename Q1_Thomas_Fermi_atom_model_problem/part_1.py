'''
QUESTION #1:
Assume the charge cloud adjusts itself locally until the electrons
at the Fermi sphere have zero energy, find a relation between the potential φ
and the Fermi momentum pF
'''

#Recall Pauli's exclusion

#NOTE
'''
1) All the electrons AT the fermi sphere refers to the electrons occupying the sphere's outer boundary (shell); that meaning it's surface.
2) Electrons occupying the outer boundary posesss the maximum kinetic energy (Ef) and the maximum speed (Vf) within the sphere. The question states their energies dropping to zero.
3) Momentum states at T= 0K
    -inside the sphere: p < pF (occupied momentum. Adjacent states are filled and electrons are restricted from scattering or changing states.)
    -on the sphere's surface: p = pF (Fermi surface = Highest occupied momentum states)
    -outside the sphere: p > pF (unoccupied moment. No electrons are outside of the sphere.)
4) The fermi surface is the geometric surface of the sphere in which the fermi function (fermi-dirac occupation probability) drop from 1 to 0. 
'''

import sympy as sp

#Recall the wavefunction of an electron is a solution of schrodinger's equation. NOTE: the hamiltonian H only includes KE.
#Recall conservation of total energy equation --> KE + UE = 0

pF, m, e, phi = sp.symbols("pF, m, e, phi", positive=True)
energy_eq = sp.Eq(pF**2/(2*m) -e*phi, 0)
relation_eq = sp.solve(energy_eq, pF**2)[0] #--> dont want it to be a list
print(f'Fermi Momentum:\npF**2 = {relation_eq}')