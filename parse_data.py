# this file extracts and formats data from json
import json

#open and read json file
def parse_repo_data():
    with open('data/repo_data.json', 'r') as f:
        data = json.load(f)

    # link to GitHub for repo
    human_facing_link = "https://github.com/" + data['full_name']

    repo_info = [
        f"GitHub Link: {human_facing_link}",
        f"Repo Owner: {data['owner']['login']}",
        f"Repo Name: {data['name']}",
        f"Description: {data['description']}",
        f"Stars: {data['stargazers_count']}",
        f"Forks: {data['forks']}",
        f"Open Issues: {data['open_issues']}"
    ]

    return "\n".join(repo_info)

def parse_contributor_data():
    #number of biggest contributors that will be outputted
    contributors_num = 5
    #list to store contributors
    contributors_list = []

    #open contributor_data.json to read
    with open('data/contributor_data.json', 'r') as f:
        data = json.load(f)

    #loop to add contributors to the list
    for i in range(contributors_num):
        #if there are less contributors than current iteration, stop the loop
        if len(data) <= i:
            break
        contributor_name = data[i]['login']         # current contributor
        contributors_list.append(contributor_name)  # add current contributor to list

    #print the contributors in the list with ", " seperating each
    #return.ist append contributors list.join or something
    return "Biggest Contributors: " + ", ".join(contributors_list)

def parse_commit_data():
    #number of most recent commits to be outputted
    recent_commits_num = 5
    commits_list = []
    # open contributor_data.json to read
    with open('data/commit_data.json', 'r') as f:
        data = json.load(f)


    for i in range(recent_commits_num):
        # if there are less commits than current iteration, stop the loop
        if len(data) <= i:
            break
        commit_message = data[i]['commit']['message']
        commit_author = data[i]['author']['login']
        commit_date = data[i]['commit']['author']['date'][:-10] #only the date, no time to make it simpler

        commits_list.append(f"{i + 1}. {commit_message} by {commit_author} on {commit_date}")

    return "Most Recent Commits: \n" + "\n".join(commits_list)

#REPO NAME
#OWNER
#DESCRIPTION
#STARS
#FORKS
#OPEN ISSUES
#LIST OF contributorS (MAY NOT EXIST)
#MOST RECENT COMMITS (E.G. TOP 5) (MAY NOT EXIST)


