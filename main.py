"""
Main launching file for the API
"""

import os
import uvicorn

# import the necessary module(s) to launch the API
from app import app
from calculator import views

# run the API
if __name__ == "__main__":
  uvicorn.run(
    app="app:app",
    host=os.environ.get('API_HOST'),
    reload=bool(os.environ.get('API_RELOAD')),
    port=int(os.environ.get('API_PORT'))
  )
