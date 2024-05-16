import sqlite3

base1 = sqlite3.connect('dino2')

punts = base1.cursor()

def crear_taula():
    punts.execute("""create table punts (
                    id integer primary key autoincrement,
                    nom text,
                    puntuacio integer
    )""")
nom = "biel"
#crear_taula()
punts.execute("select * from punts")
#punts.execute("delete from punts")
print(punts.fetchall())

