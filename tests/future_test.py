import requests


def test_specific_repo_exist():
    r = requests.get(
        url="https://api.github.com/search/repositories",
        headers={"accept": "application/vnd.github+json"},
        params={"q": "talend-eng-II"},
    )
    r.raise_for_status()

    body = r.json()

    assert body["total_count"] == 1
