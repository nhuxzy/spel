import voorwerpen
import dorp
import rivier

def activate():
    print("----Bos----")
    print("Het bos is donker en mistig. Je hoort ritselende geluiden.")
    print("Wil je een EDELSTEEN zoeken, naar de RIVIER lopen of TERUG naar dorp?")
    
    antwoord = input("> ").lower()
    
    if antwoord == "edelsteen" :
        voorwerpen.edelsteenGepakt = True
        print("Je hebt een glinsterende edelsteen gevonden!")
        activate()
    elif antwoord == "rivier" :
        rivier.activate()
    elif antwoord == "terug" :
        dorp.activate()
    else:
        print("Dat begrijp ik niet.")
        activate()