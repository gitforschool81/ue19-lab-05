import requests

# The URL for the random joke API
url = "https://official-joke-api.appspot.com/random_joke"

try:
    # 1. Send a GET request to the API
    response = requests.get(url)

    # 2. Check if the request was successful (status code 200)
    if response.status_code == 200:
        # 3. Parse the JSON response into a Python dictionary
        joke_data = response.json()

        # 4. Extract the setup and punchline from the dictionary
        setup = joke_data['setup']
        punchline = joke_data['punchline']

        # 5. Print the joke
        print("Here's your joke:")
        print(f"Setup: {setup}")
        print(f"Punchline: {punchline}")

    else:
        # Handle cases where the API might be down or returned an error
        print(f"Error: Failed to fetch joke. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    # Handle potential network errors (e.g., no internet connection)
    print(f"An error occurred with the request: {e}")
