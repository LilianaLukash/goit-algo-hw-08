import heapq

def min_cost_to_connect_cables(lengths):
    # Initialize the heap with the cable lengths
    heapq.heapify(lengths)
    
    total_cost = 0
    
    # While there's more than one cable left, connect the two shortest
    while len(lengths) > 1:
        # Pop the two shortest cables
        first = heapq.heappop(lengths)
        second = heapq.heappop(lengths)
        
        # Calculate the cost to connect them
        cost = first + second
        total_cost += cost
        
        # Add the connected cable back to the heap
        heapq.heappush(lengths, cost)
    
    return total_cost

# Example 
cable_lengths = [5, 4, 2, 8]
print(min_cost_to_connect_cables(cable_lengths))
