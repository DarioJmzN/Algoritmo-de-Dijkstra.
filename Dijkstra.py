#Pablo Darío Jiménez Nuño


import heapq  #Para usar la estructura de datos de cola de prioridad (heap)
import networkx as nx # Librería para trabajar con grafos
import matplotlib.pyplot as plt #Para visualizar grafos

def dijkstra(graph, start):
    # Inicializar distancias con infinito para todos los nodos excepto el inicio
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # Distancia al nodo de inicio es 0
    # Usar un heap para mantener los nodos no visitados ordenados por distancia mínima conocida
    priority_queue = [(0, start)]  # (distancia_actual, nodo_actual)
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Si encontramos una distancia menor en el heap, continuamos
        if current_distance > distances[current_node]:
            continue
        
        # Explorar los vecinos del nodo actual
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Si encontramos un camino más corto hacia el vecino, lo actualizamos
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Función para visualizar el grafo y el camino más corto encontrado
def visualize_graph(graph, shortest_distances, start_node):
    G = nx.Graph(graph)
    
    # Extraer las aristas del grafo original que están en el camino más corto
    edges_in_shortest_path = []
    for node, distance in shortest_distances.items():
        if node != start_node and distance != float('inf'):
            path = nx.shortest_path(G, start_node, node)
            for i in range(len(path) - 1):
                edges_in_shortest_path.append((path[i], path[i+1]))
    
    pos = nx.spring_layout(G)  # Posiciones de los nodos para graficar
    
    # Dibujar el grafo
    plt.figure(figsize=(12, 10))
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
    
    # Dibujar las aristas del camino más corto en un color diferente
    nx.draw_networkx_edges(G, pos, edgelist=edges_in_shortest_path, width=2.0, edge_color='r', alpha=0.7)
    
    # Mostrar la distancia más corta encontrada para cada nodo
    labels = {node: f"{node}\nDistancia mas corta: {distance}" for node, distance in shortest_distances.items()}
    nx.draw_networkx_labels(G, pos, labels, font_size=10, font_color='black', font_family='sans-serif')
    
    plt.title('Mapa de conexiones diarias y camino más corto')
    plt.axis('off')
    plt.show()

# Ejemplo de uso en la vida diaria de una persona con parque e iglesia
if __name__ == "__main__":
    # Definir el grafo como un diccionario de diccionarios con distancias en minutos
    graph = {
        'Hogar': {'Escuela': 10, 'Trabajo': 15, 'Mercado': 5, 'Amigos': 20, 'Parque': 8, 'Iglesia': 12},
        'Escuela': {'Hogar': 10, 'Trabajo': 25, 'Mercado': 12, 'Amigos': 15, 'Parque': 10, 'Iglesia': 20},
        'Trabajo': {'Hogar': 15, 'Escuela': 25, 'Mercado': 8, 'Amigos': 30, 'Parque': 15, 'Iglesia': 10},
        'Mercado': {'Hogar': 5, 'Escuela': 12, 'Trabajo': 8, 'Amigos': 10, 'Parque': 5, 'Iglesia': 15},
        'Amigos': {'Hogar': 20, 'Escuela': 15, 'Trabajo': 30, 'Mercado': 10, 'Parque': 25, 'Iglesia': 18},
        'Parque': {'Hogar': 8, 'Escuela': 10, 'Trabajo': 15, 'Mercado': 5, 'Amigos': 25, 'Iglesia': 10},
        'Iglesia': {'Hogar': 12, 'Escuela': 20, 'Trabajo': 10, 'Mercado': 15, 'Amigos': 18, 'Parque': 10}
    }
    
    start_node = 'Hogar'
    shortest_distances = dijkstra(graph, start_node)
    
    print("Distancias mas cortas desde.", start_node)
    for node, distance in shortest_distances.items():
        print(f"Hasta {node}: {distance} minutos")
    
    # Visualizar el grafo y el camino más corto
    visualize_graph(graph, shortest_distances, start_node)
