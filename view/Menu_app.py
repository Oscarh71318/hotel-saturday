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
            print("3. Buscar huésped por ID")
            print("4. Actualizar huésped")
            print("5. Eliminar huésped")
            print("6. Salir")
            choice = input("Seleccione una opción: ")

            if choice == "1":
                self.register_guest()
            elif choice == "2":
                self.show_guests()
            elif choice == "3":
                self.search_guest_by_id()
            elif choice == "4":
                self.update_guest()
            elif choice == "5":
                self.delete_guest()
            elif choice == "6":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

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

    def search_guest_by_id(self):
        print("\n--- Buscar Huésped ---")
        try:
            id = input("Ingrese el ID del huésped: ")
            guest = self.guest_service.get_guest_by_id(id)
            if guest:
                print("Huésped encontrado:")
                print(guest)
            else:
                print("Huésped no encontrado.")
        except Exception as e:
            print(f"Error al buscar huésped: {e}")

    def update_guest(self):
        print("\n--- Actualizar Huésped ---")
        try:
            id = input("Ingrese el ID del huésped a actualizar: ")
            guest = self.guest_service.get_guest_by_id(id)
            if guest:
                print("Ingrese los nuevos datos (deje en blanco para no cambiar):")
                name = input(f"Nombre ({guest.name}): ") or guest.name
                last_name = input(f"Apellido ({guest.last_name}): ") or guest.last_name
                phone = input(f"Teléfono ({guest.phone}): ") or guest.phone
                mail = input(f"Correo electrónico ({guest.mail}): ") or guest.mail
                password = input(f"Contraseña ({guest.password}): ") or guest.password
                status = input(f"Estado ({guest.status}): ") or guest.status
                origin = input(f"Origen ({guest.origin}): ") or guest.origin
                occupation = input(f"Ocupación ({guest.occupation}): ") or guest.occupation

                # Cambia la lista a un diccionario
                updated_data = {
                    'name': name,
                    'last_name': last_name,
                    'phone': phone,
                    'mail': mail,
                    'password': password,
                    'status': status,
                    'origin': origin,
                    'occupation': occupation
                }

                updated_guest = self.guest_service.update_guest(id, updated_data)
                if updated_guest:
                    print(f"Huésped {updated_guest.name} {updated_guest.last_name} actualizado correctamente.")
            else:
                print("Huésped no encontrado.")
        except Exception as e:
            print(f"Error al actualizar huésped: {e}")

    def delete_guest(self):
        print("\n--- Eliminar Huésped ---")
        try:
            id = input("Ingrese el ID del huésped a eliminar: ")
            if self.guest_service.delete_guest(id):
                print(f"Huésped con ID {id} eliminado correctamente.")
            else:
                print("Huésped no encontrado.")
        except Exception as e:
            print(f"Error al eliminar huésped: {e}")

if __name__ == "__main__":
    menu = MenuApp()
    menu.init_app()
