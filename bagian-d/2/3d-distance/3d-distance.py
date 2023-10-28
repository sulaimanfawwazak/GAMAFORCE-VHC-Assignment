import math

# to calculate the distance using latitude, longitude, and altitude
# we cannot use the Euclidean distance right away
# instead, we can use the Haversine formula to calculate the distance using longitude and latitude
# then we can use the Euclidean distance formula to calculate the distance using altitude

# Earth radius
earth_radius = 63781000000

# Calculate the altitude (vertical) distance
def altDistance(alt1, alt2):
  distance = abs(alt1 - alt2)

  return distance

# Calculate the longitude-latitude (horizontal) distance
def longLatDistance(long1, long2, lat1, lat2):
  distance = 2 * earth_radius * math.asin(math.sqrt(math.sin((lat2 - lat1)/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin((long2 - long1)/2)**2))

  return distance

# Calculate the final distance
def finalDistance(altDistance, longLatDistance):
  distance = math.sqrt(altDistance**2 + longLatDistance**2)

  return distance

# Get the input
def getInput():
  # Point 1
  print("Please input your 1st point data")
  lat1 = float(input("Latitude 1: "))
  long1 = float(input("Longitude 1: "))
  alt1 = float(input("Altitude 1: "))

  # Point 2
  print("\nPlease input your 2nd point data")
  lat2 = float(input("Latitude 2: "))
  long2 = float(input("Longitude 2: "))
  alt2 = float(input("Altitude 2: "))
  
  return lat1, long1, alt1, lat2, long2, alt2

if (__name__) == '__main__':
  # Assign the data
  lat1, long1, alt1, lat2, long2, alt2 = getInput()

  # Convert the latitude and the longitude into radians
  lat1, long1, lat2, long2 = map(math.radians, [lat1, long1, lat2, long2])

  # Get the vertical distance
  vert_distance = altDistance(alt1, alt2)
  print("\nVertical Distance: ", vert_distance)

  # Get the horizontal distance
  horiz_distance = longLatDistance(long1, long2, lat1, lat2)
  print("Horizontal DistanceL :", horiz_distance)

  # Get the final distance
  final_distance = finalDistance(vert_distance, horiz_distance)
  print("Distance of 2 points: ", final_distance)