from dominio.modelo.usuarios import User

class Guest(User):
    def __init__(self, id, name, last_name, phone, mail, password, status, origin, occupation):
        super().__init__(id, name, last_name, phone, mail, password, status)
        self.origin = origin
        self.occupation = occupation

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Nombre: {self.name} {self.last_name}\n"
            f"Teléfono: {self.phone}\n"
            f"Email: {self.mail}\n"
            f"Estado: {self.status}\n"
            f"Origen: {self.origin}\n"
            f"Ocupación: {self.occupation}"
        )
