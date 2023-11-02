from Transformacoes import *
import sympy as sp

def Denavit_Frame_Sym(variables):
    """
    :param variables: lista de variaveis de Denavit-Hartenberg
    :return: matriz de transformação homogênea

    Função que retorna a matriz simbólica de transformação homogênea de Denavit-Hartenberg a partir
    da transformação Tz*Tz*Rz*Tx"""
    Frame = Z_Sym_Translation(variables[0])*Z_Sym_Rotation(variables[1])*X_Sym_Translation(variables[2])*X_Sym_Rotation(variables[3])
    return Frame

def Denavit_Frame_Num(variables):
    """
    :param variables: lista de variaveis de Denavit-Hartenberg
    :return: matriz de transformação homogênea

    Função que retorna a matriz numérica de transformação homogênea de Denavit-Hartenberg a partir
    da transformação Tz*Tz*Rz*Tx"""
    Frame = Z_Translation(variables[0])*Z_Rotation(variables[1])*X_Translation(variables[2])*X_Rotation(variables[3])
    return Frame