class Servidor:
    def __init__(self, nombre, cpu, ram):
        self.nombre = nombre
        self.cpu = cpu
        self.set_ram(ram)

    def set_ram(self, ram):
        if ram <= 0:
            raise ValueError("La cantidad de RAM no puede ser 0 o negativa.")
        self.__ram = ram

    def get_ram(self):
        return self.__ram
             
    def mostrar(self):
        return f"{self.nombre} - {self.cpu} CPUs - {self.get_ram()} GB"

servidor1 = Servidor("web01", 4, 16)
print(servidor1.mostrar())
servidor1.set_ram(32)
print(servidor1.get_ram())
servidor1.set_ram(-20) #un error contolado con salida definida
print(servidor1.get_ram())
    
#servidor1 = Servidor("web01", 4, 16)
#servidor2 = Servidor("sql01", 8, 32)
#servidor3 = Servidor("app01", 16, -8)

#print(servidor1.mostrar())
#print(servidor2.mostrar())
#print(servidor3.mostrar())
#print(servidor3.get_ram())


