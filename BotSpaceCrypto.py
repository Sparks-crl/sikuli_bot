
no_ammo = Pattern("1645046175827.png").similar(0.80)

fight = Pattern("fight.png").similar(0.83)

fight_boss = "1645051088401.png"


connect = "connect.png"

sign = "sign.png"

CONFIRM  = "1645056125926.png"

def PutFight():
    while True:
        try:
            naves_fight = Region(1482,267,67,32).text()
            n = naves_fight.split('/')
            print(n)
            i = int(n[0])
            break
        except:
            continue
    while (i < 15 and exists(fight)):
        click(fight)
        wait(4)
        i += 1
    click(Location(1402, 811))
    
while True:
    wait(20)
    if exists(no_ammo):
        click(Location(396, 414))
        PutFight()


