
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from typing import Literal, TypedDict
from dotenv import load_dotenv


# Load environment variables from a .env file
load_dotenv()


# Define the LLM model to be used in the workflow
model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)


# Define state
class ModerationState(TypedDict):
    post_content: str
    user_reputation: str
    
    formatted_post: str
    content_flag: str
    result: str
    
    
# Node 1: Format Post
def format_post(state: ModerationState):
    formatted = f"User: ({state['user_reputation']}) Says: ({state['post_content']})"
    return {
        "formatted_post": formatted
    }

# Node 2: Analyze content
def analyze_content(state: ModerationState):
    content = state['post_content'].lower()
    
    if 'spam' in content or 'buy now' in content or 'contact us' in content:
        flag = 'rejected'
    elif state['user_reputation'] == 'new_user':
        flag = 'review'
    else:
        flag = 'approved'
        
    return {
        'content_flag': flag
    }

# Node 3: Approve post
def approve_post(state: ModerationState):
    result = 'Post published successfully to the timeline.'
    return {
        'result': result
    }

# Node 4: Flag for review
def flag_for_review(state: ModerationState):
    result = 'Post sent to the human moderation queue.'
    return {
        'result': result
    }

# Node 5: Reject post
def reject_post(state: ModerationState):
    result = 'Post automatically deleted due to automatically policy violation.'
    return {
        'result': result
    }
    
# Routing function
def routing_function(state: ModerationState)-> Literal['approve_post', 'flag_for_review', 'reject_post']:
    if state['content_flag'] == 'approved':
        return 'approve_post'
    elif state['content_flag'] == 'review':
        return 'flag_for_review'
    else:
        return 'reject_post'
    
    
# Build Graph  
graph = StateGraph(ModerationState)

# Register Nodes
graph.add_node('format_post', format_post)
graph.add_node('analyze_content', analyze_content)
graph.add_node('approve_post', approve_post)
graph.add_node('flag_for_review', flag_for_review)
graph.add_node('reject_post', reject_post)


# Normal Edges
graph.add_edge(START, 'format_post')
graph.add_edge('format_post', 'analyze_content')

# Conditional edge
graph.add_conditional_edges('analyze_content', routing_function)

# Connect to END
graph.add_edge('approve_post', END)
graph.add_edge('flag_for_review', END)
graph.add_edge('reject_post', END)


# Compile
workflow = graph.compile()

# Initial State
initial_state = {
    'post_content': 'Check out this amazing new product, Buy Now!',
    'user_reputation': 'trusted_user'
}

# Execute
result = workflow.invoke(initial_state)

print(result)