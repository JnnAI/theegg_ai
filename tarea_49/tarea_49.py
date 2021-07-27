class Persona:                                              #Defino la clase persona        
    def __init__(self):                                     #Creo un constructor para la clase donde los parametros puedan estar vacios
        self._nombre = None
        self._edad = None
        self._dni = None

    def mostrar(self):                                      #Metodo para mostrar los datos de la persona. Imprime en pantalla Nombre, Edad y DNI.
        print("Nombre:", self._nombre)
        print("Edad:", self._edad)
        print("DNI:", self._dni)

    def esMayorDeEdad(self):                                #Comprueba mediante una condicion si el input ingresado en edad es mayor de edad.
        esMayor = self._edad >= 18
        return esMayor

    # getter for nombre
    @property
    def nombre(self):                                       #Creo un getter que devuelve el nombre
        return self._nombre

    # setter for nombre
    @nombre.setter                                          #Creo un setter que comprueba que el nombre introducido es correcto tanto en largura (no puede ser menor a 0), como en tipo de variable (comprueba que es de tipo str)
    def nombre(self, nombre):
        esString = isinstance(nombre, str)
        if (esString):
            larguraValida = len(nombre) > 0
            if (larguraValida):
                self._nombre = nombre
            else: 
                raise ValueError('El nombre debe tener al menos un caracter')
        else:
            raise ValueError('El nombre debe ser una cadena de texto')

    # getter for age                                        #Creo un getter que devuelve la edad
    @property
    def age(self):
        return self._edad

    # setter for age
    @age.setter                                             #Creo un setter que comprueba que la edad es correcta en tipo de variable (int)
    def age(self, age):
        isNumber = isinstance(age, int)
        if (isNumber):
            self._edad = age
        else:
            raise ValueError('La edad debe ser un número')

    # getter for dni                                        #Creo un getter que devuelve el DNI
    @property
    def dni(self):
        return self._dni

    @dni.setter                                             #Creo un setter que comprueba largura y tipo de variable del dni
    def dni(self, dni):
        esString = isinstance(dni, str)
        if (esString):
            larguraValida = len(dni) == 9
            if (larguraValida):
                self._dni = dni
            else:
                raise ValueError('El dni debe tener 9 caracteres')
        else:
            raise ValueError('El dni debe ser una cadena de texto')


class Cuenta:                                               #Creo una clase llamada Cuenta que inicia con el nombre del titular en blanco y la cantidad a 0 (para que no haya errores)
    def __init__(self, titular):
        self._titular = titular
        self._cantidad = 0

    def mostrar(self):                                      #Muestra los datos iniciales de la cuenta
        print("Titular:", self.titular.nombre)
        print("Cantidad:", self.cantidad)

    def ingresar(self, cantidad):                           #Ingresa en la cuenta la cantidad especificada entre parentesis mas adelante
        print("Ingresando", cantidad, "euros")
        self._cantidad = self._cantidad + cantidad
        print("La cantidad tras el ingreso es de", self._cantidad, "euros")

    def retirar(self, cantidad):                            #Retira dinero del mismo modo que el "Metodo ingresar". Comprueba que para retirar haya dinero suficiente
        saldo_en_la_cuenta = self._cantidad - cantidad
        if (saldo_en_la_cuenta < 0):
            print("No se puede retirar", cantidad, "euros, porque se tienen tan solo", self._cantidad, "euros")
            print("Eres demasiado pobre.")
        else:
            print("Retirando", cantidad, "euros")
            self._cantidad = self._cantidad - cantidad
            print("La cantidad tras la retirada es de", self._cantidad, "euros")

    # getter for cantidad
    @property
    def cantidad(self):                                     #Devuelve la cantidad mediante un getter
        return self._cantidad

    # getter for titular
    @property
    def titular(self):                                      #Devuelve el titular mediante un setter
        return self._titular

    # setter for titular
    @titular.setter                                         #Setter que recoge al titular
    def titular(self, titular):
        self._titular = titular



# main program
persona = Persona()                     #A persona le asigno todo lo que tiene la clase Persona() dentro
persona.nombre = "Jonan"                #Añado nombre
persona.age = 27                        #Añado edad
persona.dni = "12345678A"               #Añado DNI
persona.mostrar()                       #Muestro todos los datos insertados en persona.

cuenta = Cuenta(persona)                #Asigno a cuenta la clase Cuenta
cuenta.mostrar()                        #Muestro la situacion inicial de la cuenta
cuenta.retirar(50)                      #Retiro e ingreso dinero mediante los siguientes metodos. El getter devuelve el resultado y su impresion en pantalla.
cuenta.ingresar(100)
cuenta.retirar(50)
cuenta.ingresar(20)
cuenta.retirar(10)
