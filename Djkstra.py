import heapq 
import time

class Graph:

    #constructor de la clase
    def __init__(self):
    
    #diccionario 
        self.vertices = {}

    def add_vertex(self, vertex):

        #verificar si el vertice está en el directorio
        if vertex not in self.vertices:
            self.vertices[vertex] = []
    
    def add_edge(self,inicio, final, peso):
        #verifica si inicio y final se encuentran en el diccionario 
        #se agrega una arista con peso al grafo
        if inicio in self.vertices and final in self.vertices:
            self.vertices[inicio].append((final, peso))

        else:
            print("No existen los vertices")
    
    def dijkstra(self, inicio):
        #función djktra que se encarga de inicializar distancias

        #inicializa la distancia al nodo inicial como 0
        distancias = {vertex:float('infinity') for vertex in self.vertices}
        distancias[inicio]=0


        #usar cola de prioridad para seleccionar el nodo con distancia mas corta

        cola_prioridad = [(0, inicio)]

        while cola_prioridad:
            actual_distancia, actual_vertice = heapq.heappop(cola_prioridad)


            #si la distancia actual es mayor que la almacenada, ignora

            if actual_distancia > distancias[actual_vertice]:
                continue

            #Actualizar las distancias para los nodos cercanos

            for cercano, peso in self.vertices[actual_vertice]:
                distancia = actual_distancia +peso

                if distancia< distancias[cercano]:
                    distancias[cercano]= distancia
                    heapq.heappush(cola_prioridad, (distancia, cercano))
        return distancias 
    

def dijksta_tiempos(graph,inicio_vertice):
     start_time = time.time()

     distances_from_start = graph.dijkstra(inicio_vertice)

     end_time = time.time()
     execution_time = end_time - start_time

     print(f"Tiempo de ejecución para Dijkstra desde {inicio_vertice}: {execution_time} segundos")
     for vertex, distancia in distances_from_start.items():
        print(f"{vertex}: {distancia}")

     print(f"Tiempo de ejecución para Dijkstra desde {inicio_vertice}: {execution_time} segundos")
     return distances_from_start

# Crear un grafo de ejemplo
graph = Graph()

# Agregar vértices
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')


# Agregar aristas con pesos
graph.add_edge("1", "2", 7)
graph.add_edge("1", "4", 2)
graph.add_edge("4", "2", 3)
graph.add_edge("2", "4", 2)
graph.add_edge("4", "3", 8)
graph.add_edge("2", "3", 1)
graph.add_edge("4", "5", 5)
graph.add_edge("5", "3", 4)
graph.add_edge("3", "5", 5)

# Calcular las distancias mínimas desde el nodo 'A'
start_vertex = '1'
distances_from_start =  dijksta_tiempos(graph, start_vertex)

# Imprimir resultados
print(f"Distancias mínimas desde {start_vertex}:")
for vertex, distancia in distances_from_start.items():
    print(f"{vertex}: {distancia}")