# Making a GET Requests

import requests

url = "https://api.example.com/data"  # Replace this with the URL you want to make a GET request to

try:
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()  # Assuming the response is in JSON format
        print(data)
    else:
        print(f"Request failed with status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

    # How to make a POST Request

    import requests

url = "https://api.example.com/submit"  # Replace this with the URL you want to make a POST request to
data = {
    "key1": "value1",
    "key2": "value2",
}  # Replace with the data you want to submit

try:
    response = requests.post(url, data=data)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        result = response.json()  # Assuming the response is in JSON format
        print(result)
    else:
        print(f"Request failed with status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

