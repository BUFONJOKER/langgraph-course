from batsmen_state import BatsmenState

def summary(state: BatsmenState) -> dict:
    '''
    Describe summary string from all data calculated from input data and return computed field
    '''

    summary_text = f'''
    Summary of Batsmen Innings
    Strike Rate = {state.strike_rate}
    Balls per Boundary = {state.balls_per_boundary}
    Boundaries Percent = {state.boundary_percent}
    '''
    output = {"summary": summary_text}
    return output