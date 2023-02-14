from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

class redBayesiana:

    def __init__(self, edges):
        """
            Parámetros:
                - Edges: Relaciones de dependencia. (Lista de tuplas).

            Los nodos se definen a partir de las relaciones de dependencia.
        """
        self.model = BayesianNetwork(edges)

    def cdp(self, variable, variable_card, values):
        """
            Función para agregar las distribuciones de probabilidad condicional de las variables.
            Parámetros:
                - variable: La variable cuyo CPD está definido. (int/string)
                - variable_card: Números de estados o cardinalidad. (int)
                - values: Probabilidad asignada.
        """
        cpd = TabularCPD(variable=variable, variable_card=variable_card, values=values)
        return self.model.add_cpds(cpd)

    def __str__(self):
        """
            Función para mostrar las distribuciones de probabilidad condicional de una forma más intuitiva.
        """
        output = f"Nodes: {', '.join(self.model.nodes())}\n"
        for node in self.model.nodes():
            cpd = self.model.get_cpds(node)
            if cpd:
                output += f"\nCPD of {node}:"
                output += f"\n{cpd}\n"
        return output