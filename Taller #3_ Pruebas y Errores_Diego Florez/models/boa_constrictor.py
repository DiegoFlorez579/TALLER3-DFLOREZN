from models.animal_exotico import Animal_Exotico

class Boa_Constrictor(Animal_Exotico):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos:float) -> None:
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self._ratones_comidos = 0

    @staticmethod
    def hacer_sonido() -> str:
        return('¡Tsss!')

    def comer_raton(self, ratones_comidos) -> None:
        self._ratones_comidos += ratones_comidos
        if self._ratones_comidos >= 10:
            self._ratones_comidos -= ratones_comidos
            raise ValueError('Demasiados Ratones')

    def obtener_ratones_comidos(self) -> int:
        return self._ratones_comidos