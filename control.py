import wiringpi2 as wp
wp.wiringPiSetupPhys()

pygame.init()
pygame.key.set_repeat(100,100)

rpins =[29,31,33,35,37]
tpins=[12,11,13,15,16]

ron =[0,0,0,0,0]
ton =[0,0,0,0,0]

for rpin in rpins:
    print(rpin)
    wp.pinMode(rpin,1)
    wp.digitalWrite(rpin,0)
print("\n\n")
for tpin in tpins:
    print(tpin)
    wp.pinMode(tpin,1)
    wp.digitalWrite(tpin,0)
print("\n")
thrust=0
thrustmax=31
rot=0
rotmax=31


bitarray32 = lambda n: map(int,list("0"*(5-len(bin(n)[2:]))+bin(n)[2:]))

while True:
    key = raw_input("-->")
    print("keypress")
    if key =="w":
        if thrust <thrustmax:
            thrust+=1
    if key== "s":
        if thrust>0:
            thrust-=1
    if key =="d":
        if rot < rotmax:
            rot+=1
    if key=="a":
        if rot>0:
            rot-=1
    ton = bitarray32(thrust)
    ron = bitarray32(rot)
    for i in range(0,5):
        wp.digitalWrite(tpins[i],ton[i])
        wp.digitalWrite(rpins[i],ron[i])
    print("thrust is: " + str(thrust))
    print("rot is: " + str(rot))



