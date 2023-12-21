import random

def generuj_slovo():
    samohlasky = 'aeiouyáéíóúýě'
    souhlasky = 'bcdfghjklmnpqrstvwxzščřžďťň'
    
    pocet_slabik = random.randint(1, 3)
    
    slovo = ''.join([
        random.choice(list(souhlasky)) +
        random.choice(list(samohlasky))
        for _ in range(pocet_slabik)
    ])
    
    if random.choice([True, False]):
        slovo += random.choice(list(samohlasky))

    return slovo



def generuj_lorem_ipsum():
    pocet_odstavcu = None
    while pocet_odstavcu is None:
        try:
            pocet_odstavcu = int(input("Zadejte počet odstavců: "))
        except ValueError:
            print("Chyba: Zadávejte pouze celá čísla.")

    slov_na_odstavec = None
    while slov_na_odstavec is None:
        try:
            slov_na_odstavec = int(input("Zadejte počet slov na odstavec: "))
        except ValueError:
            print("Chyba: Zadávejte pouze celá čísla.")

    lorem_ipsum_text = []

    for _ in range(pocet_odstavcu):
        odstavec = ' '.join([generuj_slovo() for _ in range(slov_na_odstavec)])
        lorem_ipsum_text.append(odstavec)

    return '\n\n'.join(lorem_ipsum_text)

def uloz_do_souboru(text, nazev_souboru='lorem_ipsum.txt'):
    with open(nazev_souboru, 'w', encoding='utf-8') as soubor:
        soubor.write(text)

vygenerovany_text = generuj_lorem_ipsum()

print("\nVygenerovaný text:\n")
print(vygenerovany_text)

uloz_do_souboru(vygenerovany_text)
print(f"\nText byl uložen do souboru 'lorem_ipsum.txt'.")

