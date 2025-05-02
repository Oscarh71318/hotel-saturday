
from dominio.modelo.Guest import Guest
from repositorio.conexion import Conexion

class GuestRepositorio:
    def __init__(self, conexion: Conexion):
        self.conexion = conexion

    def create_guest_repositorio(self, guest: Guest) -> None:
        query = """
            INSERT INTO guest (id, name, last_name, phone, mail, password, status, origin, occupation)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            guest.id,
            guest.name,
            guest.last_name,
            guest.phone,
            guest.mail,
            guest.password,
            guest.status,
            guest.origin,
            guest.occupation
        )
        self.conexion.execute_query(query, values)
