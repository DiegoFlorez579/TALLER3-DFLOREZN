import unittest
from models.boa_constrictor import Boa_Constrictor
from models.huron import Huron

class Tests_Boa(unittest.TestCase):
    def test_hacer_sonido_boa(self):
        boa_prueba = Boa_Constrictor(nombre="Nagini", peso=15.3, edad=5, pais_origen="Brasil", impuestos=200.0)
        self.assertEqual(boa_prueba.hacer_sonido(), '¡Tsss!')

    def test_calcular_flete_boa(self):
        boa_prueba = Boa_Constrictor(nombre="Nagini", peso=15.3, edad=5, pais_origen="Brasil", impuestos=200.0)
        self.assertEqual(boa_prueba.calcular_flete(), (boa_prueba.obtener_impuestos() * boa_prueba.obtener_peso()))

    def test_comer_raton_boa_correcto(self):
        boa_prueba = Boa_Constrictor(nombre="Nagini", peso=15.3, edad=5, pais_origen="Brasil", impuestos=200.0)
        self.assertIsNone(boa_prueba.comer_raton(5))

    def test_comer_raton_boa_incorrecto(self):
        boa_prueba = Boa_Constrictor(nombre="Nagini", peso=15.3, edad=5, pais_origen="Brasil", impuestos=200.0)
        self.assertRaises(ValueError, boa_prueba.comer_raton, 10)


class Tests_Huron(unittest.TestCase):
    def test_hacer_sonido_huron(self):
        huron_prueba = Huron(nombre="Fidget", peso=1.2, edad=2, pais_origen="Estados Unidos", impuestos=50.0)
        self.assertEqual(huron_prueba.hacer_sonido(), '¡Eek Eek!')

    def test_calcular_flete_huron(self):
        huron_prueba = Huron(nombre="Fidget", peso=1.2, edad=2, pais_origen="Estados Unidos", impuestos=50.0)
        self.assertEqual(huron_prueba.calcular_flete(), (huron_prueba.obtener_impuestos() * huron_prueba.obtener_peso()))