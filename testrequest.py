import requests
from pprint import pprint
session = requests.Session()
response = session.get('http://localhost:3000/showchart' )

# x = requests.get()

pprint(response.json())