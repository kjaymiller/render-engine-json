import pytest

from render_engine_json import JSONCollection, JSONPageParser


def test_JSONCollection_pases_JSONPageParse_to_Page():
    CONTENT = '[{ "title": "Hello", "content": "Hello World" }]'

    class TestCollection(JSONCollection):
        content = CONTENT

    page = next(TestCollection().pages)
    assert page.Parser == JSONPageParser


def test_JSONCollection_parses_content_no_slug():
    CONTENT = '[{ "title": "Hello", "content": "Hello World" }]'

    class TestCollection(JSONCollection):
        content = CONTENT

    page = next(TestCollection().pages)

    # assert page.title == "Hello"
    assert page.content == "Hello World"
