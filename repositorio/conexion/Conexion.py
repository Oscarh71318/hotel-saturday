import mysql.connector
from mysql.connector import Error

class Conexion:
    def __init__(self, host: str, port: int, user: str, password: str, database: str):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self) -> None:
        """
        Establece la conexión con la base de datos MySQL.
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexión establecida")
        except Error as err:
            print("Error al conectar a la base de datos:", err)
            self.connection = None

    def disconnect(self) -> None:
        """
        Cierra la conexión con la base de datos si está abierta.
        """
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada")

    def execute_query(self, query: str, params: tuple = None) -> None:
        """
        Ejecuta una consulta SQL que modifica datos (INSERT, UPDATE, DELETE).
        """
        if not self.connection or not self.connection.is_connected():
            self.connect()
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params or ())
            self.connection.commit()
            print("Consulta ejecutada exitosamente")
        except Error as err:
            print("Error al ejecutar la consulta:", err)
        finally:
            cursor.close()

    def fetch_query(self, query: str, params: tuple = None) -> list:
        """
        Ejecuta una consulta SQL de lectura (SELECT) y devuelve los resultados.
        """
        if not self.connection or not self.connection.is_connected():
            self.connect()
        cursor = self.connection.cursor(dictionary=True)
        results = []
        try:
            cursor.execute(query, params or ())
            results = cursor.fetchall()
        except Error as err:
            print("Error al ejecutar la consulta:", err)
        finally:
            cursor.close()
        return results
