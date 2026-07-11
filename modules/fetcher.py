import requests


def fetch_subscription(url: str, timeout: int = 10) -> str:
    """
    获取订阅内容
    """
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.text.strip()
