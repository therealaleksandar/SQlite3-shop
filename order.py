import sqlite3
from ime_baze import ime_baze
from kveri import query,queryselectone
from customer_controlor import CustomerControlor,kontrolor_kupaca
from product_controlor import ProductControlor,kontrolor_proizvoda

class Order:

    def dodaj_naruzdbinu(self):
        print("UNOS NARUDZBENICE")
        sql="insert into NarudzbinaKupca (Datum,Vreme,KupacID) values (?,?,?)"
        query(sql,unos_narudzbenice_kupca())
        sql2="insert into NarudzbinaPredmet (NarudzbinaID,ProizvodID,Kolicina) values (?,?,?)"
        query(sql2,dobijanje_poslednje_naruzdbenice_kupca()+unos_narudzbenice_predmeta())

    def prikazi_sve_narudzbine(self):
        np={}
        nk={}
        s=0
        for p,k in dobij_sve_narudzbine():
            s+=1
            np[s]=np.get(s,p)
            nk[s]=nk.get(s,k)
        print("LISTA SVIH NARUDZBINA")
        print()
        print("NarPrID\t ProID\t Kol.\t Datum Nar.\t Vreme\t KupacID")
        for knp in np:
            print(np[knp][0],"\t",np[knp][2],"\t",np[knp][3],"\t",
            nk[knp][1],"\t",nk[knp][2],"\t",nk[knp][3])

    def prikazi_detalje_narudzbine(self):
        print("PRIKAZ DETALJA NARUDZBINE")
        id_nar=unos_nar_pr_id()
        sql='select * from NarudzbinaPredmet where NarudzbinaPredmetID=?'
        sql2='select * from NarudzbinaKupca where NarudzbinaID=?'
        svi=queryselectone(sql,id_nar)+queryselectone(sql2,id_nar)
        sql3='select Ime,Prezime,Mesto from Kupac where KupacID=?'
        svi+=queryselectone(sql3,(svi[7],))
        sql4='select Ime from Proizvod where ProizvodID=?'
        svi+=queryselectone(sql4,(svi[2],))
        print("NarPrID\t Proizvod\t Kol.\t Dat. Nar.\t Vreme\t Ime K.\t Pr. Kupca\t Mesto")
        print(svi[0],'\t',svi[11],'\t',svi[3],'\t',svi[5],'\t',svi[6],'\t',svi[8],'\t',svi[9],'\t',svi[10])

    def obrisi_narudzbinu(self):
        print("BRISANJE NARUDZBINE")
        self.prikazi_sve_narudzbine()
        id_nar=unos_nar_pr_id()
        sql='delete from NarudzbinaPredmet where NarudzbinaID=?'
        query(sql,id_nar)
        sql2='delete from NarudzbinaKupca where NarudzbinaID=?'
        query(sql2,id_nar)
        print("NARUDZBINA OBRISANA")

    def azuriraj_narudzbinu(self):
        print("AZURIRANJE NARUDZBINE")
        self.prikazi_sve_narudzbine()
        id_nar=unos_nar_pr_id()
        sql='update NarudzbinaKupca set Datum=?,Vreme=?,KupacID=? where NarudzbinaID=?'
        query(sql,unos_narudzbenice_kupca()+id_nar)
        sql2='update NarudzbinaPredmet set ProizvodID=?,Kolicina=? where NarudzbinaPredmetID=?'
        query(sql2,unos_narudzbenice_predmeta()+id_nar)
        print("NARUDZBINA AZURIRANA")

def unos_narudzbenice_kupca():
    while True:
        try:
            datum=input("Unesite datum porudzbine: ")
            vreme=input("Unesite vreme porudzbine: ")
            kontrolor_kupaca.prikazi_sve_kupce()
            kupacid=int(input("Unesite ID kupca: "))
            if provera_id_kupca(kupacid):
                return (datum,vreme,kupacid)
            else:
                print("Pogresan ID. Molimo vas da probate ponovo.")
        except ValueError:
            print("Doslo je do greske pri unosu. Ponovite unos.")

def unos_narudzbenice_predmeta():
    while True:
        try:
            kontrolor_proizvoda.prikazi_sve_proizvode()
            proizvodid=int(input("Unesite ID proizvoda: "))
            kolicina=int(input("Unesite kolicinu: "))
            if provera_id_proizvoda(proizvodid):
                return (proizvodid,kolicina)
            else:
                print("Pogresan ID. Molimo vas da probate ponovo.")
        except ValueError:
            print("Doslo je do greske pri unosu. Ponovite unos.")

def provera_id_kupca(id_kupca):
    with sqlite3.connect(ime_baze) as kon:
        kur=kon.cursor()
        kur.execute("select KupacID from Kupac")
        listaid=[]
        for i in kur.fetchall():
            for j in i:
                listaid.append(j)
        return id_kupca in listaid

def provera_id_proizvoda(id_proizvoda):
    with sqlite3.connect(ime_baze) as kon:
        kur=kon.cursor()
        kur.execute("select ProizvodID from Proizvod")
        listaid=[]
        for i in kur.fetchall():
            for j in i:
                listaid.append(j)
        return id_proizvoda in listaid

def dobijanje_poslednje_naruzdbenice_kupca():
    with sqlite3.connect(ime_baze) as kon:
        kur=kon.cursor()
        kur.execute("select NarudzbinaID from NarudzbinaKupca")
        return kur.fetchall()[-1]

def dobij_sve_narudzbine():
    with sqlite3.connect(ime_baze) as kon:
        kur=kon.cursor()
        kur.execute("select * from NarudzbinaPredmet")
        narpred=kur.fetchall()
        kur.execute("select * from NarudzbinaKupca")
        narkup=kur.fetchall()
        return zip(narpred,narkup)

def provera_narudzbine_id(id_nar):
    with sqlite3.connect(ime_baze) as kon:
        kur=kon.cursor()
        kur.execute('select NarudzbinaPredmetID from NarudzbinaPredmet')
        return (id_nar,)in kur.fetchall()

def unos_nar_pr_id():
    while True:
        try:
            id_nar=int(input("Unesite ID narudzbine predmeta: "))
            if provera_narudzbine_id(id_nar):
                return (id_nar,)
            else:
                print("ID koji ste uneli ne postoji! Probajte ponovo.")
        except ValueError:
            print("Doslo je do greske pri unosu.")
    
kontrolor_narudzbine=Order()

if __name__=="__main__":
    #kontrolor_narudzbine.dodaj_naruzdbinu()
    kontrolor_narudzbine.prikazi_sve_narudzbine()
    kontrolor_narudzbine.prikazi_detalje_narudzbine()
    #kontrolor_narudzbine.obrisi_narudzbinu()
    #kontrolor_narudzbine.azuriraj_narudzbinu()

