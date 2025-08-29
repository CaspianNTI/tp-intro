print("Addition heltal")

complete = False

while not(complete):
    try:
        x = int(input("Första talet: "))
        y = int(input("Andra talet: "))
        sum = x + y
        print(f"Summa: {sum}")
        complete = True
    except:
        print("endast heltal bro")
