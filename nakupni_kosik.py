zbozi = ["CPU", "GPU", "RAM", "HDD", "SSD", "Motherboard", "Chlazení vodní", "Zdroj", "Case"]
kosik =[]

def vypis_zbozi():
    print("---------------------------")
    print(" ")
    print("Zde je zboží")
    print(" ")
    print("---------------------------")

def vypis_kosik():
    print("---------------------------")
    print(" ")
    print("Zde je Váš košík")
    print(" ")
    print("---------------------------")

def vypis_pole(prvek):
    
    for x in range(len(prvek)): 
        print(f"Komponent s číslem {x+1}: {prvek[x]}")
    
    print(" ")
    print("---------------------------")


while(True):
    vypis_zbozi()
    vypis_pole(zbozi)

    vyber = int(input("Zde zadejte Vaší volbu produktu podle čísla: "))

    if 0<vyber<=len(zbozi):
        kosik.append(zbozi[vyber])
        vypis_kosik()
        vypis_pole(kosik)
        zbozi.pop(vyber)
