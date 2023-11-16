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
l1 = sp.Symbol('L1')
l2 = sp.Symbol('L2')
l3 = sp.Symbol('L3*')
d3 = sp.Symbol('D3*')
dTeste = sp.Symbol('Dt')

#criando dicionário com as variaveis de denavit hatenberg (para outros robos, so criar dicionario diferente)
#se quiserem da até pra fazer o codigo todo como uma grande função e criar varios dicionarios e so chamar as funções c os dicionarios
#mas acho que fica mais facil de entender assim
denavit_ppp_3dof = {
    'A0': [l1,theta1,dTeste,0],
    'A1': [0,theta2,l3,np.deg2rad(180)],
    'A2': [d3,0,0,0]
    
}
Ghost = [l1,theta1,0,0]

#criando frame 0 como identidade
F0 = sp.eye(4)

#criando as matrizes de denavit hatenberg de forma iterativa a partir do dicionario
for key,item in denavit_ppp_3dof.items():
    #condição especial para tratar do A0
    if key == 'A0':
        A0 = Denavit_Frame_Sym(item)
        F1 = F0 * A0
    #função que executa algo a partir de uma string (apenas para podermos criar uma variavel com o nome 
    # da chave do dicionario que é string)
    exec(key +'= Denavit_Frame_Sym(item)')
Aghost = Denavit_Frame_Sym(Ghost)
#criando frames F1 e F2 a partir das multiplicações das matrizes de denavit hatenberg com os frames anteriores
F2 = F1*A1
F3 = F2*A2
Fghost = F0*Aghost

#inserindo comprimento l1 l2
l1_real = 5
l2_real = 2
l3_real = 2
dTeste_real = 1
#inserindo valores das juntas em radianos (prismatica em metros)
junta1 = np.deg2rad(0)
junta2 = np.deg2rad(-45)
junta3 = 2

#obtendo as matrizes numericas dos frames
#Caso quiséssemos ter ido direto para o numerico, na parte de criar as matrizes de denavit hatenberg
#poderiamos ter chamada a função Denavit_Frame_Num ao invés de Denavit_Frame_Sym
F1_num = F1.subs([(l1,l1_real),(l2,l2_real),(l3,l3_real),(theta1,junta1),(theta2,junta2),(d3,junta3),(dTeste,dTeste_real)])

F2_num = F2.subs([(l1,l1_real),(l2,l2_real),(l3,l3_real),(theta1,junta1),(theta2,junta2),(d3,junta3),(dTeste,dTeste_real)])

F3_num = F3.subs([(l1,l1_real),(l2,l2_real),(l3,l3_real),(theta1,junta1),(theta2,junta2),(d3,junta3),(dTeste,dTeste_real)])
Fghost_num = Fghost.subs([(l1,l1_real),(l2,l2_real),(l3,l3_real),(theta1,junta1),(theta2,junta2),(d3,junta3),(dTeste,dTeste_real)])


#simplicando matrizes para que números fiquem como zero e tals e nao e-17
F1_num = sp.nsimplify(F1_num,tolerance=1e-10,rational=True)
F2_num = sp.nsimplify(F2_num,tolerance=1e-10,rational=True)
F3_num = sp.nsimplify(F3_num,tolerance=1e-10,rational=True)
Fghost_num = sp.nsimplify(Fghost_num,tolerance=1e-10,rational=True)


#criando figura e eixos 3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#PlotTransicaoAB(F0,F1_num,ax)
PlotTransicaoAB(F0,Fghost_num,ax)
PlotTransicaoAB(Fghost_num,F1_num,ax)
PlotTransicaoAB(F1_num,F2_num,ax)
PlotTransicaoAB(F2_num,F3_num,ax)

PlotFrame(F0,ax,0)
PlotFrame(F1_num,ax,1)
PlotFrame(F2_num,ax,2)
PlotFrame(F3_num,ax,3)


plt.xlabel('X')
plt.ylabel('Y')
plt.show()