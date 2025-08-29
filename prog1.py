import random

kort1 = random.randint(1, 11)
kort2 = random.randint(1, 11)

total = kort1 + kort2
print(f"Din giv är {kort1} och {kort2}, vilket ger totalen {total}")

if total == 21:
    print("Blackjack!") 

else:
    hus1 = random.randint(1, 11)
    hus2 = random.randint(1, 11)

    hustotal = hus1 + hus2
    print(f"Huset drar {hus1} och {hus2}, vilket ger totalt {hustotal}")

    stanna = "n"
    while stanna.lower != "j":
        print(f"Din totala summa är {total}")

        if total == 21:
            print("Blackjack")
            break

        elif total > 21:
            print("Du blav tjock")
            break
        
        stanna = input("Stanna? (j/n)")

        if stanna.lower() == "j":
            print(f"Du stannar på {total}")
            break
        else:
            total += random.randint(1, 11)
    
    while hustotal < 17 or total < 21:
        hustotal += random.randint(1, 11)
        print(f"Huset har {hustotal}")

    if hustotal == 21 or hustotal > total:
        print("huset vann")
    elif hustotal == total:
        print("Push! Ingen vann")
    else:
        print("Du vann")