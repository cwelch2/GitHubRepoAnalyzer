# This file handles GitHub API requests and JSON saving
import requests
import json
import os

# makes a GET request to GitHub API and converts the response to JSON
def get_repo_data(owner, name):

    # link to GitHub API
    api_link = "https://api.github.com/repos/" + owner + "/" + name

    try:
        # request to GitHub API to get repo information
        github_request = requests.get(api_link, timeout=5)

        # if request was successful, store in JSON file
        if github_request.status_code == 200:
            # convert get request results to a dictionary
            request_dict = github_request.json()
            # convert to JSON
            request_json = json.dumps(request_dict, indent=4)

            os.makedirs("data", exist_ok=True)  #ensure the folder exists
            # write into JSON file to access later
            with open('data/repo_data.json', 'w') as f:
                f.write(request_json)
            return 'data/repo_data.json'
            # if request has a 404 code (page not found), return the code
        elif github_request.status_code == 404:
            return github_request.status_code
        else:
            print(f"Error: Code ({github_request.status_code})")

    except requests.exceptions.RequestException as error:
        print(f"Something went wrong: {error}")

    print("Could not fetch repo data")
    return None


def get_contributor_data(owner, name):
    # link to GitHub API to get contributor information
    api_link = "https://api.github.com/repos/" + owner + "/" + name + "/contributors"

    try:
        # request to GitHub API to get contributor information
        github_request = requests.get(api_link)

        # if request was successful, store in JSON file
        if github_request.status_code == 200:
            # convert get request results to a dictionary
            request_dict = github_request.json()

            # convert to json
            request_json = json.dumps(request_dict, indent=4)

            os.makedirs("data", exist_ok=True)  #ensure the folder exists
            # write into json file to access later
            with open("data/contributor_data.json", 'w') as f:
                f.write(request_json)
            return "data/contributor_data.json"
        # if request has a 204 code (the code when there are no contributors), return the code
        elif github_request.status_code == 204:
            return 204
        # contributor data not found
        elif github_request.status_code == 404:
            return 404
        else:
            print(f"Error: Code ({github_request.status_code})")

    except requests.exceptions.RequestException as error:
        print(f"Something went wrong: {error}")

    print("Could not fetch contributor data")
    return None


def get_commit_data(owner, name):
    # link to GitHub API to get contributor information
    api_link = "https://api.github.com/repos/" + owner + "/" + name + "/commits"
    try:
        # request to GitHub API to get commit information
        github_request = requests.get(api_link)

        # if request was successful, store in JSON file
        if github_request.status_code == 200:
            # convert get request results to a dictionary
            request_dict = github_request.json()

            # convert to JSON
            request_json = json.dumps(request_dict, indent=4)

            os.makedirs("data", exist_ok=True)  #ensure the folder exists
            # write into JSON file to access later
            with open('data/commit_data.json', 'w') as f:
                f.write(request_json)
            return 'data/commit_data.json'
        # if request has a 409 code (the code when there are no commits), return the code
        elif github_request.status_code == 409:
            return github_request.status_code
        elif github_request.status_code == 404:
            return 404
        else:
            print(f"Error: Code ({github_request.status_code})")

    except requests.exceptions.RequestException as error:
        print(f"Something went wrong: {error}")

    print("Could not fetch commit data")
    return None