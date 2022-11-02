#!/usr/bin/env python

# les imports standard en premier
from random import randint

import pygame as pg

# on initialise pygame et on crée une fenêtre de 400x300 pixels
pg.init()
screen = pg.display.set_mode((400, 300))

# Objet de gestion du temps
clock = pg.time.Clock()

while True:
    clock.tick(1)

    for event in pg.event.get():
        pass  # 👈 ajouter le code de gestion des événements ici

    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    screen.fill(random_color)
    pg.display.update()

pg.quit()