boekGepakt = False
mesGepakt = False
sleutelGepakt = False
edelsteenGepakt = False

def info():
    print("----Kasteel----")
    print("Je wordt wakker in een verlaten kasteel. Je weet niet hoe je hier bent gekomen.")
    print("Je hoort een mysterieuze stem fluisteren: 'Zoek de vier voorwerpen..'")
    print("Deze voorwerpen zijn:")
    print("-Een magische boek")
    print("-Een mes")
    print("-Een sleutel")
    print("-Een edelsteen")
    print("Ze liggen verstopt in vijf plaatsen: het kasteel, het dorp, het bos, de rivier en de toren.")
    print("Vind alle vier de voorwerpen om de magische deur te openen.")
    print("Je avontuur begint nu")
    
    
def kasteel():
    global boekGepakt
    print("Je staat in het kasteel. Het is donker en stil. Er liggen overal oude boeken.")
    print("Wil je een BOEK pakken of naar het DORP gaan?")
    
    antwoord = input ("> ").lower()
    
    if antwoord == "boek" :
        boekGepakt = True
        print("Je hebt het oude boek gepakt.")
        dorp()
    elif antwoord == "dorp" :
        dorp()
    else:
        print("Dat begrijp ik niet")
        kasteel()
    
        
def dorp():
    global mesGepakt
    print("----Dorp----")
    print("Je bent in het dorp. Er is een markt een een taverne.")
    print("Wil je een MES pakken, naar het BOS gaan of TERUG naar kasteel?")
    
    antwoord = input("> ").lower()
    
    if antwoord == "mes" :
        mesGepakt = True
        print("Je hebt het mes gepakt.")
        bos()
    elif antwoord == "bos" :
        bos()
    elif antwoord == "terug" :
        kasteel()
    else:
        print("Dat begrijp ik niet.")
        dorp()

def bos():
    global edelsteenGepakt
    print("----Bos----")
    print("Het bos is donker en mistig. Je hoort ritselende geluiden.")
    print("Wil je een EDELSTEEN zoeken, naar de RIVIER lopen of TERUG naar dorp?")
    
    antwoord = input("> ").lower()
    
    if antwoord == "edelsteen" :
        edelsteenGepakt = True
        print("Je hebt een glinsterende edelsteen gevonden!")
        rivier()
    elif antwoord == "rivier" :
        rivier()
    elif antwoord == "terug" :
        dorp()
    else:
        print("Dat begrijp ik niet.")
        bos()

def rivier():
    global sleutelGepakt, boekGepakt
    print("----Rivier----")
    print("De rivier stroomt rustig. Je ziet een boek drijven en glinterende stenen op de oever.")
    print("Wil je een BOEK pakken, OVERZWEMMEN naar een eiland, naar de TOREN gaan of TERUG naar het bos?")
    
    antwoord = input("> ").lower()
    
    if antwoord  == "boek" :
        boekGepakt = True
        print("Je hebt het drijvende boek gepakt!")
        toren()
    elif antwoord == "overzwemmen" :
        sleutelGepakt = True
        print("Je zwemt naar een verborgen eiland en vindt een oude sleutel!")
        toren()
    elif antwoord == "terug" :
        bos()
    else:
        print("Dat begrijp ik niet.")
        rivier()


def toren():
    global edelsteenGepakt, sleutelGepakt, boekGepakt, mesGepakt
    
    if boekGepakt and mesGepakt and sleutelGepakt and edelsteenGepakt:
        print("----Toren----")
        print("De sleutel begint te gloeien...")
        print("Een magische deur verschijnt in de muur van de toren.")
        print("Je hebt alle voorwerpen verzameld en het geheim van het verhaal ontdekt!")
        print("JE HEBT HET SPEL UITGESPEELD")
        exit()
    
    print("----Toren----")
    print("Je staat bij de toren, maar je hebt niet alle voorwerpen verzameld. Ga TERUG naar de rivier.")
    
    antwoord = input("> ").lower()
    

    if antwoord == "rivier" :
        rivier()
    else:
        print("Dat begrijp ik niet.")
   
    toren()

