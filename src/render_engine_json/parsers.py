import json
import logging

from render_engine_parser import BasePageParser


def base_parse(body: dict[str, any]) -> tuple[dict[str, any], any]:
    """
    parse content and attributes from content
    >>> base_parse({"title": "Hello", "content": "Hello World"})
    >>> ({'title': 'Hello'}, 'Hello World')
    """
    return body, body


class JSONPageParser(BasePageParser):
    """Parser for JSON content."""

    @staticmethod
    def parse_content_path(content_path: str) -> dict[str, any]:
        """
        Fetches content from a content_path and set attributes.
        """
        with open(content_path, "rb") as json_file:
            return JSONPageParser.parse_content(json_file.read())

    @staticmethod
    def parse_content(content: str) -> tuple[dict[str, any], str]:
        """
        Fetching content and atttributes from content.

        If the parsed_content is a dictionary, then the attributes are fetched from the dictionary
          and the content is fetched from the "content" key.
        If the parsed_content is a list, each item is passed as a dictionary into the `data` attribute.
        """

        body = json.loads(content)

        if isinstance(body, dict):
            logging.debug("JSON Content Identified as a dictionary.")
            return base_parse(body)

        if isinstance(body, list):
            logging.debug("JSON Content Identified as a list.")
            return {"data": body}, ""

        raise TypeError(
            "The content should be a stringified dictionary or list.\n \
            Perhaps you meant to stringify the content?"
        )

    @staticmethod
    def parse(content, extras) -> str:
        return content
