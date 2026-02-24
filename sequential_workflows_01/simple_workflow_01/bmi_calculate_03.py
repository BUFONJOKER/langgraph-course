from .bmi_state_class_02 import BMIState

def bmi_calculate(state:BMIState) -> BMIState:

    weight = state['weight_kg']
    height = state['height_m']

    bmi = weight/(height**2)
    bmi = round(bmi, 2)

    state['bmi'] = bmi

    return state