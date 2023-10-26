import time
import random

def uvod():
    print("Vítej v textové hře 'Útěk ze školy'!")
    print("Nacházíš se ve třídě a tvůj úkol je ze školy utéct a při nejlpepším se vyhnout všem učitelům.")
    print("Dávej pozor, protože škola skrývá spoustu nebezpečí.")

def konec():
    print("Děkuji za hraní hry 'Útěk ze školy'!")

def zacatek_hry():
    uvod()
    volba = input("Co uděláš? Půjdeš k oknu (okno) nebo ke dveřím (dveře)?").lower()
    if "dveře" in volba:
        dveře()
    elif "okno" in volba:
        okno()
    else:
        print("Nerozumím tvému příkazu, zkuste to znovu.")

def okno():
    print("Šel jsi k oknu, ale je bohužel zamčené.")
    volba = input("Budeš klíč hledat (hledat klíč), nebo spíš zkusíš dveře (jít ke dveřím)?").lower()
    if "hledat klíč" in volba:
        print("Našel jsi klíč a jsi osvobozen ze školy!")
        print("Konec hry")
        konec()
    elif "jít ke dveřím" in volba:
        dveře()
    else:
        print("Nerozumím tvému příkazu, zkuste to znovu.")

def dveře():
    print("Jdeš ke dveřím a ty byli poněkud záhadně odemčené.")
    print("Jdeš na chodbu.")
    chodba()

def chodba():
    print("Na chodbě ale potkáš paní učitelku Matlerovou.")
    print("Ta když tě uvidí tak ti hned zadá ať jí napíšeš slohovku.")
    volba = input("Půjdeš si napsat slohovku (napsat slohovku), nebo se jí pokusíš utýct (útěk)?").lower()
    if "napsat slohovku" in volba:
        slohovka()
    elif "útěk" in volba:
        cislo = random.randint(1,2)
        str_cislo = str(cislo)
        if '1' in str_cislo:
            print("Podařilo se ti před paní učitelkou utýct a jdeš tedy k šatnám.")
            šatny()
        elif '2' in str_cislo:
            print("Bohužel se ti před paní učitelkou nepodařilo utýct a chytila tě.")
            slohovka()
    else:
        print("Nerozumím tvému příkazu, zkuste to znovu.")

def slohovka():
        print("Paní učitelka tě odvede do jedné ze tříd, kde si budeš muset tu slohovku napsat.")
        print("Tak se do toho vrhneš.")
        time.sleep(2)
        print("Pořád píšeš......")
        time.sleep(2)
        print("Ta slohovka má mít 250 slov, tak si s ní chceš dát záležet.")
        time.sleep(2)
        print("Když už tu slohovku konečně dopíšeš, tak tě paní učitelka nechá konečně na pokoji.")
        print("Jdeš tedy k šatnám.")
        šatny()

def šatny():
    print("U šaten bohužel potkáš pana školníka.")
    print("Ten ti řekne aby sis sundal boty, protože prý 'děláš neskutečný bordel', nebo že si ten svinčík máš uklidit.")
    volba = input("Sundáš si boty (sundat boty), nebo si radši ten nepořádek uklidíš (uklidit)?").lower()
    if "sundat boty" in volba:
        print("Sundal sis boty a jdeš naboso až k východu ze školy.")
        východ()
    elif "uklidit" in volba:
        print("Pan školník ti dá lopatku a koště a ty si musíš uklidit všechno co ti z bot spadalo a možná i to co spadalo spolužákům.")
        print("Když to douklízíš, pan školník tě nechá jít.")
        východ()
    else:
        print("Nerozumím tvému příkazu, zkuste to znovu.")


def východ():
    print("U východu ale potkáš další a teď snad už poslední nemilou návštěvu.")
    print("Před tebou se objeví obávaný pan učitel Šmehlík.")
    print("Ten chce po tobě aby jsi udělal 10 kliků.")
    volba = input("Uděláš těch 10 kliků (kliky), nebo se radši pokusíš utýct (útěk)?").lower()
    if "kliky" in volba:
        kliky()
    elif "útěk" in volba:
        cislo = random.randint(1, 2)
        str_cislo = str(cislo)
        if '1' in str_cislo:
            print("Podařilo se ti před Šmehlíkem utýct a tím pádem jsi unikl ze školy.")
            konec()
        elif '2' in str_cislo:
            print("Nepodařilo se ti před Šmehlíkem utýct, a ty kliky si tím pádem budeš muset udělat.")
            kliky()
    else:
        print("Nerozumím tvému příkazu, zkuste to znovu.")

def kliky():
        print("Ty si teda přemůžeš a hezky to před ním odklikuješ.")
        print("Po klicích jsi trochu unavený, ale pořád se zvládneš zvednout a teď už v klidu odejít ze školy.")
        konec()

zacatek_hry()