from Transformacoes import *
from DenavitHatenberg import *
from PlotFunctions import *
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

theta1 = sp.Symbol('theta{1}*')
theta2 = sp.Symbol('theta{2}*')
theta3 = sp.Symbol('theta{3}*')
l1 = sp.Symbol('L1')
l2 = sp.Symbol('L2')
l3 = sp.Symbol('L3')

denavit_rrp_3dof = {
    'A0': [l1,theta1,0,np.deg2rad(-90)],
    'A1': [0,theta2,l2,0],
    'A2': [0,theta3,l3,0]
}

F0 = sp.eye(4)

for key,item in denavit_rrp_3dof.items():
    #condição especial para tratar do A0
    if key == 'A0':
        A0 = Denavit_Frame_Sym(item)
        F1 = F0 * A0
    #função que executa algo a partir de uma string (apenas para podermos criar uma variavel com o nome 
    # da chave do dicionario que é string)
    exec(key +'= Denavit_Frame_Sym(item)')

F2 = F1*A1
F3 = F2*A2

l1_real = 2
l2_real = 2
l3_real = 2

junta1 = 0
junta2 = 0
junta3 = 0

F1_num = F1.subs([(l1,l1_real),(l2,l2_real),(l3,l3_real),(theta1,junta1),(theta2,junta2),(theta3,junta3)])

F2_num = F2.subs([(l1,l1_real),(l2,l2_real),(l3,l3_real),(theta1,junta1),(theta2,junta2),(theta3,junta3)])

F3_num = F3.subs([(l1,l1_real),(l2,l2_real),(l3,l3_real),(theta1,junta1),(theta2,junta2),(theta3,junta3)])

#simplicando matrizes para que números fiquem como zero e tals e nao e-17
F1_num = sp.nsimplify(F1_num,tolerance=1e-10,rational=True)
F2_num = sp.nsimplify(F2_num,tolerance=1e-10,rational=True)
F3_num = sp.nsimplify(F3_num,tolerance=1e-10,rational=True)

#criando figura e eixos 3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


PlotTransicaoAB(F0,F1_num,ax)
PlotTransicaoAB(F1_num,F2_num,ax)
PlotTransicaoAB(F2_num,F3_num,ax)
PlotFrame(F0,ax,0)
PlotFrame(F1_num,ax,1)
PlotFrame(F2_num,ax,2)
PlotFrame(F3_num,ax,3)


plt.xlabel('X')
plt.ylabel('Y')
plt.show()