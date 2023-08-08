"""
Utility functions for the calculator module
"""

import logging
import math

# configure the logging module
logging.basicConfig(format='%(asctime)s | %(levelname)s: %(message)s', level=logging.NOTSET)

# function to read the coordinate file
def read_coordinate_file(
  coordinate_file: str,
  start: str,
  stop: str
):
  """
  Function to read and treat the coordinate
  file accordingly for use with calculations
  """

  # the file must have a .csv extension for this to work
  if 'csv' in coordinate_file.split('.'):
    # read the file
    with open(coordinate_file, 'r') as stations:
      for station in stations:
        # make sure we deal only with the stations that we want
        if start == station.split(';')[1]:
          if station.split(';')[4] == 'FV':
            logging.debug("Start railstation: " + station)
            # get the start station's longitude (Laenge) and latitude (Breite)
            start_station_name = station.split(';')[3]
            start_longitude = station.split(';')[5]
            start_latitude = station.split(';')[6]
          else:
            logging.error("This is not a FV railway station.")
            raise Exception("This is not a FV railway station.")

        if stop == station.split(';')[1]:
          if station.split(';')[4] == 'FV':
            logging.debug("Stop railstation: " + station)
            # get the end station's longitude (Laenge) and latitude (Breite)
            stop_station_name = station.split(';')[3]
            stop_longitude = station.split(';')[5]
            stop_latitude = station.split(';')[6]
          else:
            logging.error("This is not a FV railway station.")
            raise Exception("This is not a FV railway station.")

  else:
    logging.error(msg="The file must be of the csv type.")

  logging.info("Successfully read input file.")

  return (start_longitude, start_latitude, stop_longitude, stop_latitude), (start_station_name, stop_station_name)

# function treat the coordinates returned for better utility
def treat_coordinates(coordinates: tuple):
  """
  Function to treat the coordinates returned
  for better utility in computation
  """

  final_coordinates = list()

  for coordinate in coordinates[0]:
    splitted_coordinate = str(coordinate).split(',')
    treated_coordinate = [int(element) for element in splitted_coordinate] # [8, 664137]
    joined_coordinate = '{0}.{1}'.format(treated_coordinate[0], treated_coordinate[1])
    final_coordinates.append(float(joined_coordinate))
  final_coordinates.append(coordinates[1])

  logging.info("Successfully applied treatment to all the coordinates in the file.")

  return final_coordinates

# function to convert the final coordinates in to radian values
def convert_coordinates(final_coordinates: list()):
  """
  Function to convert the coordinates
  into radian values for better computation
  """

  # convert the final coordinates into radian values
  converted_coordinates = [(degree_coordinate * 3.14)/180 for degree_coordinate in final_coordinates \
                            if type(degree_coordinate) is float]
  
  # converted coordinates with rail station names

  logging.info("Successfully converted all the coordinates to radian values.")

  return converted_coordinates + [final_coordinates[4]]

# function to compute the airline distance
def compute_airline_distance(converted_coordinates: list()) -> int:
  """
  Function to compute the airline distance
  between two given coordinates points
  """

  # compute the airline distance given the coordinates
  airline_distance = math.acos(
    math.sin(converted_coordinates[3]) * math.sin(converted_coordinates[1]) + \
    math.cos(converted_coordinates[3]) * math.cos(converted_coordinates[1]) * \
    math.cos(converted_coordinates[2] - converted_coordinates[0])
  ) * 6365

  logging.info("Successfully computed airline distance. Check endpoint for value.")

  return math.ceil(airline_distance), converted_coordinates[4][0], converted_coordinates[4][1]
