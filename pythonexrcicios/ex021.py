import pygame
import time  # Para evitar uso excessivo de CPU

# Inicializa apenas o mixer (som)
pygame.mixer.init()

# Carrega a música (certifique-se de que o nome e caminho estão corretos)
pygame.mixer.music.load("Loucura e Travessura.mp3")

# Toca a música
pygame.mixer.music.play()
print("Tocando música...")

# Espera a música terminar
while pygame.mixer.music.get_busy():
    time.sleep(0.1)  # Aguarda 0.1s entre cada checagem

print("Música finalizada.")
