
#3 clases, primera: usuario y contraseña y un metodo que imprima los atributos del usuario y contraseña
#segundo: rol usuario, atributo de nombre de rol y metodo que diga imprima numero del rol
#ultima: herede de maner multiple: datos usuario y esta hereda las dos clases anteriores y que imprima un saludo
#crear un objeto donde instancia el rol de usuario, el nombre de usuario, contraseña y que imprima
#los metodos de las otras clases

#settear metodo logic: pedri al usuario nombre: contraseña y validar si esa contraseña es correcta 
#(acceder de la clase 3)

#crear un diccionario, tener los {valor}: nombre, apellidos, sexo, edad, estatura
#crear un atributo donde el obejto tenga la estructura inicial pero vacia y crear un metodo en la clase datosusuario
#donde permita crear una lista de obejtos apartir del numero de usuario que desee agregar el usuario y
#usar un get para devolver el diccionario completo

class Datos_usuario:
    def __init__(self,usuario,contraseña,apellido,edad,sexo,altura):
        self.usuario = usuario
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
        self.altura = altura
        self.contraseña = contraseña


class Rol_Usuario:
    def __init__(self,rol):
        self.rol = rol
    
    def NumeroRol(self):
        self.rol = print("rol numero: ",{self.rol})

class Persona(Datos_usuario,Rol_Usuario):
    def saludo(self):
        print(f"Hola {self.usuario}! (contraseña ingresada: {self.contraseña})")

    def logic(self):
        if self.contraseña == "5564":
            print(True)
        else:
            print(False)

class dict(Datos_usuario):

    def diccionario(self):
        self.diccionario = {
            'nombre: ': self.usuario,
            'apellidos': self.apellido,
            'edad: ': self.edad,
            'sexo: ': self.sexo,
            'altura: ': self.altura
        }

        veces = int(input("total de veces a repetir: "))

        for i in self.diccionario(veces):
            self.diccionario.append()


nombre = Persona("juan","5564","lopez",20,"hombre",1.85)
nombre.saludo()
nombre.logic()

roles = Rol_Usuario(5)
roles.NumeroRol()

dicc = dict("juan","5564","lopez",20,"hombre",1.85)
dicc.diccionario()










