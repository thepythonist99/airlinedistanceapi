"""
Views for the calculator module
"""
import os

from fastapi.responses import JSONResponse

from app import app

from . import utilities
from . import schemas

# view function to evaluate the distance between two railway stations
@app.get("/api/v1/distance/{start}/{stop}", 
        response_model=schemas.AirlineDistanceCalculator, 
        tags=["calculator"])
async def read_airline_distance(start: str, stop: str) -> JSONResponse:
  """
  Read computed airline distance
  """

  try:
    # get the computed airline distance
    airline_distance = utilities.compute_airline_distance(
      utilities.convert_coordinates(
        utilities.treat_coordinates(
          utilities.read_coordinate_file(
            os.environ.get('COORDINATE_FILE'),
            start=str(start), 
            stop=str(stop)
          )
        )
      )
    )

    # 
    response = {
      'from': airline_distance[1],
      'to': airline_distance[2],
      'distance': airline_distance[0],
      'unit': "km"
    }

    return JSONResponse(content=response, status_code=200)
    
  except:
    response = {
      "message": "Could not compute the airline distance between " + start + " and " + stop + ". Check logs for details."
    }
    utilities.logging.error("The start or stop railway stations might not be of type FV.")

    return JSONResponse(content=response, status_code=422)
