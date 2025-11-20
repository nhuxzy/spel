import bos
import toren
import voorwerpen

def activate():
    global sleutelGepakt, boekGepakt
    print("----Rivier----")
    print("De rivier stroomt rustig. Je ziet een boek drijven en glinterende stenen op de oever.")
    print("Wil je een BOEK pakken, OVERZWEMMEN naar een eiland, naar de TOREN gaan of TERUG naar het bos?")
    
    antwoord = input("> ").lower()
    
    if antwoord  == "boek" :
        voorwerpen.boekGepakt = True
        print("Je hebt het drijvende boek gepakt!")
        activate()
    elif antwoord == "overzwemmen" :
        voorwerpen.sleutelGepakt = True
        print("Je zwemt naar een verborgen eiland en vindt een oude sleutel!")
        activate()
    elif antwoord == "terug" :
        bos.activate()
    elif antwoord == "toren":
        toren.activate()
    else:
        print("Dat begrijp ik niet.")
        activate()