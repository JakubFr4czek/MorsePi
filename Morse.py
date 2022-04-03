from sense_hat import SenseHat
import os
import time
import pygame  # See http://www.pygame.org/docs
from pygame.locals import *

#one unit

pygame.init()
pygame.display.set_mode((640, 480))

sh = SenseHat()
sh.clear()  # Blank the LED matrix
    
W = [255, 255, 255]  # White
B = [0, 0, 0] #Black
R = [255, 0 ,0] #Red
G = [0, 255, 0] #Green

letter = ""

#matrix

dot = [
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, B, B,
B, B, B, W, W, B, B, B,
B, B, B, W, W, B, B, B,
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, B, B
]

line = [
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, B, B,
B, B, W, W, W, W, B, B,
B, B, W, W, W, W, B, B,
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, B, B
]    
        
def computeLetter(result):
    if result == ".-":
        sh.show_letter("A", W, B)
    elif result == "-...":
        sh.show_letter("B", W, B)
    elif result == "-.-.":
        sh.show_letter("C", W, B)
    elif result == "-..":
        sh.show_letter("D", W, B)
    elif result == ".":
        sh.show_letter("E", W, B)
    elif result == "..-.":
        sh.show_letter("F", W, B)
    elif result == "--.":
        sh.show_letter("G", W, B)
    elif result == "....":
        sh.show_letter("H", W, B)
    elif result == "..":
        sh.show_letter("I", W, B)
    elif result == ".---":
        sh.show_letter("J", W, B)
    elif result == "-.-":
        sh.show_letter("K", W, B)
    elif result == ".-..":
        sh.show_letter("L", W, B)
    elif result == "--":
        sh.show_letter("M", W, B)
    elif result == "-.":
        sh.show_letter("N", W, B)
    elif result == "---":
        sh.show_letter("O", W, B)
    elif result == ".--.":
        sh.show_letter("P", W, B)
    elif result == "--.-":
        sh.show_letter("Q", W, B)
    elif result == ".-.":
        sh.show_letter("R", W, B)
    elif result == "...":
        sh.show_letter("S", W, B)
    elif result == "-":
        sh.show_letter("T", W, B)
    elif result == "..-":
        sh.show_letter("U", W, B)
    elif result == "...-":
        sh.show_letter("V", W, B)
    elif result == ".--":
        sh.show_letter("W", W, B)
    elif result == "-..-":
        sh.show_letter("X", W, B)
    elif result == "-.--":
        sh.show_letter("Y", W, B)
    elif result == "--..":
        sh.show_letter("Z", W, B)
    elif result == ".----":
        sh.show_letter("1", W, B)
    elif result == "..---":
        sh.show_letter("2", W, B)
    elif result == "...--":
        sh.show_letter("3", W, B)
    elif result == "....-":
        sh.show_letter("4", W, B)
    elif result == ".....":
        sh.show_letter("5", W, B)
    elif result == "-....":
        sh.show_letter("6", W, B)
    elif result == "--...":
        sh.show_letter("7", W, B)
    elif result == "---..":
        sh.show_letter("8", W, B)
    elif result == "----.":
        sh.show_letter("9", W, B)
    elif result == "-----":
        sh.show_letter("0", W, B)
    else:
        sh.show_letter("", R, R)
        time.sleep(0.5)
        sh.clear()

def released(event, time):
    if time < 0.15:
        sh.set_pixels(dot)
        return "."
    else: 
        sh.set_pixels(line)
        return "-"

def eventHandler(event):
    if event.type == KEYDOWN:
        if event.key == pygame.K_RETURN:
            return "pressed"
    elif event.type == KEYUP:
        if event.key == pygame.K_RETURN:
            return "released"

last = -1;
afterLetter = -1
pressed = False

while True:
    
    if last != -1:
        if time.time() - last > 0.6 and pressed == False:
            computeLetter(letter)
            letter = ""
            last = -1
            afterLetter = time.time()
    if afterLetter != -1:
        if time.time() - afterLetter > 1:
            sh.clear()
            afterLetter = -1
    
    for event in pygame.event.get():
        inp = eventHandler(event)
        if inp == "pressed":
            last = time.time()
            afterLetter = -1
            pressed = True
        if inp == "released":
            letter = letter + released(event, time.time() - last)
            pressed = False
            last = time.time()