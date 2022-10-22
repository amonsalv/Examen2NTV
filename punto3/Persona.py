class Banco:
    def _init_(self, nombre, apellido, cedula,ciudad, numCuenta, saldo, retiro=0, ingreso=0):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._ciudad = ciudad
        self._numCuenta = numCuenta
        self._saldo = saldo
        self._retiro = retiro
        self._ingreso = ingreso
        
    def nombre(self, nombre):
        self._nombre = nombre

    def apellido(self, apellido):
        self._apellido = apellido

    def cedula(self, cedula):
        self._cedula = cedula

    def ciudad(self, ciudad):
        self._ciudad = ciudad

    def numCuenta(self, numCuenta):
        self._numCuenta = numCuenta

    def saldo(self, saldo):
        self._saldo = saldo

    def retiro(self, retiro):
        self._retiro = retiro

    def ingreso(self, ingreso):
        self._ingreso = ingreso

