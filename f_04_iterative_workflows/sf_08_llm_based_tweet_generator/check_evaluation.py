from state_schema import TweetState

def check_evaluation(state: TweetState) -> str:
    '''
    This function checks the evaluation results and
    determines the next step in the workflow.
    
    '''
    
    if state['evaluation'] == 'approved' or state['iteration'] >= state['max_iterations']:
        return 'approved'

    return 'needs_improvement'