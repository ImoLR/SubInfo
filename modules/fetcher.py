import requests


class FetchError(Exception):
    """订阅获取异常"""
    pass


def fetch_subscription(url: str, timeout: int = 10) -> str:
    try:
        response = requests.get(
            url,
            timeout=timeout,
            headers={
                "User-Agent": "SubInfo/0.1"
            }
        )
        response.raise_for_status()
        return response.text.strip()

    except requests.RequestException as e:
        raise FetchError(str(e))
