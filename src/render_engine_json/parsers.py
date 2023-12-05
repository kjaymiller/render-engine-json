import json

from render_engine.parsers.base_parsers import BasePageParser


def base_parse(body: dict[str, any]) -> tuple[dict[str, any], str]:
    """
    parse content and attributes from content
    >>> base_parse({"title": "Hello", "content": "Hello World"})
    >>> ({'title': 'Hello'}, 'Hello World')
    """
    content = body.pop("content", None)
    return body, content


def parse_from_slug_entry(
    slug_entry: dict[str, dict[str, any]]
) -> tuple[dict[str, any], str]:
    """
    Fething content and attributes from a slug entry.
    >>> parse_from_slug_entry({"slug": {"content": "Hello World"}})
    >>> ({'slug': 'slug'}, 'Hello World')

    This function expects input to be a dictionary with a single key whose value is a dict.
    """

    attrs, content = base_parse(list(slug_entry.values())[0])
    attrs["slug"] = list(slug_entry.keys())[0]
    return attrs, content


class JSONPageParser(BasePageParser):
    """Parser for JSON content."""

    @staticmethod
    def parse_content_path(content_path: str) -> dict[str, Any]:
        """
        Fetches content from a content_path and set attributes.
        """
        with open(content_path, "rb") as json_file:
            return json.load(json_file)

    @staticmethod
    def parse_content(content: str) -> tuple[dict[str, Any], str]:
        """
        Fetching content and atttributes from content.

        If the parsed_content is a dictionary, then the attributes are fetched from the dictionary
          and the content is fetched from the "content" key.
        If the parsed_content is a list, each item is passed as a dictionary into the `data` attribute.
        """

        body = json.loads(content)

        if isinstance(body, dict):
            return parse_from_slug_entry(body)

        if isinstance(body, list):
            return {"data": body}, ""

        raise TypeError(
            "The content should be a stringified dictionary or list.\n \
            Perhaps you meant to stringify the content?"
        )
