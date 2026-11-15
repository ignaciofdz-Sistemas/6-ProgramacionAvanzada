#Manejo de clases, atributos y métodos en Python

from abc import ABC, abstractmethod

class Dispositivored(ABC):
    @abstractmethod
    def hacer_backup(self) -> str:
        pass
    
    def __init__(self, marca: str, ip: str, modelo: str):
        self.marca = marca
        self.ip = ip
        self.modelo = modelo
   
    def resumen(self) -> str:
        return f"Dispositivo {self.marca} - ({self.modelo}) - IP {self.ip}"
    
               
class Switch(Dispositivored):
    def __init__(self, marca: str, ip: str, modelo: str):
        super().__init__(marca=marca, modelo=modelo, ip=ip)
        self.vlan=[]
        
    def añadir_vlan(self, vlan: str) -> None:
            self.vlan.append(vlan)
            
    def hacer_backup(self):
        return ("backup de switch completado")
            
    def resumen(self) -> str:
        return super().resumen() + f" - VLAN {self.vlan}" + f" {self.hacer_backup()}"
        
class Firewall(Dispositivored):
    def __init__(self, marca: str, ip: str, modelo: str):
        super().__init__(marca=marca, modelo=modelo, ip=ip)
        self.politica=[]  
    def añadir_politica(self, politica: str) -> None:
        self.politica.append(politica)
        
    def hacer_backup(self):
            return ("backup de Firewall completado")
        
    def resumen(self) -> str:
        return super().resumen() + f" - POLITICA {self.politica}" + f" {self.hacer_backup()}"
    
#fw = FirewallFortigate("fw-madrid", "10.0.0.1", "FG-100F")


dr1 = Switch("Cisco","10.10.0.2","F480")
dr1.añadir_vlan("150")

dr2 = Firewall("Forti","172.20.10.1","FW-60G")
dr2.añadir_politica("LAN->WAN permitir 443")

for d in [dr1,dr2]:
    print(d.resumen())
    
#generico = Dispositivored("TP-Link", "192.168.1.1", "X1") # no funciona, no podemos llamar a la clase madre directamente.

