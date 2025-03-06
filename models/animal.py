from models.ianimal import IAnimal

class Animal(IAnimal):
    def __init__(self, nombre: str, peso: float, edad: int) -> None:
        self._nombre = nombre
        self._peso = peso
        self._edad = edad
        self._kilos_comidos = 0

    def cambiar_kilos_comidos(self, kilos_comidos:int) -> None:
        self._kilos_comidos = kilos_comidos

    def cambiar_nombre(self, nombre: str) -> None:
        self._nombre = nombre
    
    def cambiar_peso(self, peso:float) -> None:
        self._peso = peso
    
    def cambiar_edad(self, edad: int) -> None:
        self._edad = edad
    
    def obtener_kilos_comidos(self) -> int:
        return self._kilos_comidos
    
    def obtener_nombre(self) -> str:
        return self._nombre
    
    def obtener_peso(self) -> float:
        return self._peso
    
    def obtener_edad(self) -> int:
        return self._edad
    
    def comer(self, kilos:int) -> None:
        self._kilos_comidos+=kilos

    @staticmethod
    def hacer_sonido():
        pass