def test_repos_can_be_find(github_api):
    body = github_api.search_repo('talend-eng-II')
    assert body["total_count"] == 1


def test_repos_cannot_be_find(github_api):
    body = github_api.search_repo(';ksjedfihndijfnviuneqroivmoerkmv')
    assert body["total_count"] == 0


def test_repos_spefic_ch_can_be_find(github_api):
    body = github_api.search_repo('***')
    assert body["total_count"] == 0
