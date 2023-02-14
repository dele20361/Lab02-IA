from bngen import redBayesiana

# Relaciones
edges = [("Dificultad","Calificacion"),
         ("Inteligencia","Calificacion"), 
         ("Inteligencia","SAT"),
         ("Calificacion","Referencias")]

# Creación de red bayesiana
network = redBayesiana(edges)

# CPD
network.cdp('Dificultad', 2, [[0.6], [0.4]])
network.cdp('Inteligencia', 2, [[0.7], [0.3]])
network.cdp('SAT', 4, [[0.95], [0.05], [0.2], [0.8]])
network.cdp('Referencias', 6, [[0.1], [0.9], [0.4], [0.6], [0.99], [0.01]])
network.cdp('Calificacion', 12, [[0.3], [0.4], [0.3], [0.05], [0.25], [0.7], [0.9], [0.08], [0.02], [0.5], [0.3], [0.2]])

