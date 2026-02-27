from Enemigo import *
import random

class Ogro(Enemigo):
    def _init_(self, puntos_energia=20, ataque=3):
        super()._init_(tipo_enemigo='Ogro', puntos_energia=puntos_energia, ataque=ataque)

    def habla(self):
        print("Ogro aplasta todo!!!")

    def ataque_especial(self):
        print("Ogro ataque especial")
        funciona_ataque_especial = random.random() <0.20
        if funciona_ataque_especial:
            self.ataque +=4
            print('Ogro enojado y incremento su ataque por 4!!!')