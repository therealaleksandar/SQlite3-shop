import sqlite3
from kveri import query,queryselectall,queryselectone
from ime_baze import ime_baze
from product_type_controlor import ProductTypeControlor,kontrolor_proizvoda_tipa

class ProductControlor:

    def dodaj_proizvod(self):
        sql="insert into Proizvod (Ime,Cena,ProizvodTipID) values (?,?,?)"
        print("UNOS PROIZVODA")
        sadrzaj=unos_proizvoda()
        query(sql,sadrzaj)
        print("Proizvod unesen")

    def prikazi_sve_proizvode(self):
        sql="select * from Proizvod"
        print("LISTA SVIH PROIZVODA")
        print("ID\t Ime\t\t Cena\t PrTipID")
        for proizvod in queryselectall(sql):
            print(proizvod[0],"\t",proizvod[1],"\t",proizvod[2],"\t",proizvod[3])

    def azuriraj_proizvod(self):
        self.prikazi_sve_proizvode()
        print("AZURIRANJE PROIZVODA")
        id_proizvoda=dobij_proizvod_id()
        sadrzaj=unos_proizvoda()
        sadrzaj+=(id_proizvoda,)
        sql="update Proizvod set Ime=?,Cena=?,ProizvodTipID=? where ProizvodID=?"
        query(sql,sadrzaj)
        print("Proizvod je azuriran!")

    def obrisi_proizvod(self):
        self.prikazi_sve_proizvode()
        print("BRISANJE PROIZVODA")
        id_proizvoda=dobij_proizvod_id()
        sql="delete from Proizvod where ProizvodID=?"
        query(sql,(id_proizvoda,))
        print("Proizvod je obrisan!")

    def prikazi_detalje_proizvoda(self):
        print("PRIKAZ DETALJA PROIZVODA")
        id_proizvoda= dobij_proizvod_id()
        sql="select * from Proizvod where ProizvodID=?"
        print("ID\t Ime\t\t Cena\t PrTipID")
        proizvod=queryselectone(sql,(id_proizvoda,))
        print(proizvod[0],"\t",proizvod[1],"\t",proizvod[2],"\t",proizvod[3])

def unos_proizvoda():
    while True:
        try:
            ime=input("Unesite ime: ")
            cena=float(input("Unesite cenu: "))
            kontrolor_proizvoda_tipa.prikazi_sve_proizvod_tipove()
            ptipid=int(input("Unesite ID tipa proizvoda: "))
            if provera_proizvod_tipa_id(ptipid):
                return (ime,cena,ptipid)
            else:
                print("ID proizvoda tipa koji ste uneli ne postoji. Molimo vas da probate ponovo.")
        except ValueError:
            print("Doslo je do greske pri unosu. Ponovite unos.")

def dobij_proizvod_id():
    with sqlite3.connect(ime_baze) as kon:
        kur=kon.cursor()
        kur.execute("select ProizvodID from Proizvod")
        prid=kur.fetchall()
        listaid=[]
        for i in prid:
            for j in i:
                listaid.append(j)
        while True:
            try:
                id_pr=int(input("Unesite ID proizvoda: "))
                if id_pr in listaid:
                    return id_pr
                else:
                    print("ID proizvoda koji ste uneli ne postoji. Molimo vas da probate ponovo.")
            except:
                print("Doslo je do greske, probajte ponovo!")

def provera_proizvod_tipa_id(id_protipa):
    with sqlite3.connect(ime_baze) as kon:
        kur=kon.cursor()
        kur.execute("select ProizvodTipID from ProizvodTip")
        prtipid=kur.fetchall()
        listaid=[]
        for i in prtipid:
            for j in i:
                listaid.append(j)
        return id_protipa in listaid
           

kontrolor_proizvoda=ProductControlor()

if __name__=="__main__":
    #kontrolor_proizvoda.dodaj_proizvod()
    kontrolor_proizvoda.prikazi_sve_proizvode()
    #kontrolor_proizvoda.azuriraj_proizvod()
    #kontrolor_proizvoda.obrisi_proizvod()
    kontrolor_proizvoda.prikazi_detalje_proizvoda()
