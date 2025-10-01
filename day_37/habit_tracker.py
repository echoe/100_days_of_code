"""Pixela and post requests! Comment out the thing you need to run it."""
import requests
from datetime import datetime
PIXELA_ENDPOINT="https://pixe.la/v1/users"

# Fill these out
PIXELA_USER="" #Pick a username!
PIXELA_TOKEN="" #Make a random one for yourself :)
GRAPH_ID="" # Make a random one for yourself! :)
TIMEZONE='UTC' # Adjust this as necessary
auth_headers = {
    'X-USER-TOKEN': PIXELA_TOKEN
}
#Create a user. Comment this out after making it :)
# user_params={
#     'token': PIXELA_TOKEN,
#     'username': PIXELA_USER,
#     'notMinor': 'yes',
#     'agreeTermsOfService': 'yes',
# }
# user_response = requests.post(url=PIXELA_ENDPOINT,json=user_params)
# print(user_response.text)

# Create a graph definition. Comment this out after making it
# graph_params = {
#     'id': GRAPH_ID,
#     'name': 'Coding Daily Tracker',
#     'unit': 'days',
#     'type': 'int',
#     'color': 'ajisai', #purple
#     'timezone': TIMEZONE,
# }
# graph_response = requests.post(url=f"{PIXELA_ENDPOINT}/{PIXELA_USER}/graphs",json=graph_params,headers=auth_headers)
# print(graph_response.text)

#Add a pixel to the graph.
# data_params = {
#     'date': datetime.now().strftime('%Y%m%d'), #Get today's date and format it to the requested format.
#     'quantity': "1"
# }
# add_pixel = requests.post(url=f"{PIXELA_ENDPOINT}/{PIXELA_USER}/graphs/{GRAPH_ID}",json=data_params,headers=auth_headers)
# print(add_pixel.text)

#Modify a pixel.
# edit_params = {
#     'quantity': "2"
# }
# edit_pixel = requests.put(url=f"{PIXELA_ENDPOINT}/{PIXELA_USER}/graphs/{GRAPH_ID}/{datetime.now().strftime('%Y%m%d')}",json=edit_params,headers=auth_headers)
# print(edit_pixel.text)

#Delete a pixel.
# delete_pixel = requests.delete(url=f"{PIXELA_ENDPOINT}/{PIXELA_USER}/graphs/{GRAPH_ID}/{datetime.now().strftime('%Y%m%d')}",headers=auth_headers)
# print(delete_pixel.text)