import parse_data
import fetch_data
from cleanup import remove_files

repo_owner = input("Repo Owner: ")
repo_name = input("Repo Name: ")

#Fetch and output general repo data
fetch_repo = fetch_data.get_repo_data(repo_owner, repo_name)
# if repo was fetched, parse the data using the filepath returned in fetch_repo
if fetch_repo == "data/repo_data.json":
    print(parse_data.parse_repo_data(fetch_repo))

# if repo wasn't fetched, check if it exists (code 404)
elif fetch_repo == 404:
    print("Repo not found! Check repo name and owner, repo may be private")


#Fetch and output contributor data
fetch_contributor = fetch_data.get_contributor_data(repo_owner, repo_name)
# if contributors were fetched, parse the data.
if fetch_contributor == "data/contributor_data.json":
    print(parse_data.parse_contributor_data(fetch_contributor))

# if contributors weren't fetched, check if they exist (code 204)
elif fetch_contributor == 204:
    print("Repo has no contributors!")

#Fetch and output commit data
fetch_commit = fetch_data.get_commit_data(repo_owner,repo_name)
# if commits were fetched, parse the data
if fetch_commit == "data/commit_data.json":
    print(parse_data.parse_commit_data(fetch_commit))

# if commits weren't fetched, check if they exist (code 409)
elif fetch_commit == 409:
    print("Repo has no commits!")

#Prompt user to delete or retain JSON files
if fetch_repo == "data/repo_data.json": #only prompt user if repo was found
    while True:    #loop until user makes a valid input
        delete_choice = input("Keep repository JSON files? (y/n): ").strip().lower()
        if delete_choice in ('y', 'yes', 'no', 'n'):
            break
        print("Invalid input. Try again.")
    if delete_choice == 'n' or delete_choice == 'no':
        remove_files(fetch_repo, fetch_contributor, fetch_commit)
    elif delete_choice == 'y' or delete_choice == 'yes':
        print("JSON files retained.")


