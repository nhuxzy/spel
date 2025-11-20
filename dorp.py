import bos
import kasteel
import voorwerpen

def activate():
    print("----Dorp----")
    print("Je bent in het dorp. Er is een markt een een taverne.")
    print("Wil je een MES pakken, naar het BOS gaan of TERUG naar kasteel?")
    
    antwoord = input("> ").lower()
    
    if antwoord == "mes" :
        voorwerpen.mesGepakt = True
        print("Je hebt het mes gepakt.")
        activate()
    elif antwoord == "bos" :
        bos.activate()
    elif antwoord == "terug" :
        kasteel.activate()
    else:
        print("Dat begrijp ik niet.")
        activate()