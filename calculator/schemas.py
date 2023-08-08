"""
Calculator Pydantic representation module
"""

from pydantic import BaseModel


class AirlineDistanceCalculatorBase(BaseModel):
  start: str
  stop: str
  unit: str

class AirlineDistanceCalculator(AirlineDistanceCalculatorBase):
  distance: int
