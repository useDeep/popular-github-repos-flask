class github_repo:
    def __init__(self, name, language, num_stars) -> None:
        self.name= name
        self.language= language
        self.num_stars= num_stars
        pass

    def __str__(self) -> str:
        return f"-> {self.name} is a {self.language} repo with {self.num_stars} stars."
        pass
    def __repr__(self) -> str:
        return f"Github repo ({self.name}, {self.language}, {self.num_stars}"     
        pass