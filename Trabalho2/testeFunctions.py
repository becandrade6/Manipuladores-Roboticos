from Transformacoes import *
import numpy as np
import sympy as sp

#declarando simbólicos
dx, dy, dz = sp.symbols('dx dy dz')

# Teste de funções
F0 = sp.eye(4)

A1 = X_Sym_Translation(dx)*Z_Sym_Translation(dz)*Y_Sym_Translation(dy)

F1 = F0 * A1

sp.pprint(F1)