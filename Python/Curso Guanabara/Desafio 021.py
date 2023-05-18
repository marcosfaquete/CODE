"""
    Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
    # Dica usar módulos.

"""

from pygame import mixer
mixer.init()
mixer.music.load('021.mp3')
mixer.music.play()

