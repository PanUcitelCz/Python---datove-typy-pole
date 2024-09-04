cislo = int(1) #Tohle je datový typ celého čísla
cislo_float = float(3.23) #Tohle je číslo s desetinou čárkou
text = str("String je sada znaků, například pro text")
Boolean = True #Booleanská hodnota, značí buď pravdu/nepravdu (True/False)

# Datový typ - pole, kde můžeme mít více prvků. Závorky píšeme pravý alt + d/f
# V poli se začíná na pozici 0. Ačkoliv je délka pole 6, poslední prvek je na pozici 5

            #0      #1         #2      #3       #4         #5
arrays = ["Ford", "Porsche", "Audi", "BMW", "Mercedes", "Škoda"]

# Tohle vypíše, úplně celé pole včetně hranatých závorek
# a uvozovek s čárkama.
print(arrays)

# Vypíše pouze jeden prvek bez uvozovek, čárek a hranatých závrek, vypíše jen Porsche
# Na pozici 1 se nachází string "Porsche".
print(arrays[1])

# Vypíše nám error, že není nic na pozici 6 v poli
# print(arrays[6])


# Vypíše všechny prvnky z pole, nelze x používat jak číslo
# Pomocí cyklu můžeme krásně vypsat každá prvek v poli pod sebe
for x in arrays:
    print(x)

# Vypíše všechny pole v délce, která je rovná delce pole
# len() je funkce, který dokáže vrátit hodnotu, která říka délku pole
# Tím že zde máme x jako číslo, které začíná defualtně od 0
# Můžeme vypsat všechny prvky pod sebe, a očíslovat jejich pořadí.
# Tím že pořadí je + 1, nám ošetřuje skutečnost, že cyklus začíná od nuly, 
# ale my chceme aby číslování začínalo od 1.
# Při volání arrays[x] se vypíše pomocí cyklu všechna pole. Prní cyklus je x  0.
# Proto se v prvním cyklu vypíše i arryas[0]
for x in range(len(arrays)):
    # "Chlupaté závorky" pravý alt + b/n
    # f v printu je z důvodu zřetězení stringu a proměnných/jiných datových typu
    # Do chlupatých závorek (správně složených závorek) píšeme proměnné nebo například int.
    print(f"{x+1}: {arrays[x]}")
