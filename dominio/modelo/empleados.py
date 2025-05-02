from dominio.modelo.usuarios import User

class Empleado(User):
    def __init__(self, id, name, last_name, phone, mail, password, status, rol):
        super().__init__(id, name, last_name, phone, mail, password, status)
        self._rol = rol

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, rol):
        self._rol = rol

    def __str__(self):
        return (f"Empleado: {self.name} {self.last_name}"
                f", Rol: {self.rol}, Estado: {self.status}")
