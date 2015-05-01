import RPi.GPIO as GPIO
import pygame

pygame.init()
pygame.key.set_repeat(100,100)
GPIO.setmode(GPIO.BOARD)

rpins =[29,31,33,35,37]
tpins[12,11,13,15,16]

ron =[0,0,0,0,0]
ton =[0,0,0,0,0]

for rpin in rpins:
    GPIO.setup(rpin, GPIO.OUT)
    GPIO.output(rpin,0)
for tpin in tpins:
    GPIO.setup(tpin, GPIO.OUT)
    GPIO.output(tpin,0)

thrust=0
thrustmax=31
rot=0
rotmax=31


bitarray32 = lambda n: map(int,list("0"*(5-len(bin(n)[2:]))+bin(n)[2:]))

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if thrust <thrustmax:
                    thrust+=1
            if event.key == pygame.K_s:
                if thrust>0:
                    thrust-=1
            if event.key == pygame.K_d:
                if rot < rotmax:
                    rot+=1
            if event.key == pygame.K_a:
                if rot>0:
                    rot-=1
            ton = bitarray32(thrust)
            ron = bitarray32(rot)
            for i in range(0,5):
                GPIO.output(tpins[i],ton[i])
                GPIO.output(rpins[i],ron[i])



