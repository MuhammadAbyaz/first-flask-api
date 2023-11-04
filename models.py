class GithubRepo:
    # used to represent a single github repo
    def __init__(self, name, language, number_of_stars):
        self.name = name
        self.language = language
        self.number_of_stars = number_of_stars

    def __str__(self) -> str:
        return f"-> {self.name} is a {self.language} repo with {self.number_of_stars} stars"

    def __repr__(self):
        return f"GithubRepo({self.name}, {self.language}, {self.number_of_stars})"
