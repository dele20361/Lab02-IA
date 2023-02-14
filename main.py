
import pandas as pd
import Lab02_IA as rb

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

opc = 0
while opc != "6":
    print("\n                L A B O R A T O R I O  2")
    print("""
        Opciones:
        1. Verificación de Red Bayesiana.
        2. Verificación de red bayesiana completamente descrita.
        3. Representación compacta de Red Bayesiana.
        4. Diccionario de Red Bayesiana.
        5. Inferencia.
        6. Salir
    """)
    opc = input(" >> Ingrese el número de opción: ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    match opc:
        case "1":
            print("- La red Bayesiana está definida correctamente?: ", network.correcta())
        case "2":
            print("- La red Bayesiana está completamente descrita?: ", network.completamenteDescrita())
        case "3":
            print("- Representación compacta de la red bayesiana: ", network.compact())
        case "4":
            print("- Representación de la red bayesiana como diccionario: \n", pd.DataFrame(network.diccionario()))
        case "5":
            print("- P(Calificacion|Inteligencia=0, Dificultad=1): \n", network.inferencia(["Calificacion"], {"Dificultad": 1, "Inteligencia": 0}))
        case "6":
            print("Saliendo...")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")