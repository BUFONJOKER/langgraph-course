from pydantic import BaseModel, Field, field_validator, ConfigDict

class BatsmenState(BaseModel):
    '''
    BatsmenState Class which inherits pydantic BaseModel with variables
    runs (int)
    balls (int)
    fours (int)
    sixes (int)
    strike_rate (float)
    balls_per_boundary (float)
    boundary_percent (float)
    summary (str)
    '''

    # Enable validation when changing field values after creation
    model_config = ConfigDict(validate_assignment=True)

    runs: int = Field(description="Total runs scored by batsmen")

    balls: int = Field(description="Total balls played by batsmen")
    
    fours: int = Field(description="Total fours hit by batsmen")
    
    sixes: int = Field(description="Total sixes scored by batsmen")

    strike_rate: float = Field(
        default=0.0, description="Strike Rate calculated by runs over balls multiply by 100"
    )

    balls_per_boundary: float = Field(
        default=0.0, description="Total balls played divide by total boundaries fours + sixes hit"
    )

    boundary_percent: float = Field(
        default=0.0, description="Total boundaries fours + sixes over total runs multiply by 100"
    )

    summary: str = Field(
        default='', description="Summary of overall stats of innings"
    )
