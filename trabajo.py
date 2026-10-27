import math
import random
import matplotlib.pyplot as plt

# Función objetivo a minimizar
def cost_function(x):
    return x**2 + 10 * math.sin(x)

# Generar vecino (vecindad)
def get_neighbor(x, step_size=0.5):
    return x + random.uniform(-step_size, step_size)

# Hill Climbing
def hill_climbing(start_x, iterations=100):
    current_x = start_x
    current_cost = cost_function(current_x)
    history = [current_cost]
    
    for _ in range(iterations):
        neighbor = get_neighbor(current_x)
        neighbor_cost = cost_function(neighbor)
        
        if neighbor_cost < current_cost:
            current_x = neighbor
            current_cost = neighbor_cost
        history.append(current_cost)
        
    return current_x, current_cost, history

# Simulated Annealing
def simulated_annealing(start_x, initial_temp=100, cooling_rate=0.9, iterations=100):
    current_x = start_x
    current_cost = cost_function(current_x)
    best_x, best_cost = current_x, current_cost
    T = initial_temp
    history = [current_cost]
    
    for _ in range(iterations):
        neighbor = get_neighbor(current_x)
        neighbor_cost = cost_function(neighbor)
        
        # Diferencia de costos
        delta = neighbor_cost - current_cost
        
        # Aceptar si es mejor, o con cierta probabilidad si es peor
        if delta < 0 or random.random() < math.exp(-delta / T):
            current_x = neighbor
            current_cost = neighbor_cost
            if current_cost < best_cost:
                best_x, best_cost = current_x, current_cost
                
        history.append(current_cost)
        T *= cooling_rate # Enfriamiento
        
    return best_x, best_cost, history

# Ejecución y Comparación
start_point = 8.0 # Punto inicial (lejos del óptimo)

hc_x, hc_cost, hc_history = hill_climbing(start_point)
sa_x, sa_cost, sa_history = simulated_annealing(start_point)

print(f"Hill Climbing: x={hc_x:.4f}, Costo={hc_cost:.4f}")
print(f"Simulated Annealing: x={sa_x:.4f}, Costo={sa_cost:.4f}")

# Gráfica de convergencia
plt.plot(hc_history, label='Hill Climbing')
plt.plot(sa_history, label='Simulated Annealing')
plt.title('Gráfica de Convergencia: HC vs SA')
plt.xlabel('Iteraciones')
plt.ylabel('Costo (Función Objetivo)')
plt.legend()
plt.show()