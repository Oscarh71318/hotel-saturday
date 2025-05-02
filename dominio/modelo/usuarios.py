class User:
    def __init__(self, id, name, last_name, phone, mail, password, status):
        self._id = id
        self._name = name
        self._last_name = last_name
        self._phone = phone
        self._mail = mail
        self._password = password
        self._status = status

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def mail(self):
        return self._mail

    @mail.setter
    def mail(self, mail):
        self._mail = mail

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status
