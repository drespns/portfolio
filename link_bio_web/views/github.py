import requests
import reflex as rx


class GithubState(rx.State):

    """
    https://api.github.com/users/drespns/followers:

    [
        {
            "login": "juanmabv",
            "id": 79248282,
            "node_id": "MDQ6VXNlcjc5MjQ4Mjgy",
            "avatar_url": "https://avatars.githubusercontent.com/u/79248282?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/juanmabv",
            "html_url": "https://github.com/juanmabv",
            "followers_url": "https://api.github.com/users/juanmabv/followers",
            "following_url": "https://api.github.com/users/juanmabv/following{/other_user}",
            "gists_url": "https://api.github.com/users/juanmabv/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/juanmabv/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/juanmabv/subscriptions",
            "organizations_url": "https://api.github.com/users/juanmabv/orgs",
            "repos_url": "https://api.github.com/users/juanmabv/repos",
            "events_url": "https://api.github.com/users/juanmabv/events{/privacy}",
            "received_events_url": "https://api.github.com/users/juanmabv/received_events",
            "type": "User",
            "site_admin": false
        },
        {
            "login": "PexerMath",
            "id": 158829661,
            "node_id": "U_kgDOCXeMXQ",
            "avatar_url": "https://avatars.githubusercontent.com/u/158829661?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/PexerMath",
            "html_url": "https://github.com/PexerMath",
            "followers_url": "https://api.github.com/users/PexerMath/followers",
            "following_url": "https://api.github.com/users/PexerMath/following{/other_user}",
            "gists_url": "https://api.github.com/users/PexerMath/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/PexerMath/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/PexerMath/subscriptions",
            "organizations_url": "https://api.github.com/users/PexerMath/orgs",
            "repos_url": "https://api.github.com/users/PexerMath/repos",
            "events_url": "https://api.github.com/users/PexerMath/events{/privacy}",
            "received_events_url": "https://api.github.com/users/PexerMath/received_events",
            "type": "User",
            "site_admin": false
        },
        {
            "login": "juanma-sao",
            "id": 169241003,
            "node_id": "U_kgDOChZpqw",
            "avatar_url": "https://avatars.githubusercontent.com/u/169241003?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/juanma-sao",
            "html_url": "https://github.com/juanma-sao",
            "followers_url": "https://api.github.com/users/juanma-sao/followers",
            "following_url": "https://api.github.com/users/juanma-sao/following{/other_user}",
            "gists_url": "https://api.github.com/users/juanma-sao/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/juanma-sao/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/juanma-sao/subscriptions",
            "organizations_url": "https://api.github.com/users/juanma-sao/orgs",
            "repos_url": "https://api.github.com/users/juanma-sao/repos",
            "events_url": "https://api.github.com/users/juanma-sao/events{/privacy}",
            "received_events_url": "https://api.github.com/users/juanma-sao/received_events",
            "type": "User",
            "site_admin": false
        }
        ]
    """
    url: str = "https://github.com/reflex-dev"
    profile_image: str = (
        "https://avatars.githubusercontent.com/u/104714959"
    )

    def set_profile(self, username: str):
        if username == "":
            return
        github_data = requests.get(
            f"https://api.github.com/users/{username}"
        ).json()
        self.url = github_data["url"]
        self.profile_image = github_data["avatar_url"]


def index():
    return rx.hstack(
        rx.link(
            rx.avatar(src=GithubState.profile_image),
            href=GithubState.url,
        ),
        rx.input(
            placeholder="Your Github username",
            on_blur=GithubState.set_profile,
        ),
    )