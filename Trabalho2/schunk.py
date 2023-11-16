#importando pacotes

from Transformacoes import *    #contem funções de transformações homogêneas
from DenavitHatenberg import *  #contem funções de denavit hatenberg
from PlotFunctions import *     #contem funções de plotagem para frames e transições
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

#criando símbolos no sympy para caso desejamos fazer análises simbólicas
theta1 = sp.Symbol('theta{1}*')
theta2 = sp.Symbol('theta{2}*')
theta3 = sp.Symbol('theta{3}*')
theta4 = sp.Symbol('theta{4}*')
theta5 = sp.Symbol('theta{5}*')
theta6 = sp.Symbol('theta{6}*')
theta7 = sp.Symbol('theta{7}*')

l1 = sp.Symbol('L1')
l2 = sp.Symbol('L2')
l3 = sp.Symbol('L3')
l4 = sp.Symbol('L4')

#criando dicionário com as variaveis de denavit hatenberg (para outros robos, so criar dicionario diferente)
#se quiserem da até pra fazer o codigo todo como uma grande função e criar varios dicionarios e so chamar as funções c os dicionarios
#mas acho que fica mais facil de entender assim
denavit_rrp_3dof = {
    
    'A0': [l1,0,0,0],
    'A0': [l2,theta1,0,np.deg2rad(90)],
    'A1': [0,theta2,0,np.deg2rad(-90)],
    'A2': [l2,theta3,0,np.deg2rad(90)],
    'A3': [0,theta4,0,np.deg2rad(-90)],
    'A4': [l3,theta5,0,np.deg2rad(90)],
    'A5': [0,theta6,0,np.deg2rad(-90)],
    'A6': [l4,theta7,0,0],
}

#criando frame 0 como identidade
F0 = sp.eye(4)

#criando as matrizes de denavit hatenberg de forma iterativa a partir do dicionario
for key,item in denavit_rrp_3dof.items():
    #condição especial para tratar do A0
    if key == 'A0':
        A0 = Denavit_Frame_Sym(item)
        F1 = F0 * A0
    #função que executa algo a partir de uma string (apenas para podermos criar uma variavel com o nome 
    # da chave do dicionario que é string)
    exec(key +'= Denavit_Frame_Sym(item)')

#criando frames F1 e F2 a partir das multiplicações das matrizes de denavit hatenberg com os frames anteriores
F2 = F1*A1
F3 = F2*A2
F4 = F3*A3
F5 = F4*A4
F6 = F5*A5
F7 = F6*A6

#inserindo comprimento l1 l2
l1_real = 300/100
l2_real = 328/100
l3_real = 276.5/100
l4_real = 171.7/100

#inserindo valores das juntas em radianos (prismatica em metro
junta1 = np.deg2rad(30)
junta2 = np.deg2rad(15)
junta3 = np.deg2rad(22)
junta4 = np.deg2rad(40)
junta5 = np.deg2rad(90)
junta6 = np.deg2rad(10)
junta7 = np.deg2rad(90)


#obtendo as matrizes numericas dos frames
#Caso quiséssemos ter ido direto para o numerico, na parte de criar as matrizes de denavit hatenberg
#poderiamos ter chamada a função Denavit_Frame_Num ao invés de Denavit_Frame_Sym
F1_num = F1.subs([(l1,l1_real),(l2,l2_real),(l3,l3_real),(l4,l4_real),(theta1,junta1),(theta2,junta2),(theta3,junta3),(theta4,junta4),(theta5,junta5),(theta6,junta6),(theta7,junta7)])

F2_num = F2.subs([(l1,l1_real),(l2,l2_real),(l3,l3_real),(l4,l4_real),(theta1,junta1),(theta2,junta2),(theta3,junta3),(theta4,junta4),(theta5,junta5),(theta6,junta6),(theta7,junta7)])

F3_num = F3.subs([(l1,l1_real),(l2,l2_real),(l3,l3_real),(l4,l4_real),(theta1,junta1),(theta2,junta2),(theta3,junta3),(theta4,junta4),(theta5,junta5),(theta6,junta6),(theta7,junta7)])

F4_num = F4.subs([(l1,l1_real),(l2,l2_real),(l3,l3_real),(l4,l4_real),(theta1,junta1),(theta2,junta2),(theta3,junta3),(theta4,junta4),(theta5,junta5),(theta6,junta6),(theta7,junta7)])

F5_num = F5.subs([(l1,l1_real),(l2,l2_real),(l3,l3_real),(l4,l4_real),(theta1,junta1),(theta2,junta2),(theta3,junta3),(theta4,junta4),(theta5,junta5),(theta6,junta6),(theta7,junta7)])

F6_num = F6.subs([(l1,l1_real),(l2,l2_real),(l3,l3_real),(l4,l4_real),(theta1,junta1),(theta2,junta2),(theta3,junta3),(theta4,junta4),(theta5,junta5),(theta6,junta6),(theta7,junta7)])

F7_num = F7.subs([(l1,l1_real),(l2,l2_real),(l3,l3_real),(l4,l4_real),(theta1,junta1),(theta2,junta2),(theta3,junta3),(theta4,junta4),(theta5,junta5),(theta6,junta6),(theta7,junta7)])



#simplicando matrizes para que números fiquem como zero e tals e nao e-17
F1_num = sp.nsimplify(F1_num,tolerance=1e-10,rational=True)
F2_num = sp.nsimplify(F2_num,tolerance=1e-10,rational=True)
F3_num = sp.nsimplify(F3_num,tolerance=1e-10,rational=True)
F4_num = sp.nsimplify(F4_num,tolerance=1e-10,rational=True)
F5_num = sp.nsimplify(F5_num,tolerance=1e-10,rational=True)
F6_num = sp.nsimplify(F6_num,tolerance=1e-10,rational=True)
F7_num = sp.nsimplify(F7_num,tolerance=1e-10,rational=True)

#criando figura e eixos 3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

PlotTransicaoAB(F0,F1_num,ax)
PlotTransicaoAB(F1_num,F2_num,ax)
PlotTransicaoAB(F2_num,F3_num,ax)
PlotTransicaoAB(F3_num,F4_num,ax)
PlotTransicaoAB(F4_num,F5_num,ax)
PlotTransicaoAB(F5_num,F6_num,ax)
PlotTransicaoAB(F6_num,F7_num,ax)

PlotFrame(F0,ax,0)
#PlotFrame(F1_num,ax,1)
#PlotFrame(F2_num,ax,2)
#PlotFrame(F3_num,ax,3)
#PlotFrame(F4_num,ax,4)
#PlotFrame(F5_num,ax,5)
#PlotFrame(F6_num,ax,6)
PlotFrame(F7_num,ax,7)

plt.xlabel('X')
plt.ylabel('Y')
plt.show()