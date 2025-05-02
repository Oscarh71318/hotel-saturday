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

    def get_guest_by_id(self, guest_id):
        self.conexion.connect()
        query = "SELECT * FROM usuarios WHERE id = %s"
        result = self.conexion.fetch_query(query, (guest_id,))
        if result:
            guest_data = result[0]
            query_guest = "SELECT * FROM huespedes WHERE id = %s"
            result_guest = self.conexion.fetch_query(query_guest, (guest_id,))
            if result_guest:
                guest_info = result_guest[0]
                return Guest(
                    id=guest_data['id'],
                    name=guest_data['name'],
                    last_name=guest_data['last_name'],
                    phone=guest_data['phone'],
                    mail=guest_data['mail'],
                    password=guest_data['password'],
                    status=guest_data['status'],
                    origin=guest_info['origin'],
                    occupation=guest_info['occupation']
                )
        return None

    def update_guest_repositorio(self, guest: Guest):
        self.conexion.connect()
        try:
            query_user = """
                UPDATE usuarios
                SET name = %s, last_name = %s, phone = %s, mail = %s, password = %s, status = %s
                WHERE id = %s
            """
            user_data = (
                guest.name,
                guest.last_name,
                guest.phone,
                guest.mail,
                guest.password,
                guest.status,
                guest.id
            )
            self.conexion.execute_query(query_user, user_data)

            query_guest = """
                UPDATE huespedes
                SET origin = %s, occupation = %s
                WHERE id = %s
            """
            guest_data = (
                guest.origin,
                guest.occupation,
                guest.id
            )
            self.conexion.execute_query(query_guest, guest_data)
        except Exception as e:
            print("Error al actualizar huésped:", e)
        finally:
            self.conexion.disconnect()

    def delete_guest_repositorio(self, guest_id):
        self.conexion.connect()
        try:
            query_user = "DELETE FROM usuarios WHERE id = %s"
            self.conexion.execute_query(query_user, (guest_id,))

            query_guest = "DELETE FROM huespedes WHERE id = %s"
            self.conexion.execute_query(query_guest, (guest_id,))
        except Exception as e:
            print("Error al eliminar huésped:", e)
        finally:
            self.conexion.disconnect()

