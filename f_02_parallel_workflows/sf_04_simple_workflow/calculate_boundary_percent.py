from batsmen_state import BatsmenState

def boundary_percent(state: BatsmenState) -> dict:
    '''
    Calculate boundary percent from given data runs, fours, sixes and return computed field
    '''

    runs = state.runs

    fours = state.fours

    sixes = state.sixes

    boundaries_score = (fours*4) + (sixes*6)


    result = (boundaries_score/runs) * 100

    output = {"boundary_percent": round(result, 2)}

    return output
    