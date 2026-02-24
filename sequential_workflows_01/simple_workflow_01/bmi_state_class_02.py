from typing import TypedDict

class BMIState(TypedDict):

    weight_kg: float
    height_m: float
    bmi: float
    bmi_category: str