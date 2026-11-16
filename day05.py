import requests

username = input("Enter a GitHub username: ")
url = "https://api.github.com/users/" + username

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()
        print("Name:", data["login"])
        print("Public repos:", data["public_repos"])
    elif response.status_code == 404:
        print("No user found with that name.")
    else:
        print("Something went wrong. Code:", response.status_code)

except requests.exceptions.RequestException:
    print("Could not reach GitHub. Check your internet.")