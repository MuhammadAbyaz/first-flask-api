import requests

from models import GithubRepo
from exceptions import GitHubApiError


GITHUB_API_URL = "https://api.github.com/search/repositories"


def create_query(language, min_stars):
    query = " ".join(f"language:{language.strip()}" for language in language)
    query = query + f" stars:>{min_stars}"
    return query


def repos_with_most_stars(language, min_stars=40000, sort="stars", order="desc"):
    query = create_query(language=language, min_stars=min_stars)
    parameters = {"q": query, "sort": sort, "order": order}
    response = requests.get(GITHUB_API_URL, params=parameters)

    if response.status_code != 200:
        raise GitHubApiError(response.status_code)

    response_json = response.json()
    items = response_json["items"]
    return [GithubRepo(item["name"], item["language"], item["stargazers_count"]) for item in items]
