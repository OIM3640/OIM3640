import urllib.request
import json
import pprint

url = "http://api.open-notify.org/astros.json"

with urllib.request.urlopen(url) as response:
    response_text = response.read().decode("utf-8")
    # print(response_text)
    # print(type(response_text))
    data = json.loads(response_text)
    # print(data)
    # print(type(data))
    pprint.pprint(data)
    # print(len(data))

# Can you print number of people in the space?
# print(data['number'])

# Can you print all the names?
people = data['people']
for astro in people:  # type(people): list  type(astro): dict
    # print(type(astro))
    # how to get the name form the dict
    print(astro['name'])



