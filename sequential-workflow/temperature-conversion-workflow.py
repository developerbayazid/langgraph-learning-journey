from langgraph.graph import StateGraph, START, END
from typing import TypedDict


# Define the state of the temperature conversion workflow
class TemperatureState(TypedDict):
    celsius: float
    fahrenheit: float
    weather_status: str
    

# Define the temperature conversion nodes    
def celsius_to_fahrenheit(state: TemperatureState) -> TemperatureState:
    """Convert Celsius to Fahrenheit."""
    celsius = state["celsius"]
    fahrenheit = (celsius * 9/5) + 32
    state["fahrenheit"] = round(fahrenheit, 2)
    return state


def label_weather(state: TemperatureState) -> TemperatureState:
    """Label the weather based on the Fahrenheit temperature."""
    fahrenheit = state["fahrenheit"]
    if fahrenheit < 32:
        state["weather_status"] = "Cold"
    elif 32 <= fahrenheit < 60:
        state["weather_status"] = "Cool"
    elif 60 <= fahrenheit < 80:
        state["weather_status"] = "Warm"
    else:
        state["weather_status"] = "Hot"
    return state


# Create the state graph for the temperature conversion workflow
graph = StateGraph(TemperatureState)

# Add nodes to the graph
graph.add_node('celsius_to_fahrenheit', celsius_to_fahrenheit)
graph.add_node('label_weather', label_weather)

# Add edges to define the workflow
graph.add_edge(START, 'celsius_to_fahrenheit')
graph.add_edge('celsius_to_fahrenheit', 'label_weather')
graph.add_edge('label_weather', END)

# Compile the graph and invoke it with an initial state
graph = graph.compile()
initial_state = {"celsius": 20.50}
final_output = graph.invoke(initial_state)

print(final_output)