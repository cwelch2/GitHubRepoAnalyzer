import pytest
import fetch_data
from unittest.mock import patch, Mock
import os
import requests

#sample data to mock api response
sample_repo_data = {"name": "sample", "full_name": "test/sample"}
sample_contributor_data = [{"login": "dev1", "contributions": 10}]
sample_commit_data = [{"sha":"abc123"}]

#fixture to patch get request in fetch_data
@pytest.fixture
def mock_requests_get():
    with patch("fetch_data.requests.get") as mock:
        yield mock

#test: a successful response from get_repo_data
def test_get_repo_data_success(tmp_path, mock_requests_get, cleanup_test_data):
    #create a mock response object with a 200 status and JSON data
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = sample_repo_data
    mock_requests_get.return_value = mock_response

    #call the function and check the returned path and file existence
    output_path = fetch_data.get_repo_data("test", "sample")
    assert output_path == 'data/repo_data.json'
    assert os.path.exists('data/repo_data.json')  #confirm file was saved
    os.remove('data/repo_data.json')

#test: get_repo_data handling a 404 not found response
def test_get_repo_data_404(mock_requests_get):
    #simulate a 404 error from the API
    mock_response = Mock(status_code=404)
    mock_requests_get.return_value = mock_response

    #ensure the function returns 404
    assert fetch_data.get_repo_data("bad", "repo") == 404

#test: get_contributor_data handling a 204 no content response
def test_get_contributor_data_204(mock_requests_get):
    #simulate a 204 no content response
    mock_response = Mock(status_code=204)
    mock_requests_get.return_value = mock_response

    #ensure the function returns 204
    assert fetch_data.get_contributor_data("test", "sample") == 204

#test: get_commit_data handling a 409 conflict response
def test_get_commit_data_409(mock_requests_get):
    #simulate a 409 conflict response
    mock_response = Mock(status_code=409)
    mock_requests_get.return_value = mock_response

    #ensure the function returns 409
    assert fetch_data.get_commit_data("test", "sample") == 409

#test: get_repo_data handling a general request exception
def test_get_repo_data_exception(mock_requests_get):
    #simulate a network or request error
    mock_requests_get.side_effect = requests.exceptions.RequestException("connection error")

    #ensure the function returns None on exception
    result = fetch_data.get_repo_data("test", "sample")
    assert result is None