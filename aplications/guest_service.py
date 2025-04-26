from dominio.modelo.Guest import Guest



class GuestService:
    def __init__(self):
        self.guests = []

    def create_guest(self, register_data):
        if len(register_data) < 8:
            raise ValueError("Se requieren al menos 8 campos para crear un huésped.")

        guest = Guest(
            id=register_data[0],
            name=register_data[1],
            last_name=register_data[2],
            phone=register_data[3],
            mail=register_data[4],
            password=register_data[5],
            status=register_data[6],
            origin=register_data[7],
            occupation=register_data[8] if len(register_data) > 8 else None
        )
        self.guests.append(guest)
        return guest

    def print_guests(self):
        for guest in self.guests:
            print(guest)

