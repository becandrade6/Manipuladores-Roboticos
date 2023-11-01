from ManipuladoresFunctions import *
import sympy as sp
import numpy as np
#import matplotlib.pyplot as plt

theta1 = sp.Symbol('theta{1}*')
theta2 = sp.Symbol('theta{2}*')
l1 = sp.Symbol('L1')
l2 = sp.Symbol('L2')
l3 = sp.Symbol('L3*')

F1 = None
F2 = None
F3 = None
denavit_rrp_3dof = {
    'A0': [0,theta1,l1,0],
    'A1': [0,np.deg2rad(90)+theta2,0,np.deg2rad(90)],
    'A2': [l2 + l3,0,0,0]
}

F0 = sp.eye(4)
for key,item in denavit_rrp_3dof.items():
    if key == 'A0':
        A0 = Z_Sym_Translation(item[0])*Z_Sym_Rotation(item[1])*X_Sym_Translation(item[2])*X_Sym_Rotation(item[3])
        F1 = F0 * A0
    exec(key +'=Z_Sym_Translation(item[0])*Z_Sym_Rotation(item[1])*X_Sym_Translation(item[2])*X_Sym_Rotation(item[3])')

F2 = F1*A1

F3 = F2*A2

#sp.pprint(F2)
#print('')

#sp.pprint(F3)

l1_real = 2
l2_real = 2

junta1 = 0
junta2 = 0
junta3 = 0

F1_num = F1.subs([(l1,l1_real),(l2,l2_real),(theta1,junta1),(theta2,junta3),(l3,junta3)])

F2_num = F2.subs([(l1,l1_real),(l2,l2_real),(theta1,junta1),(theta2,junta3),(l3,junta3)])

F3_num = F3.subs([(l1,l1_real),(l2,l2_real),(theta1,junta1),(theta2,junta3),(l3,junta3)])

sp.pprint(F3_num)