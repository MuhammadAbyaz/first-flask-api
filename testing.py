from exceptions import GitHubApiError
exception = GitHubApiError(status_code=500)
print(repr(exception))
