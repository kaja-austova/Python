import random

def hadej_cislo():
    cislo = random.randint(1,100)
    pokusy = 0
    print("Myslím si číslo mezi 1 a 100")

    while True:
        guess = int(input("Hádej číslo: "))
        pokusy += 1

        if guess < cislo:
            print ("Moc nízko! Zkus to znovu.")
        elif guess > cislo:
            print ("Moc vysoko! Zkus to znovu.")
        else:
            print ("Skvěle! Uhodl si číslo v", pokusy, "pokusech")

hadej_cislo()