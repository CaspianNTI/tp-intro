#Prompt:
#jag vill skriva ett program som använder [att spara] för att mata in två tal. 
# Programet ska sedan skriva ut summan. 
# Programet ska använda [att upprepa] för att fortsätta köra tills att användaren skriver "stopp".

while True:  # [att upprepa]
    tal1 = input("Mata in det första talet (eller skriv 'stopp' för att avsluta): ")  # [att spara]
    if tal1.lower() == "stopp":
        break
    tal2 = input("Mata in det andra talet (eller skriv 'stopp' för att avsluta): ")  # [att spara]
    if tal2.lower() == "stopp":
        break
    summa = float(tal1) + float(tal2)  # [att spara]
    print("Summan är:", summa)