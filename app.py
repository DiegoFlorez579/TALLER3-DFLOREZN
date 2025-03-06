
from models.boa_constrictor import Boa_Constrictor
from models.huron import Huron
from models.guarderia import Guarderia

#Implementación de 2 ejemplos de boa:
boa1 = Boa_Constrictor(nombre="Nagini", peso=15.3, edad=5, pais_origen="Brasil", impuestos=200.0)
boa2 = Boa_Constrictor(nombre="Kaa", peso=12.5, edad=3, pais_origen="India", impuestos=180.0)


#Implementación de 2 ejemplos de huron:
huron1 = Huron(nombre="Fidget", peso=1.2, edad=2, pais_origen="Estados Unidos", impuestos=50.0)
huron2 = Huron(nombre="Bandit", peso=1.5, edad=4, pais_origen="Canadá", impuestos=55.0)

#Implementación de la clase guarderia:
guarderia1 = Guarderia([huron1, huron2], [boa1, boa2])

#Alimenta la boa1
valor_nulo = None
valor_incorrecto = 'Prueba'
print(f'-'*60)
print(f"{' '*24} PRUEBAS {' '*24}")
print(f'-'*60)
print(f' La boa {boa1.obtener_nombre()} recibe los ratones con: {guarderia1.alimentar_boa(boa1, 2)}')
print(f' * Ratones comidos por {boa1.obtener_nombre()} = {boa1.obtener_ratones_comidos()}')
print(f' La boa {boa2.obtener_nombre()} recibe los ratones con: {guarderia1.alimentar_boa(boa2, 7)}')
print(f' * Ratones comidos por {boa2.obtener_nombre()} = {boa2.obtener_ratones_comidos()}')
print(f' Lo siento {boa1.obtener_nombre()} {guarderia1.alimentar_boa(boa1, 10)} y no puede comer más')
print(f' * Ratones comidos por {boa1.obtener_nombre()} = {boa1.obtener_ratones_comidos()}')
print(f'-'*60)
print(f"{' '*20} Valores incorrectos {' '*20}")
print(f'-'*60)
print(f' Con un valor nulo: {guarderia1.alimentar_boa(valor_nulo, 10)}')
print(f' Con una Boa sin inicializar: {guarderia1.alimentar_boa(valor_incorrecto, 10)}')
print(f'-'*60)