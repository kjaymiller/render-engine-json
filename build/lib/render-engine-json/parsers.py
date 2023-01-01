import json
from typing import Any, Type

import slugify
from render_engine.parsers import BasePageParser


def base_parse(body: dict[str, Any]) -> tuple[dict[str, Any], str]:
    """
    parse content and attributes from content
    >>> base_parse({"title": "Hello", "content": "Hello World"})
    >>> ({'title': 'Hello'}, 'Hello World')
    """
    content = body.pop("content", None)
    return body, content


def parse_from_slug_entry(
    slug_entry: dict[str, dict[str, Any]]
) -> tuple[dict[str, Any], str]:
    """
    Fething content and attributes from a slug entry.
    >>> parse_from_slug_entry({"slug": {"content": "Hello World"}})
    >>> ({'slug': 'slug'}, 'Hello World')

    This function expects input to be a dictionary with a single key whose value is a dict.
    """

    attrs, content = base_parse(slug_entry.values()[0])
    attrs["slug"] = slug_entry.keys()[0]
    return attrs, content


class JSONPageParser(BasePageParser):
    """Parser for JSON content."""

    @staticmethod
    def parse_content_path(content_path):
        """Fething content from a content_path and set attributes."""
        with open(content_path, "rb") as json_file:
            return json.load(json_file)

    @staticmethod
    def parse_content(content: str) -> tuple[dict[str, Any], str]:
        """Fething content and atttributes from content"""

        body = json.loads(content)
        if len(body.keys()) == 1 and isinstance(body.values()[0], dict):
            return parse_from_slug_entry(body)

        return base_parse(body)
