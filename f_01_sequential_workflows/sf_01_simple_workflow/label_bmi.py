from .bmi_state_class import BMIState

def label_bmi(state:BMIState) -> BMIState:
    bmi = state['bmi']

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    state['bmi_category'] = category

    return state