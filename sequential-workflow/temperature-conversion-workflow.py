from langgraph.graph import StateGraph, START, END
from typing import TypedDict


# Define the state of the temperature conversion workflow
class TemperatureState(TypedDict):
    celsius: float
    fahrenheit: float
    

# Define the temperature conversion nodes    
def celsius_to_fahrenheit(state: TemperatureState) -> TemperatureState:
    """Convert Celsius to Fahrenheit."""
    celsius = state["celsius"]
    fahrenheit = (celsius * 9/5) + 32
    state["fahrenheit"] = round(fahrenheit, 2)
    return state


# Create the state graph for the temperature conversion workflow
graph = StateGraph(TemperatureState)

# Add nodes to the graph
graph.add_node('celsius_to_fahrenheit', celsius_to_fahrenheit)

# Add edges to define the workflow
graph.add_edge(START, 'celsius_to_fahrenheit')
graph.add_edge('celsius_to_fahrenheit', END)

# Compile the graph and invoke it with an initial state
graph = graph.compile()
initial_state = {"celsius": 29.50}
final_output = graph.invoke(initial_state)

print(final_output)