from shop_controlor import ShopControlor,kontrolor_shopa
from product_type_controlor import ProductTypeControlor,kontrolor_proizvoda_tipa
from product_controlor import ProductControlor,kontrolor_proizvoda
from customer_controlor import CustomerControlor,kontrolor_kupaca
from order import Order,kontrolor_narudzbine
from ime_baze import ime_baze
#from IPython.display import clear_output

# def napravi_ime_baze():
#     with open('ime_baze.py','w') as ime:
#         ime_b=input("Unesite ime baze koju zelite napraviti: ")+".db"
#         ime.write(f"ime_baze='{ime_b}'")

def prikazi_glavni_meni():
    print("\nMENI ZA KONTROLU SHOPA\n")
    print("1. Napravite bazu")
    print("2. Upravljajte bazom kupaca")
    print("3. Upravljajte bazom tipova proizvoda")
    print("4. Upravljajte bazom proizvoda")
    print("5. Upravljajte bazom narudzbina\n")
    print("0. Izadji\n")

def prikazi_meni_kupca():
    print("\nUPRAVLJANJE KUPCIMA\n")
    print("1. Dodaj kupca")
    print("2. Obrisi kupca")
    print("3. Azuriraj kupca")
    print("4. Prikazi detalje kupca")
    print("5. Prikazi listu svih kupaca\n")
    print("0. Nazad\n")

def prikazi_meni_tipa_proizvoda():
    print("\nUPRAVLJANJE TIPOVIMA PROIZVODA\n")
    print("1. Dodaj tip proizvoda")
    print("2. Obrisi tip proizvoda")
    print("3. Azuriraj tip proizvoda")
    print("4. Prikazi listu svih tipova proizvoda\n")
    print("0. Nazad\n")

def prikazi_meni_proizvoda():
    print("\nUPRAVLJANJE PROIZVODIMA\n")
    print("1. Dodaj proizvod")
    print("2. Obrisi proizvod")
    print("3. Azuriraj proizvod")
    print("4. Prikazi detalje proizvoda")
    print("5. Prikazi listu svih proizvoda\n")
    print("0. Nazad\n")

def prikazi_meni_narudzbina():
    print("\nUPRAVLJANJE NARUDZBINAMA\n")
    print("1. Dodaj narudzbinu")
    print("2. Obrisi narudzbinu")
    print("3. Azuriraj narudzbinu")
    print("4. Prikazi detalje narudzbine")
    print("5. Prikazi listu svih narudzbina\n")
    print("0. Nazad\n")

def unos():
    while True:
        try:
            odg=int(input("Unesite vas izbor: "))
            if odg in range(6):
                return odg
            else:
                print("Vas izbor se ne nalazi u opcijama!")
        except ValueError:
            print("Vas izbor se ne nalazi u opcijama!")

def meni_kupca():
    while True:
        prikazi_meni_kupca()
        print()
        izbor=unos()
        print()
        if izbor==1:
            kontrolor_kupaca.dodaj_kupca()
        elif izbor==2:
            kontrolor_kupaca.obrisi_kupca()
        elif izbor==3:
            kontrolor_kupaca.azuriraj_kupca()
        elif izbor==4:
            kontrolor_kupaca.prikazi_detalje_kupca()
        elif izbor==5:
            kontrolor_kupaca.prikazi_sve_kupce()
        else:
            break

def meni_tipa_proizvoda():
    while True:
        prikazi_meni_tipa_proizvoda()
        print()
        izbor=unos()
        print()
        if izbor==1:
            kontrolor_proizvoda_tipa.dodaj_tip()
        elif izbor==2:
            kontrolor_proizvoda_tipa.obrisi_tip()
        elif izbor==3:
            kontrolor_proizvoda_tipa.azuriraj_tip()
        elif izbor==4:
            kontrolor_proizvoda_tipa.prikazi_sve_proizvod_tipove()
        else:
            break

def meni_proizvoda():
    while True:
        prikazi_meni_proizvoda()
        print()
        izbor=unos()
        print()
        if izbor==1:
            kontrolor_proizvoda.dodaj_proizvod()
        elif izbor==2:
            kontrolor_proizvoda.obrisi_proizvod()
        elif izbor==3:
            kontrolor_proizvoda.azuriraj_proizvod()
        elif izbor==4:
            kontrolor_proizvoda.prikazi_detalje_proizvoda()
        elif izbor==5:
            kontrolor_proizvoda.prikazi_sve_proizvode()
        else:
            break

def meni_narudzbine():
    while True:
        prikazi_meni_narudzbina()
        print()
        izbor=unos()
        print()
        if izbor==1:
            kontrolor_narudzbine.dodaj_naruzdbinu()
        elif izbor==2:
            kontrolor_narudzbine.obrisi_narudzbinu()
        elif izbor==3:
            kontrolor_narudzbine.azuriraj_narudzbinu()
        elif izbor==4:
            kontrolor_narudzbine.prikazi_detalje_narudzbine()
        elif izbor==5:
            kontrolor_narudzbine.prikazi_sve_narudzbine()
        else:
            break

if __name__=="__main__":
    while True:
        prikazi_glavni_meni()
        print()
        izbor=unos()
        print()
        if izbor==1:
            kontrolor_shopa.kreiraj_sve() 
        elif izbor==2:
            #clear_output()
            print('\n'*100)
            meni_kupca()
        elif izbor==3:
            #clear_output()
            print('\n'*100)
            meni_tipa_proizvoda()
        elif izbor==4:
            #clear_output()
            print('\n'*100)
            meni_proizvoda()
        elif izbor==5:
            #clear_output()
            print('\n'*100)
            meni_narudzbine()
        else:
            print("Dovidjenja!")
            break
