from evidence import Evidence    #importuji všechny třídy
from pojistenec import Pojistenec
from datetime import date

pojistenci = [] # seznam 
date.today() #modul datumu
print()
print("Vítejte v aplikaci Evidence pojištěných")
print("Dnešní datum je :  " + str(date.today()))
evidence = Evidence() 
print("========================================\n")

pokracovat ="ano"  #opakovaná podmínka
while pokracovat == "ano": 
    
    print("1 - Přidat nového pojištěného")
    print("2 - Vypsat všechny pojištěné")
    print("3 - Vyhledat pojištěného")
    print("4- Konec")
    print()

    vyber = input("Vyberte si akci:\n")
    if vyber == ("1"):       
        print("Přidat nového pojištěneho")
        novyPojistenec = evidence.pridejZaznam()
        pojistenci.append(novyPojistenec)  
        print("Data byla uložena. Pokračujte libovolnou klávesou...")
        print()

    elif vyber == ("2"):
        
        print("Zobrazit všechny pojištěné\n")        
        for i in pojistenci: 
           print(i)
         
    
    elif vyber == ("3"):
        print("hledany_pojistenec")
        hledane_jmeno = input("Zadej hledané jméno:\n")
        hledane_prijmeni = input("Zadejte hledané přijmení: ")
        for pojistenec in pojistenci:
            if hledane_jmeno == pojistenec.jmeno and hledane_prijmeni == pojistenec.prijmeni:
                print(pojistenec)
            

    elif vyber == ("4"):
        print("Program vás vrátil na začátek možností výběru")
        print()
    else:
        print("Zadal jste chybný vstup")
