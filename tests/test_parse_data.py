import json
import pytest
from parse_data import parse_repo_data, parse_contributor_data, parse_commit_data

#fixture to create a temp JSON file with mock repo data
@pytest.fixture
def repo_json(tmp_path):
    data = {
        "full_name": "evanB/Hello-World",
        "owner": {"login": "evanB"},
        "name": "Hello-World",
        "description": "This is a test repo description",
        "stargazers_count": 80,
        "forks": 9,
        "open_issues": 0
    }
    path = tmp_path / "repo_data.json"
    with open(path, "w") as f:
        json.dump(data, f)
    return path

#fixture to create a temp JSON file with mock contributor data
@pytest.fixture
def contributor_json(tmp_path):
    data = [{"login": f"user{i}"} for i in range(1, 4)] #user1, user2, user3
    path = tmp_path / "contributor_data.json"
    with open(path, "w") as f:
        json.dump(data, f)
    return path

#fixture to create a temp JSON file with mock commit data
@pytest.fixture
def commit_json(tmp_path):
    data = [{
        "commit": {
            "message": f"Commit message {i}",
            "author": {"date": f"2023-07-0{i}T12:00:00Z"}
        },
        "author": {"login": f"author{i}"}
    } for i in range(1, 4)]  # 3 mock commits
    path = tmp_path / "commit_data.json"
    with open(path, "w") as f:
        json.dump(data, f)
    return path

# TESTS
def test_parse_repo_data(repo_json):
    output = parse_repo_data(repo_json)
    assert "GitHub Link: https://github.com/evanB/Hello-World" in output
    assert "Repo Owner: evanB" in output
    assert "Repo Name: Hello-World" in output
    assert "Stars: 80" in output

def test_parse_contributor_data(contributor_json):
    output = parse_contributor_data(contributor_json)
    assert "Biggest Contributors: user1, user2, user3" == output

def test_parse_commit_data(commit_json):
    output = parse_commit_data(commit_json)
    assert "1. Commit message 1 by author1 on 2023-07-01" in output
    assert "2. Commit message 2 by author2 on 2023-07-02" in output
