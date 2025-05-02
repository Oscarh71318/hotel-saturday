import dominio.modelo.usuarios
from aplications.guest_service import GuestService
from repositorio.conexion.Conexion import Conexion


class MenuApp:
    def __init__(self):
        self.bd = Conexion(host='localhost', port=3306, user='root', password='', database='hotel_saturday')
        self.guest_service = GuestService()

    def init_app(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Registrar huésped")
            print("2. Mostrar huéspedes")
            print("3. Salir")
            choice = input("Seleccione una opción: ")

            if choice == "1":
                self.register_guest()
            elif choice == "2":
                self.show_guests()
            elif choice == "3":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo")

    def register_guest(self):
        print("\n--- Registro de Huésped ---")
        try:
            id = input("ID: ")
            name = input("Nombre: ")
            last_name = input("Apellido: ")
            phone = input("Teléfono: ")
            mail = input("Correo electrónico: ")
            password = input("Contraseña: ")
            status = input("Estado: ")
            origin = input("Origen: ")
            occupation = input("Ocupación: ")

            guest_data = [id, name, last_name, phone, mail, password, status, origin, occupation]
            guest = self.guest_service.create_guest(guest_data)
            print(f"Huésped {guest.name} {guest.last_name} registrado exitosamente.")
        except Exception as e:
            print(f"Error al registrar huésped: {e}")

    def show_guests(self):
        print("\n--- Lista de Huéspedes ---")
        if not self.guest_service.guests:
            print("No hay huéspedes registrados.")
        else:
            for guest in self.guest_service.guests:
                print(guest)

if __name__ == "__main__":
    menu = MenuApp()
    menu.init_app()
