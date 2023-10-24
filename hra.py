import random

def uvod():
    print("Vítej v textové hře 'Ztracený v lese'!")
    print("Nacházíš se v temném lese a tvůj úkol je najít cestu zpět domů.")
    print("Na tvé cestě se budeš muset rozhodovat a tvoje rozhodnutí budou mít dopad na tvůj osud.")
    print("Buď opatrný a správně vybírej, abys se dostal domů v bezpečí.")
    print()

def konec():
    print("Děkuji za hraní hry 'Ztracený v lese'!")

def zacni_hru():
    uvod()
    while True:
        volba = input("Co uděláš? (Jdi doprava / Jdi doleva / Jdi rovně): ").lower()
        if "doprava" in volba:
            doprava()
        elif "doleva" in volba:
            doleva()
        elif "rovně" in volba:
            rovne()
        else:
            print("Nerozumím tvému příkazu, zkuste to znovu.")

def doprava():
    print("Jdeš doprava a narazíš na starý most.")
    print("Most vypadá trochu rozpadle, ale zdá se, že je dostatečně pevný.")
    print("Co uděláš?")
    volba = input("Přejdeš most (Přejít most) nebo se vrátíš (Vrátit se zpět)? ").lower()
    if "přejít most" in volba:
        print("Podařilo se ti přejít most. Pokračuješ dále lesem.")
        setkani_s_lidmi()
    elif "vrátit se zpět" in volba:
        print("Vracíš se zpět na křižovatku.")
    else:
        print("Nerozumím tvému příkazu, zkuste to znovu.")

def doleva():
    print("Jdeš doleva a narazíš na starou jeskyni.")
    print("V jeskyni vidíš záblesky zlata. Co uděláš?")
    volba = input("Seber zlato (Sebrat zlato) nebo pokračuj dál (Pokračovat dál)? ").lower()
    if "sebrat zlato" in volba:
        print("Sebral jsi zlato, ale z jeskyně vylétl drak a požral tě.")
        print("Konec hry.")
        konec()
    elif "pokračovat dál" in volba:
        print("Vracíš se zpět na křižovatku.")
    else:
        print("Nerozumím tvému příkazu, zkuste to znovu.")

def rovne():
    print("Jdeš rovně a narazíš na starý dům.")
    print("Vypadá opuštěný, ale slyšíš hlasitý zvuk smíchu uvnitř.")
    volba = input("Vstoupíš do domu (Vstoupit do domu) nebo utečeš (Uteci)? ").lower()
    if "vstoupit do domu" in volba:
        print("Uvnitř domu je oslava a připojil ses k veselí. Získáváš nové přátele a cestu z lesa znáš.")
        print("Gratuluji, vyhrál jsi hru!")
        konec()
    elif "uteci" in volba:
        print("Utíkáš zpět na křižovatku.")
    else:
        print("Nerozumím tvému příkazu, zkuste to znovu.")

def setkani_s_lidmi():
    print("Pokračuješ dál lesem a narazíš na skupinu lidí.")
    print("Jsou to místní obyvatelé, kteří ti nabízí pomoc.")
    volba = input("Přijmeš jejich pomoc (Přijmout pomoc) nebo pokračuješ sám (Pokračovat sám)? ").lower()
    if "přijmout pomoc" in volba:
        print("Společně s místními obyvateli se ti podařilo najít cestu ven z lesa.")
        print("Gratuluji, vyhrál jsi hru!")
        konec()
    elif "pokračovat sám" in volba:
        print("Rozhodl jsi se pokračovat sám. Pokračuješ dál lesem.")
    else:
        print("Nerozumím tvému příkazu, zkuste to znovu.")

if __name__ == "__main__":
    zacni_hru()
