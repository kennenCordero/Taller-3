import sqlite3 as dba_object 
from sqlite3 import Error

def conecction_database():
    try:
        conexion = dba_object.connect("DB_ICE.db")
        print ("correcto")
        return conexion
    except Error as err:
        print(err)



def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE operador(identificador INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT")
        print ("correcto")
        connection.commit()
    except Error:
        print(Error, "Debio ser en el query!")


def insertar_Operador(connection, valores):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO operador(nombre) VALUES(?)", valores)
        connection.commit()
    except Error:
        print(Error, "Debieron ser valores erroneos!")


objeto_conexion = conecction_database()
create_table(objeto_conexion)
insertar_Operador(objeto_conexion,"pablo")




