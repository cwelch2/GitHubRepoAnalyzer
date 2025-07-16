import parse_data
import fetch_data
#repo_owner = input("Repo Owner: ")
#repo_name = input("Repo Name: ")


#hardcode for testing, remove later
# 'https://api.github.com/repos/pallets/flask'
repo_owner = "pallets"
repo_name = "flask"

fetch_repo = fetch_data.get_repo_data(repo_owner, repo_name)
# if repo was fetched, parse the data
if fetch_repo == 'data/repo_data.json':
    print(parse_data.parse_repo_data())

# if repo wasn't fetched, check if it exists (code 404)
elif fetch_repo == 404:
    print("Repo not found! Check repo name and owner")


fetch_contributor = fetch_data.get_contributor_data(repo_owner, repo_name)
# if contributors were fetched, parse the data.
if fetch_contributor == 'data/contributor_data.json':
    print(parse_data.parse_contributor_data())

# if contributors weren't fetched, check if they exist (code 204)
elif fetch_contributor == 204:
    print("Repo has no contributors!")


fetch_commit = fetch_data.get_commit_data(repo_owner,repo_name)
# if commits were fetched, parse the data
if fetch_commit == 'data/commit_data.json':
    print(parse_data.parse_commit_data())

# if commits weren't fetched, check if they exist (code 409)
elif fetch_commit == 409:
    print("Repo has no commits!")



