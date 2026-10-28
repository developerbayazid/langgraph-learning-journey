from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from typing import TypedDict
from dotenv import load_dotenv


# Load environment variables from a .env file
load_dotenv()


# Define the LLM model to be used in the workflow
model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.3)


# Define the state of the LLM workflow
class LLMState(TypedDict):
    input_text: str
    output_text: str
    
    
    
def llm_qa(state: LLMState) -> LLMState:
    """Process the input text using the LLM and store the output."""
    
    # Extract the input text from the state
    input_text = state["input_text"]
    
    prompt = f"Answer the following question based on the provided context:\n\n{input_text}\n\nAnswer:"
    
    # Use the LLM to process the input text
    output_text = model.invoke(prompt).content
    
    # Store the output text in the state
    state["output_text"] = output_text
    return state



graph = StateGraph(LLMState)

# Add nodes to the graph
graph.add_node('llm_qa', llm_qa)

# Add edges to define the workflow
graph.add_edge(START, 'llm_qa')
graph.add_edge('llm_qa', END)

graph = graph.compile()

final_result = graph.invoke({"input_text": "What is the capital of Bangladesh?"})

print(final_result)