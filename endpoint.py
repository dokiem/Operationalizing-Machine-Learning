import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = ''
# If the service is authenticated, set the key or token
key = ''

# Two sets of data to score, so we get two results back
data = {
    "input_data": {
        "columns": [
            "age",
            "campaign",
            "cons.conf.idx",
            "cons.price.idx",
            "contact",
            "day_of_week",
            "default",
            "duration",
            "education",
            "emp.var.rate",
            "euribor3m",
            "housing",
            "job",
            "loan",
            "marital",
            "month",
            "nr.employed",
            "pdays",
            "poutcome",
            "previous"
        ],
        "index": [0, 1],
        "data": [
            [17, 1, -46.2, 92.893, "cellular", "mon", "no", 971, "university.degree", -1.8, 1.299, "yes", "blue-collar", "yes", "married", "may", 5099.1, 999, "failure", 1],
            [87, 1, -46.2, 92.893, "cellular", "mon", "no", 471, "university.degree", -1.8, 1.299, "yes", "blue-collar", "yes", "married", "may", 5099.1, 999, "failure", 1]
        ]
    }
}

# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())


