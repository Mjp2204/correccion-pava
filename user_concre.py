from usuario import Usuario

class ConcretoUsuario(Usuario):
    def __init__(self, nombre, contraseña, recordarme):
        super().__init__(nombre, contraseña, recordarme)

    def bienvenida_usuario(self):
        pass

    def iniciar_sesion(self):
        pass