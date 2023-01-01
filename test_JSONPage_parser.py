import pytest

from render_engine_json.parsers import JSONPageParser


def test_JSONPageParser_parses_content_no_slug():
    CONTENT = '{ "title": "Hello", "content": "Hello World" }'
    assert JSONPageParser().parse_content(CONTENT) == (
        {"title": "Hello"},
        "Hello World",
    )


def test_JSONPageParser_parses_content_with_slug():
    CONTENT = '{ "slug": { "title": "Hello", "content": "Hello World" } }'
    assert JSONPageParser().parse_content(CONTENT) == (
        {"slug": "slug", "title": "Hello"},
        "Hello World",
    )
