"""
File to create an instance of the FastAPI class
"""

import os

from fastapi import FastAPI

# create a secret key
SECRET_KEY = os.environ.get('SECRET_KEY')

# instantiate a FastAPI app
app = FastAPI(
  title="AirlineDistanceCalcultorAPI",
  version="1.0",
  description="This API computes the airline distance between two railway stations.",
  contact={
    "name": "DB Systel GmbH",
    "email": "dbsystel@email.com",
	},
    swagger_ui_parameters={
      'filter': True
		}
)
