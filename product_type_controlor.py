import sqlite3
from kveri import query,queryselectall,queryselectone
from ime_baze import ime_baze

class ProductTypeControlor:
    def dodaj_tip(self):
        sql="insert into ProizvodTip(Opis) values (?)"
        print("UNOS TIPA PROIZVODA")
        sadrzaj=unos_proizvod_tipa()
        query(sql,(sadrzaj,))
        print("Proizvod Tip dodat!")

    def prikazi_sve_proizvod_tipove(self):
            sql="select * from ProizvodTip"
            print("LISTA SVIH TIPOVA PROIZVODA")
            print("ID\t Opis\t")
            for tip in queryselectall(sql):
                print(tip[0],"\t",tip[1],"\t")

    def azuriraj_tip(self):
        self.prikazi_sve_proizvod_tipove()
        print("AZURIRANJE TIPA PROIZVODA")
        idtipa=dobij_proizvod_tipa_id()
        sql="update ProizvodTip set Opis=? where ProizvodTipID=?"
        sadrzaj=(unos_proizvod_tipa(),idtipa)
        query(sql,sadrzaj)
        print("Proizvod Tip azuriran!")

    def obrisi_tip(self):
        self.prikazi_sve_proizvod_tipove()
        print("BRISANJE TIPA PROIZVODA")
        idtipa=dobij_proizvod_tipa_id()
        sql="delete from ProizvodTip where ProizvodTipID=?"
        sadrzaj=(idtipa,)
        query(sql,sadrzaj)
        print("Proizvod Tip obrisan!")
    
#FUNKCIJE KONTROLORA PROIZVODTIP
def unos_proizvod_tipa():
    while True:
        try:
            ime=input("Unesite ime tipa proizvoda: ")
            return ime
        except ValueError:
            print("Doslo je do greske pri unosu. Ponovite unos.")  

def dobij_proizvod_tipa_id():
    with sqlite3.connect(ime_baze) as kon:
        kur=kon.cursor()
        kur.execute("select ProizvodTipID from ProizvodTip")
        prtipid=kur.fetchall()
        listaid=[]
        for i in prtipid:
            for j in i:
                listaid.append(j)
        while True:
            try:
                id_prtipa=int(input("Unesite ID proizvoda tipa: "))
                if id_prtipa in listaid:
                    return id_prtipa
                else:
                    print("ID proizvoda tipa koji ste uneli ne postoji. Molimo vas da probate ponovo.")
            except:
                print("Doslo je do greske, probajte ponovo!")

kontrolor_proizvoda_tipa=ProductTypeControlor()

if __name__=="__main__":
    #kontrolor_proizvoda_tipa.dodaj_tip()
    kontrolor_proizvoda_tipa.prikazi_sve_proizvod_tipove()
    #kontrolor_proizvoda_tipa.azuriraj_tip()
    #kontrolor_proizvoda_tipa.obrisi_tip()

