"""
:Author: Joshua Rose
:Version: 2.0.0 of 2023/05/28
:License: `Apache 2.0 <https://gh-syn.github.io/urban-cli/license.html>`_
:File: request.py
"""

from typing import Literal

from loguru import logger
from typing import Literal, Optional
from definition import Definition
import requests


class Request:
    """Represents a request for a word"""

    def __init__(self, word: str):
        """
        If a word is not given, a random one is provided.

        :param word: the word to query for (optional)
        """

        self.url = f"https://api.urbandictionary.com/v0/define?term={word}"

    def search(self) -> dict:
        """
        :returns: a dict of definitions
        """

        data = requests.get(self.url).json()
        definitions = [Definition(**item) for item in data["list"]]
        self.definitions = definitions

        return definitions
