import json

from render_engine.page import Page

from render_engine_json.parsers import JSONPageParser


def test_JSONPageParser_parses_content_no_slug():
    CONTENT = '{ "title": "Hello", "content": "Hello World" }'
    assert JSONPageParser().parse_content(CONTENT) == (
        {"title": "Hello"},
        "Hello World",
    )


def test_sort_options():
    
    def sorter(data):
        return sorted(data, key=lambda x: x["order"])

    class TestPage(Page):
        data =  [{"name": "Second", "order": 1}, {"name": "First", "order": 0}, {"name": "Third", "order": 2}]
        content = "Test"
        Parser = JSONPageParser
        parser_extras = {"modify": sorter}

    JSONPageParser.parse(TestPage.content, TestPage)
    assert TestPage.data[0]["name"] == "First"
    assert TestPage.data[1]["name"] == "Second"
    assert TestPage.data[2]["name"] == "Third"
