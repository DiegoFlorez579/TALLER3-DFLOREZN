from models.animal import Animal

class Animal_Exotico(Animal):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, peso, edad)
        self._pais_origen = pais_origen
        self._impuestos = impuestos
    
    def cambiar_pais_origen(self, pais_origen: str) -> None:
        self._pais_origen = pais_origen
    
    def cambiar_impuestos(self, impuestos: float) -> None:
        self._impuestos = impuestos

    def obtener_pais_origen(self) -> str:
        return self._pais_origen
    
    def obtener_impuestos(self) -> float:
        return self._impuestos

    def calcular_flete(self) -> float:
        return (self._impuestos * self._peso)