class Servidor:
    def __init__(self, nombre, cpu, ram):
        self.nombre = nombre
        self.cpu = cpu
        self.ram = ram

    def mostrar(self):
        return f"{self.nombre} - {self.cpu} CPUs - {self.ram} GB"
    
servidor1 = Servidor("web01", 4, 16)
servidor2 = Servidor("sql01", 8, 32)

print(servidor1.mostrar())
print(servidor2.mostrar())