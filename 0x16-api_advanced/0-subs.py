#!/usr/bin/python3
"""
This module contains the function number_of_subscribers
that queries the Reddit API and returns the number of
subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of
    subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the
        subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "python:subreddit.subscriber.counter:v1.0 (by u/your_username)"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code != 200:
            return 0
        
        data = response.json()
        return data["data"]["subscribers"]
    
    except Exception:
        return 0
