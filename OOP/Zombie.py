from Enemigo import *
import random

class Zombie(Enemigo):
    def _init_(self, puntos_energia=10, ataque=1):
        super()._init_(tipo_enemigo='Zombie', puntos_energia=puntos_energia,ataque=ataque)

    def habla(self):
        print("Hummmm.....*")

    def propagar_enfermedad(self):
        print("El Zombie esta tratando de propagar la enfermedad!!")

    def ataque_especial(self):
        print("Ogro ataque especial")
        funciona_ataque_especial = random.random() <0.50
        if funciona_ataque_especial:
            self.ataque +=2
            print('Zombie ha regenerado su energia con 2HP!!!!')