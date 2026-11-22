'''
QUESTION #2:
Use the relation derived in (a) to obtain an algebraic relation 
between the charge density rho(x) and the potential phi(x).'''

#Recall electron charge density, rho.

import sympy as sp
from part_1 import pF, energy_eq, e

#from part 1: pF^2 = 2emphi

pF_eq = sp.solve(energy_eq, pF)[-1]

hbar, rho = sp.symbols("hbar, rho")
N_expr = pF_eq**3 / (3 * sp.pi**2 * hbar**3)
rho_expr = -e * N_expr 
final_rho_eq = sp.Eq(rho, sp.simplify(rho_expr))

if __name__ == "__main__":
    print("This is part 2 of the Thomas-Fermi atom model problem.")
    print(f"Charge Density:\nrho = {final_rho_eq.rhs}")