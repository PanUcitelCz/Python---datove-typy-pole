zbozi = ["CPU", "GPU", "RAM", "HDD", "SSD", "Motherboard", "Chlazení vodní", "Zdroj", "Case"]
kosik = []

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

def pridat_do_kosiku_vyberem(vyber):
    # Přidání do košíku podle čísla
    kosik.append(zbozi[vyber-1])
    zbozi.pop(vyber-1)

def pridat_do_kosiku_nazvem(nazev):
    # Přidání do košíku podle názvu, pokud se najde
    if nazev in zbozi:
        kosik.append(nazev)
        zbozi.remove(nazev)
    else:
        print(f"Produkt s názvem '{nazev}' nebyl nalezen.")

while(True):
    if len(zbozi) == 0:
        print("Už nemůžeš přidat další zboží, košík je plný!")
        break

    vypis_zbozi()
    vypis_pole(zbozi)

    volba = input("Zadejte číslo nebo název produktu, který chcete přidat do košíku: ")

    if volba.isdigit():  # Zda je volba číslo
        vyber = int(volba)
        if 0 < vyber <= len(zbozi):
            pridat_do_kosiku_vyberem(vyber)
        else:
            print("Neplatná volba čísla.")
    else:
        pridat_do_kosiku_nazvem(volba)

    vypis_kosik()
    vypis_pole(kosik)
