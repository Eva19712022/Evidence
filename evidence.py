from pojistenec import Pojistenec
class Evidence:
    def __init__(self):
        pass

    def pridejZaznam(self):
            
        jmeno = (input("Zadejte jméno pojištěného:\n"))    
        prijmeni = (input("Zadejte přijmení pojištěného:\n"))
        vek = (input("Zadejte věk pojištěného:\n"))
        telefon = (input("Zadejte telefonní číslo pojištěného:\n"))
        novyPojistenec = Pojistenec(jmeno,prijmeni,vek,telefon)
        return (novyPojistenec)
    
    def zobrazPojistence(self):
        return()
                        
