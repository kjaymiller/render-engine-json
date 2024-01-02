import json

from render_engine.page import Page

from render_engine_json.parsers import JSONPageParser


def test_JSONPageParser_parses_content_no_slug():
    CONTENT = '{ "title": "Hello", "content": "Hello World" }'
    assert JSONPageParser().parse_content(CONTENT) == (
    {
        "title": "Hello",
        "content": "Hello World"
     },
     {
        "title": "Hello",
        "content": "Hello World"
     },
    )


def test_sort_options():
    
    def sorter(data):
        return sorted(data, key=lambda x: x["order"])

    class TestPage(Page):
        content =  [{"name": "Second", "order": 1}, {"name": "First", "order": 0}, {"name": "Third", "order": 2}]
        Parser = JSONPageParser
        parser_extras = {"modify": sorter}

    content = JSONPageParser.parse(TestPage.content, TestPage.parser_extras)
    assert content[0]["name"] == "First"
    assert content[1]["name"] == "Second"
    assert content[2]["name"] == "Third"
