import dorp
import voorwerpen

def activate():
    print("Je staat in het kasteel. Het is donker en stil. Er liggen overal oude boeken.")
    print("Wil je een BOEK pakken of naar het DORP gaan?")
    
    antwoord = input ("> ").lower()
    
    if antwoord == "boek" :
        voorwerpen.boekGepakt = True
        print("Je hebt het oude boek gepakt.")
        activate()
    elif antwoord == "dorp" :
        dorp.activate()
    else:
        print("Dat begrijp ik niet")
        activate()