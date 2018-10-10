import sqlite3
from kveri import query,queryselectall,queryselectone
from ime_baze import ime_baze

class CustomerControlor:

    def dodaj_kupca(self):
        sql="insert into Kupac(Ime, Prezime, Ulica, Mesto, PostanskiBroj, Telefon, EMail) values(?,?,?,?,?,?,?)"
        print("UNOS KUPCA")
        query(sql,unos_kupca())
        print("Kupac unet!")

    def prikazi_sve_kupce(self):
        sql="select * from Kupac"
        print("LISTA SVIH KUPACA")
        print("ID\t Ime\t Prezime\t Ulica\t\t Mesto\t\t P. Broj\t Telefon\t EMail")
        for kupac in queryselectall(sql):
            print(kupac[0],"\t",kupac[1],"\t",kupac[2],"\t",kupac[3],"\t",kupac[4],"\t",kupac[5],"\t\t",kupac[6],"\t",kupac[7],"\t")


    def prikazi_detalje_kupca(self):
        print("PRIKAZ DETALJA KUPCA")
        id_kupca=dobij_id_kupca()
        sql="select * from Kupac where KupacID=?"
        print("ID\t Ime\t Prezime\t Ulica\t\t Mesto\t\t P. Broj\t Telefon\t EMail")
        kupac=queryselectone(sql,(id_kupca,))
        print(kupac[0],"\t",kupac[1],"\t",kupac[2],"\t",kupac[3],"\t",kupac[4],"\t",kupac[5],"\t\t",kupac[6],"\t",kupac[7],"\t")

    def obrisi_kupca(self):
        self.prikazi_sve_kupce()
        print("BRISANJE KUPCA")
        id_kupca=(dobij_id_kupca(),)
        sql="delete from Kupac where KupacID=?"
        query(sql,id_kupca)
        print("Kupac obrisan!")
        self.prikazi_sve_kupce()

    def azuriraj_kupca(self):
        self.prikazi_sve_kupce()
        print("AZURIRANJE KUPCA")
        id_kupca=dobij_id_kupca()
        sadrzaj=unos_kupca()
        sadrzaj+=(id_kupca,)
        sql="update Kupac set Ime=?, Prezime=?, Ulica=?, Mesto=?, PostanskiBroj=?, Telefon=?, EMail=? where KupacID=?"
        query(sql,sadrzaj)
        print("Kupac azuriran!")
        self.prikazi_sve_kupce() 


#FUNKCIJE KONTROLORA KUPCA
def unos_kupca():
    while True:
        try:
            ime=input("Unesite ime: ")
            prezime=input("Unesite prezime: ")
            ulica=input("Unesite ulicu: ")
            mesto=input("Unesite mesto: ")
            pbroj=int(input("Unesite postanski broj: "))
            telefon=input("Unesite telefon: ")
            email=input("Unesite email: ")
            return (ime,prezime,ulica,mesto,pbroj,telefon,email)
        except ValueError:
            print("Doslo je do greske pri unosu. Ponovite unos.")

def dobij_id_kupca():
    with sqlite3.connect(ime_baze) as kon:
        kur=kon.cursor()
        kur.execute("select KupacID from Kupac")
        kupacid=kur.fetchall()
        listaid=[]
        for i in kupacid:
            for j in i:
                listaid.append(j)
        while True:
            try:
                id_kupca=int(input("Unesite ID kupca: "))
                if id_kupca in listaid:
                    return id_kupca
                else:
                    print("ID kupca koji ste uneli ne postoji. Molimo vas da probate ponovo.")
            except:
                print("Doslo je do greske, probajte ponovo!")

kontrolor_kupaca=CustomerControlor()

if __name__=="__main__":
    #kontrolor_kupaca.dodaj_kupca()
    #kontrolor_kupaca.obrisi_kupca()
    kontrolor_kupaca.prikazi_detalje_kupca()
    #kontrolor_kupaca.azuriraj_kupca()
    kontrolor_kupaca.prikazi_sve_kupce()