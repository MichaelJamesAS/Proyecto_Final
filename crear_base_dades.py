import sqlite3

base1 = sqlite3.connect('bases_dades/objectes')

items = base1.cursor()

def crear_taula():
    items.execute("""create table items (
                    id integer primary key autoincrement,
                    item text,
                    quantity integer,
                    price integer
    )""")
crear_taula()

def insertar (item, quantity, price):
    items.execute("insert into items (item, quantity, price) values (?, ?, ?)", (item, quantity, price))

insertar('Sword', 8, 15)
insertar('Chestplate', 8, 30)
insertar('Potion', 8, 25)
insertar('Food', 8, 15)
insertar('Bow', 8, 15)
insertar('Axe', 8, 20)
insertar('Trebuchet', 8, 50)
insertar('Book', 8, 30)
insertar('Wand', 8, 25)
insertar('Ring', 8, 15)
insertar('Boots', 8, 20) 
base1.commit()

items.execute("select * from items")

print(items.fetchall())

base1.commit()
base1.close()
