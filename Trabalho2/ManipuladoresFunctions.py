import numpy as np
import sympy as sp

def X_Translation(deltax):
    """
    :param deltay: float deltax
    :return: matriz de translação no eixo x
    Função que retorna a matriz de translação em x numérica
    """
    return np.array([[1, 0, 0, deltax],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

def Z_Translation(deltaz):
    """
    :param deltaz: float deltaz
    :return: matriz de translação no eixo z
    Função que retorna a matriz de translação em z numérica
    """
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, deltaz],
                     [0, 0, 0, 1]])

def Y_Translation(deltay):
    """
    :param deltay: float deltay
    :return: matriz de translação no eixo y
    Função que retorna a matriz de translação em y numérica
    """
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, deltay],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

def X_Sym_Translation(deltax):
    """
    :param deltax: symbolic deltax
    :return: matriz simbólica de translação no eixo x
    Função que retorna a matriz de translação em x simbólica
    """
    return sp.Matrix([[1, 0, 0, deltax],
                      [0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])

def Y_Sym_Translation(deltay):
    """
    :param deltay: symbolic deltay
    :return: matriz simbólica de translação no eixo y
    Função que retorna a matriz de translação em y simbólica
    """
    return sp.Matrix([[1, 0, 0, 0],
                      [0, 1, 0, deltay],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])

def Z_Sym_Translation(deltaz):
    """
    :param deltaz: symbolic deltaz
    :return: matriz simbólica de translação no eixo z
    Função que retorna a matriz de translação em z simbólica
    """
    return sp.Matrix([[1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, 1, deltaz],
                      [0, 0, 0, 1]])

def X_Rotation(theta):
    """
    :param theta: float theta
    :return: matriz de rotação no eixo x
    Função que retorna a matriz de rotação em x numérica
    """
    return np.array([[1, 0, 0, 0],
                     [0, np.cos(theta), -np.sin(theta), 0],
                     [0, np.sin(theta), np.cos(theta), 0],
                     [0, 0, 0, 1]])

def Y_Rotation(theta):
    """
    :param theta: float theta
    :return: matriz de rotação no eixo y
    Função que retorna a matriz de rotação em y numérica
    """
    return np.array([[np.cos(theta), 0, np.sin(theta), 0],
                     [0, 1, 0, 0],
                     [-np.sin(theta), 0, np.cos(theta), 0],
                     [0, 0, 0, 1]])

def Z_Rotation(theta):
    """
    :param theta: float theta
    :return: matriz de rotação no eixo z
    Função que retorna a matriz de rotação em z numérica
    """

    return np.array([[np.cos(theta), -np.sin(theta), 0, 0],
                     [np.sin(theta), np.cos(theta), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

def X_Sym_Rotation(theta):
    """ 
    :param theta: symbolic theta
    :return: matriz simbólica de rotação no eixo x
    Função que retorna a matriz de rotação em x simbólica
    """
    return sp.Matrix([[1, 0, 0, 0],
                      [0, sp.cos(theta), -sp.sin(theta), 0],
                      [0, sp.sin(theta), sp.cos(theta), 0],
                      [0, 0, 0, 1]])

def Y_Sym_Rotation(theta):
    """
    :param theta: symbolic theta
    :return: matriz simbólica de rotação no eixo y
    Função que retorna a matriz de rotação em y simbólica
    """
    return sp.Matrix([[sp.cos(theta), 0, sp.sin(theta), 0],
                      [0, 1, 0, 0],
                      [-sp.sin(theta), 0, sp.cos(theta), 0],
                      [0, 0, 0, 1]])

def Z_Sym_Rotation(theta):
    """
    :param theta: symbolic theta
    :return: matriz simbólica de rotação no eixo z
    
    Função que retorna a matriz de rotação em z simbólica
    """
    return sp.Matrix([[sp.cos(theta), -sp.sin(theta), 0, 0],
                      [sp.sin(theta), sp.cos(theta), 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])

def Denavit_Frame_Sym(variables):
    """
    :param variables: lista de variaveis de Denavit-Hartenberg
    :return: matriz de transformação homogênea

    Função que retorna a matriz simbólica de transformação homogênea de Denavit-Hartenberg a partir
    da transformação Tz*Tz*Rz*Tx"""
    Frame = Z_Sym_Translation(variables[0])*Z_Sym_Rotation(variables[1])*X_Sym_Translation(variables[2])*X_Sym_Rotation(variables[3])
    return Frame