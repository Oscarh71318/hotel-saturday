
from aplications.guest_service import GuestService

class GuestInput:
    """
    Interfaz de línea de comandos para registrar y mostrar huéspedes.
    """
    def __init__(self):
        # Inicializa el servicio de huésped
        self.guest_service = GuestService()

    def register(self) -> None:
        """
        Solicita datos por consola y registra un nuevo huésped.
        """
        data = []
        try:
            user_id = int(input("Ingrese su documento de identidad: "))
        except ValueError:
            print("El ID debe ser un número entero.")
            return
        data.append(user_id)

        data.append(input("Ingrese su nombre: "))
        data.append(input("Ingrese su apellido: "))
        data.append(input("Ingrese su teléfono: "))
        data.append(input("Ingrese su email: "))
        data.append(input("Ingrese su contraseña: "))
        data.append(input("Seleccione el estado: "))
        data.append(input("Ingrese su origen: "))
        data.append(input("Ingrese su ocupación: "))

        try:
            guest = self.guest_service.create_guest(data)
            print(f"Huésped {guest.name} {guest.last_name} registrado exitosamente.")
        except Exception as e:
            print(f"Error al registrar huésped: {e}")

    def print_data(self) -> None:
        """
        Muestra todos los huéspedes registrados.
        """
        self.guest_service.print_guests()
