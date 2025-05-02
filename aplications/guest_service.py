import re
from dominio.modelo.Guest import Guest
from repositorio.conexion.Conexion import Conexion


class GuestService:
    def __init__(self):
        self.guests = []
        self.db = Conexion(
            host='localhost',
            port=3306,
            user='root',
            password='',
            database='hotel_saturday'
        )

    def validate_guest_data(self, data):
        if len(data) < 9:
            raise ValueError("Se requieren 9 campos para crear un huésped.")

        id, name, last_name, phone, mail, password, status, origin, occupation = data

        # Validar campos no vacíos
        if not all(data):
            raise ValueError("Todos los campos deben estar completos.")

        # Validar email
        if not re.match(r"[^@]+@[^@]+\.[^@]+", mail):
            raise ValueError("Correo electrónico no válido.")

        # Validar teléfono numérico
        if not phone.isdigit() or len(phone) < 7:
            raise ValueError("Teléfono inválido. Debe contener al menos 7 dígitos numéricos.")

        # Validar contraseña
        if len(password) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres.")

    def create_guest(self, register_data):
        self.validate_guest_data(register_data)

        guest = Guest(
            id=register_data[0],
            name=register_data[1],
            last_name=register_data[2],
            phone=register_data[3],
            mail=register_data[4],
            password=register_data[5],
            status=register_data[6],
            origin=register_data[7],
            occupation=register_data[8]
        )
        self.guests.append(guest)

        self.db.connect()
        try:
            query_user = """
                INSERT INTO usuarios (id, name, last_name, phone, mail, password, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            user_data = (
                guest.id, guest.name, guest.last_name,
                guest.phone, guest.mail, guest.password,
                guest.status
            )
            self.db.execute_query(query_user, user_data)

            query_guest = """
                INSERT INTO huespedes (id, origin, occupation)
                VALUES (%s, %s, %s)
            """
            guest_data = (guest.id, guest.origin, guest.occupation)
            self.db.execute_query(query_guest, guest_data)

        except Exception as e:
            raise Exception(f"Error al guardar en la base de datos: {e}")
        finally:
            self.db.disconnect()

        return guest
