from langgraph.graph import StateGraph, START, END
from check_evaluation import check_evaluation
from generator_tweet import generate
from evaluator_tweet import evaluate
from optimizer_tweet import optimize
from state_schema import TweetState
from structured_output_schema import TweetEvaluationOutput
from model import load_huggingface_model, load_ollama_model

model = load_huggingface_model()

structured_model = load_ollama_model(TweetEvaluationOutput, method='function_calling')

graph = StateGraph(state_schema=TweetState)

# Define nodes
graph.add_node('generate_tweet', generate)
graph.add_node('evaluate_tweet', evaluate)
graph.add_node('optimize_tweet', optimize)

# Define edges
graph.add_edge(START, 'generate_tweet')
graph.add_edge('generate_tweet', 'evaluate_tweet')

# Conditional edges based on evaluation results
graph.add_conditional_edges('evaluate_tweet', check_evaluation, {'approved': END, 'needs_improvement': 'optimize_tweet'})

# After optimization, we want to re-evaluate the tweet iteratively until it is approved
graph.add_edge('optimize_tweet', 'evaluate_tweet')

workflow = graph.compile()

