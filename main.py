import json
import pandas as pd
from bngen import redBayesiana as rb

# Relaciones
edges = [("Dificultad","Calificacion"),
         ("Inteligencia","Calificacion"), 
         ("Inteligencia","SAT"),
         ("Calificacion","Referencias")]

# Creación de red bayesiana
network = rb(edges)

# CPD
network.cdp('Dificultad', 2, [[0.6], [0.4]])
network.cdp('Inteligencia', 2, [[0.7], [0.3]])
network.cdp('SAT', 2, [[0.95, 0.2],
                       [0.05, 0.8]],
                       ['Inteligencia'],
                       [2]
                       )
network.cdp('Referencias', 2,
                   [[0.1, 0.4, 0.99],
                    [0.9, 0.6, 0.01]],
                    ['Calificacion'],
                    [3])
network.cdp('Calificacion', 3,
                [[0.3, 0.05, 0.9,  0.5],
                [0.4, 0.25, 0.08, 0.3],
                [0.3, 0.7,  0.02, 0.2]],
                ['Inteligencia', 'Dificultad'],
                [2, 2])

print("La red Bayesiana está definida correctamente?: ", network.correcta())
print("La red Bayesiana está completamente descrita?: ", network.completamenteDescrita())
print("Representación compacta de la red bayesiana: ", network.compact())
print("Representación de la red bayesiana como diccionario: \n", pd.DataFrame(network.diccionario()))

