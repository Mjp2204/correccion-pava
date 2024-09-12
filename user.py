from usuario import *

class IniciarSesion:
    def __init__(self, guardar_datos):
        self.guardar_datos = guardar_datos

    def solicitar_credenciales(self):
        nombre = input("Ingrese su nombre de usuario: ").strip()
        contraseña = input("Ingrese su contraseña: ").strip()
        return nombre, contraseña

    def validar_credenciales(self, nombre, contraseña):
        self.guardar_datos.cargar_datos()
        return self.guardar_datos.nombre == nombre and self.guardar_datos.contraseña == contraseña

    def iniciar(self):
        nombre, contraseña = self.solicitar_credenciales()
        if self.validar_credenciales(nombre, contraseña):
            print("Inicio de sesión exitoso.")
        else:
            print("Nombre de usuario o contraseña incorrectos.")
