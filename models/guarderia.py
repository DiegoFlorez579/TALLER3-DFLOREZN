#Define la clase guarderia solicitada en el taller 3 modulo 2:
class Guarderia():
    def __init__(self, hurones: list, boas: list) -> None:
        self._hurones = hurones
        self._boas = boas

    def consultar_hurones(self) -> list:
        return(self._hurones)

    def consultar_boas(self) -> list:
        return(self._boas)
    
    def alimentar_boa(self, boa, numero_ratones):
        try:
            boa.comer_raton(numero_ratones)
            return('Éxito')
        except ValueError:
            return('La boa está llena')
        except NameError:
            return('Esta Boa no existe!')
        except AttributeError:
            return('Esta Boa no existe!')