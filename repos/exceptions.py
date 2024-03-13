class github_api_exception(Exception):
    def __init__(self, status_code) -> None:
        if status_code== 404:
            message= "API limit exceeded. Try after a while..."
        else:
            message= f"The http status code: {status_code}"

        super().__init__("Error with the GitHub API: ", message)
        pass
