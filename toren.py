import rivier
import voorwerpen

def activate():
    if voorwerpen.allesGepakt():
        print("----Toren----")
        print("De sleutel begint te gloeien...")
        print("Een magische deur verschijnt in de muur van de toren.")
        print("Je hebt alle voorwerpen verzameld en het geheim van het verhaal ontdekt!")
        print("JE HEBT HET SPEL UITGESPEELD")
        exit()
    
    print("----Toren----")
    print("Je staat bij de toren, maar je hebt niet alle voorwerpen verzameld. Ga TERUG naar de rivier.")
    
    antwoord = input("> ").lower()
    

    if antwoord == "rivier" or antwoord == "terug":
        rivier.activate()
    else:
        print("Dat begrijp ik niet.")
   
    activate()