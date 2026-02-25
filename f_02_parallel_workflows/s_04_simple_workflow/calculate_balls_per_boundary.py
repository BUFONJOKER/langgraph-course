from batsmen_state import BatsmenState

def balls_per_boundary(state: BatsmenState) -> dict:
    '''
    Calculates balls per boundary from given data balls, fours, sixes and return computed field
    '''

    balls = state.balls

    fours = state.fours

    sixes = state.sixes

    boundaries = fours + sixes

    result = balls / boundaries

    output = {"balls_per_boundary": round(result, 2)}

    return output