from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from typing import TypedDict
from dotenv import load_dotenv


# Load environment variables from a .env file
load_dotenv()


# Define the LLM model to be used in the workflow
model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.3)


# Define the state of the employee analytics workflow
class EmployeeState(TypedDict):
    employee_id: int
    employee_name: str
    monthly_salary: int
    working_days: int
    completed_projects: int
    
    yearly_salary: int
    bonus_amount: int
    project_status: str
    summary: str
    
 
# Calculate yearly salary based on monthly salary and working days
def calculate_yearly_salary(state: EmployeeState) -> dict:
    yearly_salary = state["monthly_salary"] * 12
    return {
        'yearly_salary': yearly_salary
    }


# Calculate bonus based on yearly salary
def calculate_bonus(state: EmployeeState) -> dict:
    bonus_amount = state["monthly_salary"] * 0.1  # Example bonus calculation  
    return {
        "bonus_amount" : bonus_amount
    }

# Evaluate project performance based on completed projects
def project_evaluation(state: EmployeeState) -> dict:
    # Example project evaluation logic
    if state["completed_projects"] >= 5:
        project_status = "Excellent"
    else:
        project_status = "Needs Improvement"
    return {
        'project_status' : project_status
    }

def summary(state: EmployeeState) -> dict:
    summary = (
        f"Employee ID: {state['employee_id']}, "
        f"Employee: {state['employee_name']}, "
        f"Yearly Salary: {state['yearly_salary']}, "
        f"Bonus: {state['bonus_amount']}, "
        f"Project Status: {state['project_status']}"
    )

    return {
        'summary' : summary
    }

# Define the graph
graph = StateGraph(EmployeeState)


# add nodes to the graph
graph.add_node('calculate_yearly_salary', calculate_yearly_salary)
graph.add_node('calculate_bonus', calculate_bonus)
graph.add_node('project_evaluation', project_evaluation)
graph.add_node('summary', summary)

# add edges to define the workflow
graph.add_edge(START, 'calculate_yearly_salary')
graph.add_edge(START, 'calculate_bonus')
graph.add_edge(START, 'project_evaluation')

# graph.add_edge('calculate_yearly_salary', 'calculate_bonus')

# # Wait for both branches before summary
# graph.add_edge(
#     ["calculate_bonus", "project_evaluation"],
#     "summary"
# )

graph.add_edge('calculate_yearly_salary', 'summary')
graph.add_edge('calculate_bonus', 'summary')
graph.add_edge('project_evaluation', 'summary')

graph.add_edge('summary', END)

parallel_workflow = graph.compile()



initial_state = {
    "employee_id": 1,
    "employee_name": "Bayazid Hasan",
    "monthly_salary": 5000,
    "working_days": 22,
    "completed_projects": 6
}

state = parallel_workflow.invoke(initial_state)

print(state['summary'])