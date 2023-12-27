# import pygame as pg
import json

# pg.init()
# pg.display.set_caption('My Game')
# screen = pg.display.set_mode((800, 600))
# pg.display.flip()

with open ('score.json', "r") as json_file:
    python_Daten = json.load(json_file)

    print((python_Daten["The last choices"].count('RED')/10)*100)