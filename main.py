# Calculadora de quanto vai sobrar pro beta

#Bibliotecas
from time import sleep
from random import randint
#Utilize pip install pygame-ce
import pygame

#Pygame
pygame.init()

#Painel Inicial
print("-="*15)
print("Calculadora do betinha")
print("-="*15)
print("Carregando...")
sleep(3)
while True:
    name = input("Digite o nome do betinha: ")
    sobrou = randint(1, 10)

    if sobrou == 10:
        print("Carregando...")
        sleep(3)
        print(f"Parabéns, sobrou algo pro betinha {name}, isso é um milagre, sinta-se honrado.")
        testar = input("Deseja testar outro nome de betinha? [S/N] ")
        if testar == "N":
            break

    else:
        print("Carregando...")
        sleep(3)
        print(f"Não sobrou nada pro maldito betinha {name}.")
        pygame.mixer.music.load("Brutal.mp3")
        pygame.mixer.music.play()
        sleep(4)
        testar = input("Deseja testar outro nome de betinha? [S/N] ")
        if testar == "N":
            break