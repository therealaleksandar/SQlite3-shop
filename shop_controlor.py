import sqlite3
from ime_baze import ime_baze

class ShopControlor:

    def kreiraj_bazu(self,ime_baze,ime_tabele,sql):
        with sqlite3.connect(ime_baze) as kon:
            kur=kon.cursor()
            kur.execute("select name from sqlite_master where name=:imet",{'imet':ime_tabele})
            rezultat=kur.fetchall()
            sacuvaj=True
            if len(rezultat)>=1:
                odgovor=input(f"Tabela {ime_tabele} je prisutna. Da li zelite da je obrisete i napravite novu?: ")
                if odgovor[0].lower()=='d':
                    sacuvaj=False
                    print(f"Tabela {ime_tabele} ce biti obrisana i naravice se nova tabela!")
                    kur.execute("drop table if exists {}".format(ime_tabele))
                    kon.commit()
                else:
                    print("Tabela je sacuvana.")
            else:
                sacuvaj=False
            if not sacuvaj:
                kur.execute(sql)
                kon.commit()

    def kreiraj_proizvod(self):
        tablaProizvod="""create table Proizvod
                        (ProizvodID integer,
                        Ime text,
                        Cena real,
                        ProizvodTipID integer,
                        PRIMARY KEY (ProizvodID),
                        FOREIGN KEY (ProizvodTipID) references ProizvodTip(ProizvodTipID)
                        on update cascade on delete set null)"""
        self.kreiraj_bazu(ime_baze,'Proizvod',tablaProizvod)

    def kreiraj_proizvod_tip(self):
        tablaProizvodTip="""create table ProizvodTip
                            (ProizvodTipID integer,
                            Opis text,
                            PRIMARY KEY (ProizvodTipID))"""
        self.kreiraj_bazu(ime_baze,'ProizvodTip',tablaProizvodTip)

    def kreiraj_kupac(self):
        tablaKupac="""create table Kupac
                    (KupacID integer,
                    Ime text,
                    Prezime text,
                    Ulica text,
                    Mesto text,
                    PostanskiBroj integer,
                    Telefon text,
                    EMail text,
                    PRIMARY KEY (KupacID))"""
        self.kreiraj_bazu(ime_baze,'Kupac',tablaKupac)

    def kreiraj_narudzbina_kupac(self):
        tablaNaruzbinaKupca="""create table NarudzbinaKupca
                                (NarudzbinaID integer,
                                Datum text,
                                Vreme text,
                                KupacID integer,
                                PRIMARY KEY (NarudzbinaID),
                                FOREIGN KEY (KupacID) references Kupac(KupacID)
                                on update cascade on delete set null)"""
        self.kreiraj_bazu(ime_baze,'NarudzbinaKupca',tablaNaruzbinaKupca)

    def kreiraj_narudzbina_predmet(self):
        tablaNarudzbinaPredmet="""create table NarudzbinaPredmet
                                (NarudzbinaPredmetID integer,
                                NarudzbinaID integer,
                                ProizvodID integer,
                                Kolicina integer,
                                PRIMARY KEY (NarudzbinaPredmetID),
                                FOREIGN KEY (NarudzbinaID) references NarudzbinaKupca(NarudzbinaID),
                                FOREIGN KEY (ProizvodID) references Proizvod(ProizvodID)
                                on update cascade on delete set null)"""
        self.kreiraj_bazu(ime_baze,'NarudzbinaPredmet',tablaNarudzbinaPredmet)

    def kreiraj_sve(self):
        self.kreiraj_kupac()
        self.kreiraj_proizvod_tip()
        self.kreiraj_proizvod()
        self.kreiraj_narudzbina_kupac()
        self.kreiraj_narudzbina_predmet()

kontrolor_shopa=ShopControlor()
if __name__=="__main__":
    # kontrolor_shopa.kreiraj_kupac()
    # kontrolor_shopa.kreiraj_narudzbina_kupac()
    # kontrolor_shopa.kreiraj_narudzbina_predmet()
    # kontrolor_shopa.kreiraj_proizvod()
    # kontrolor_shopa.kreiraj_proizvod_tip()
    kontrolor_shopa.kreiraj_sve()
