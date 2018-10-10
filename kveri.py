import sqlite3
from ime_baze import ime_baze

def query(sql,sadrzaj):
    with sqlite3.connect(ime_baze) as kon:
        kur=kon.cursor()
        kur.execute("PRAGMA foreign_keys = ON")
        kur.execute(sql,sadrzaj)
        kon.commit()

def queryselectone(sql,sadrzaj):
    with sqlite3.connect(ime_baze) as kon:
        kur=kon.cursor()
        kur.execute("PRAGMA foreign_keys = ON")
        kur.execute(sql,sadrzaj)
        return kur.fetchone()

def queryselectall(sql):
    with sqlite3.connect(ime_baze) as kon:
        kur=kon.cursor()
        kur.execute("PRAGMA foreign_keys = ON")
        kur.execute(sql)
        return kur.fetchall()

def query_shopa(sql_naredba):
    with sqlite3.connect(ime_baze) as kon:
        kur=kon.cursor()
        kur.execute(sql_naredba)
        lista=sql_naredba.split()
        if lista[0].lower()=='select':
            print(kur.fetchall())
        kon.commit()

def dobij_sql():
    return input(f"Unesite SQL naredbu koju zelite da uradite nad bazom {ime_baze}:\n")
