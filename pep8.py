"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para linguagem Python

The Zen Of Python

import this

A ideia da pep8 é que possamos escrever códigos Python de forma Pythônica.

------------------------------------------------ PEP8 ------------------------------------------------
[1] - Utilize Camel Case para nome de classes;


class Calculadora:
    pass


class CalculadoraCientifica:
    pass


[2] - Utilize nomes em minúsculo separados por underline para funções ou variáveis;


def soma():
    pass


def soma_dois():
    pass


numero = 2

numero_impar = 3


[3] - Utilize 4 espaços para identação! Obs: não use TAB

if 'a' in 'banana':
    print('tem')


[4] - Linhas em branco;
- Separar funções e definições de classe com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco.



class Calculadora:
    pass


class CalculadoraCientifica:
    pass


[5] imports devem ser sempre feitos em linhas separadas;

#import Errado

import sys, os


#import Certo

import sys
import os

#Não há problema em utilizar:
from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# imports devem ser colocados no topo do arquivo, logo depois de qualquer comentário ou docstrings
e antes de constantes ou váriaveis globais

[6] - Espaços em expressões e instruções:

#Não faça:

funcao( algo [ 1 ], { outro: 2 } )

#Faça:

funçao(algo[1], {outro: 2})

#Não faça:
algo (23)

#Faça:
algo(23)


[7] - Termine sempre uma instrução sempre com uma nova linha.


"""
import this
