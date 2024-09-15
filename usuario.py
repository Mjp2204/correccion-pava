from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre, contraseña, recordarme):
        self.nombre = nombre
        self.contraseña = contraseña
        self.recordarme = recordarme

    @abstractmethod
    def bienvenida_usuario(self):
        pass

    @abstractmethod
    def iniciar_sesion(self):
        pass