from mimetypes import init

from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from typing import Literal, TypedDict, Annotated
from pydantic import BaseModel, Field
from langchain.messages import HumanMessage, SystemMessage
import operator
from dotenv import load_dotenv


# Load environment variables from a .env file
load_dotenv()


# Define the LLM model to be used in the workflow
generator_llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
evaluator_llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
optimizer_llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)



class PostEvaluation(BaseModel):
    evaluation: Literal["approved", "needs_improvement"] = Field(..., description="Final evaluation result.")
    feedback: str = Field(..., description="feedback for the Facebook post.")
    
    
structured_evaluator_llm = evaluator_llm.with_structured_output(PostEvaluation)

post = """
🚀 The future of AI is no longer just about answering questions — it’s about taking action.

Welcome to the era of *Agentic AI* 🤖

Agentic AI systems can plan, reason, make decisions, and execute tasks autonomously. From managing workflows and analyzing data to coordinating tools and solving complex problems, these AI agents are transforming how we work and innovate.

Imagine an AI that doesn’t just assist you — it collaborates with you.

🔹 Smarter automation
🔹 Faster decision-making
🔹 Personalized experiences
🔹 Continuous learning & adaptation

Businesses, developers, and creators who embrace Agentic AI early will shape the next generation of digital transformation.

The question is no longer *“Can AI do this?”*
It’s *“How far can AI agents go?”*

#AgenticAI #ArtificialIntelligence #AI #Automation #FutureOfWork #Innovation #TechTrends #GenerativeAI

"""


result = structured_evaluator_llm.invoke(post)

# print("Evaluation Result:", result.evaluation)
# print("Feedback:", result.feedback)


class PostState(TypedDict):
    topic: str
    post: str
    evaluation: Literal["approved", "needs_improvement"]
    feedback: str
    iteration: int
    max_iteration: int

    post_history: Annotated[list[str], operator.add]
    feedback_history: Annotated[list[str], operator.add]
    
    

graph = StateGraph(PostState)


def generate(state: PostState):
    # prompt
    messages = [
        SystemMessage(content="You are a funny and clever Facebook influencer."),
        HumanMessage(content=f"""
        Write a short, original, and hilarious Facebook post on the topic: "{state['topic']}".

        Rules:
        - Do NOT use question-answer format.
        - Max 500 characters.
        - Use observational humor, irony, sarcasm, or cultural references.
        - Think in meme logic, punchlines, or relatable takes.
        - Use simple, day to day english
        """)
    ]
    
    response = generator_llm.invoke(messages).content
    return {
        "post": response,
        "iteration": state["iteration"] + 1,
        "post_history": state["post_history"] + [response]
    }
    

def evaluate(state: PostState):
    # prompt
    messages = [
        SystemMessage(content="You are a ruthless, no-laugh-given Facebook critic. You evaluate posts based on humor, originality, virality, and post format."),
        HumanMessage(content=f"""
        Evaluate the following Facebook post:

        Post: "{state['post']}"

        Use the criteria below to evaluate the post:

        1. Originality – Is this fresh, or have you seen it a hundred times before?  
        2. Humor – Did it genuinely make you smile, laugh, or chuckle?  
        3. Punchiness – Is it short, sharp, and scroll-stopping?  
        4. Virality Potential – Would people share, react, or comment on it?  
        5. Format – Is it a well-formed Facebook post (not a setup-punchline joke, not a Q&A joke, and under 500 characters)?

        Auto-reject if:
        - It's written in question-answer format (e.g., "Why did..." or "What happens when...")
        - It exceeds 500 characters
        - It reads like a traditional setup-punchline joke
        - Dont end with generic, throwaway, or deflating lines that weaken the humor (e.g., “Masterpieces of the auntie-uncle universe” or vague summaries)

        ### Respond ONLY in structured format:
        - evaluation: "approved" or "needs_improvement"  
        - feedback: One paragraph explaining the strengths and weaknesses 
        """)
    ]

    response = structured_evaluator_llm.invoke(messages)
    return {'evaluation':response.evaluation, 'feedback': response.feedback, 'feedback_history': [response.feedback]}
    
    

def optimize(state: PostState):
    messages = [
        SystemMessage(content="You punch up Facebook posts for virality and humor based on given feedback."),
        HumanMessage(content=f"""
        Improve the Facebook post based on this feedback:
        "{state['feedback']}"

        Topic: "{state['topic']}"
        Original Post:
        {state['post']}

        Re-write it as a short, viral-worthy Facebook post. Avoid Q&A style and stay under 500 characters.
        """)
    ]

    response = optimizer_llm.invoke(messages).content
    iteration = state['iteration'] + 1

    return {'post': response, 'iteration': iteration, 'post_history': [response]}


def route_evaluation(state: PostState):

    if state['evaluation'] == 'approved' or state['iteration'] >= state['max_iteration']:
        return 'approved'
    else:
        return 'needs_improvement'


graph.add_node('generate', generate)
graph.add_node('evaluate', evaluate)
graph.add_node('optimize', optimize)


graph.add_edge(START, 'generate')
graph.add_edge('generate', 'evaluate')
graph.add_conditional_edges('evaluate',route_evaluation,{'approved': END, 'needs_improvement': 'optimize'})
graph.add_edge('optimize', 'evaluate')


workflow = graph.compile()

initial_state = {
    'topic': 'Agentic AI',
    'iteration': 0,
    'max_iteration': 3
}

result = workflow.invoke(initial_state)

print(result)
print("Final Post:", result['post'])
print("Evaluation:", result['evaluation'])