from dominio.modelo.Guest import Guest
from repositorio.conexion import Conexion

class GuestRepositorio:
    def __init__(self, conexion: Conexion):
        self.conexion = conexion

    def create_guest_repositorio(self, guest: Guest) -> None:
        self.conexion.connect()
        try:
            query_user = """
                INSERT INTO usuarios (id, name, last_name, phone, mail, password, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            user_data = (
                guest.id,
                guest.name,
                guest.last_name,
                guest.phone,
                guest.mail,
                guest.password,
                guest.status
            )
            self.conexion.execute_query(query_user, user_data)

            query_guest = """
                INSERT INTO huespedes (id, origin, occupation)
                VALUES (%s, %s, %s)
            """
            guest_data = (
                guest.id,
                guest.origin,
                guest.occupation
            )
            self.conexion.execute_query(query_guest, guest_data)
        except Exception as e:
            print("Error al guardar huésped:", e)
        finally:
            self.conexion.disconnect()
