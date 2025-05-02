import re
from dominio.modelo.Guest import Guest
from repositorio.conexion.Conexion import Conexion
from repositorio.persisten.guestRepositorio import GuestRepositorio

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
        self.repo = GuestRepositorio(self.db)

    def validate_guest_data(self, data):
        if len(data) < 9:
            raise ValueError("Se requieren 9 campos para crear un huésped.")

        id, name, last_name, phone, mail, password, status, origin, occupation = data

        if not all(data):
            raise ValueError("Todos los campos deben estar completos.")

        if not re.match(r"[^@]+@[^@]+\.[^@]+", mail):
            raise ValueError("Correo electrónico no válido.")

        if not phone.isdigit() or len(phone) < 7:
            raise ValueError("Teléfono inválido. Debe contener al menos 7 dígitos numéricos.")

        if len(password) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres.")

    def create_guest(self, register_data):
        try:
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

            # Guardamos el huésped en la base de datos
            self.repo.create_guest_repositorio(guest)
            return guest
        except ValueError as e:
            print(f"Error al crear huésped: {e}")
        except Exception as e:
            print(f"Error inesperado al crear huésped: {e}")
        return None

    def get_guests(self):
        try:
            # Recuperamos todos los huéspedes de la base de datos
            guests_data = self.repo.get_all_guests()
            if not guests_data:
                print("No se encontraron huéspedes.")
            return guests_data
        except Exception as e:
            print(f"Error al obtener huéspedes: {e}")
        return []

    def update_guest(self, guest_id, updated_data):
        try:
            # Obtenemos el huésped por ID
            guest = self.repo.get_guest_by_id(guest_id)
            if not guest:
                print("Huésped no encontrado.")
                return None

            # Actualizamos los campos del huésped
            guest.name = updated_data.get('name', guest.name)
            guest.last_name = updated_data.get('last_name', guest.last_name)
            guest.phone = updated_data.get('phone', guest.phone)
            guest.mail = updated_data.get('mail', guest.mail)
            guest.password = updated_data.get('password', guest.password)
            guest.status = updated_data.get('status', guest.status)
            guest.origin = updated_data.get('origin', guest.origin)
            guest.occupation = updated_data.get('occupation', guest.occupation)

            # Guardamos los cambios en la base de datos
            self.repo.update_guest(guest)
            return guest
        except Exception as e:
            print(f"Error al actualizar huésped: {e}")
        return None

    def delete_guest(self, guest_id):
        try:
            # Obtenemos el huésped por ID
            guest = self.repo.get_guest_by_id(guest_id)
            if not guest:
                print("Huésped no encontrado.")
                return None

            # Eliminamos el huésped de la base de datos
            self.repo.delete_guest(guest)
            self.guests.remove(guest)  # También lo eliminamos de la lista local
            return guest
        except Exception as e:
            print(f"Error al eliminar huésped: {e}")
        return None

    def print_guests(self):
        if not self.guests:
            print("No hay huéspedes registrados.")
        for guest in self.guests:
            print(guest)
