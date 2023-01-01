# Render Engine JSON

JSON Parser and Collection Module for Render Engine

## Installation

```bash
pip install render_engine_json
```

## Usage

The `render-engine-json` extends render-engine to allow you to build pages and collections using JSON. 

The `JSONPageParser` class can be used to parse a single JSON page and the `JSONCollection` class can be used to parse a single collection of JSON pages.

> **NOTE**
> The `JSONCollection` class is designed to work with a single JSON file that contains an array of JSON Objects or a JSON Hash where the keys are the slugs. If you want to work with multiple JSON files you can use a regular `Collection` and the `JSONPageParser` as the parser.

### Single JSON Page Entry

To create a json entry you will need the `JSONPageParser` class as the Parser for your `Page` Object.

You can pass the page a json string or a json file path.

#### As a string

```python

from render_engine import Page, Site
from render_engine_json import JSONPageParser

site = Site()

json_page = """
{
    "title": "My JSON Page",
    "content": "This is my json page"
}
"""

@site.page
class JSONStringPage(Page):
    parser = JSONPageParser
    content = json_page

```

#### As a file

```python

@site.page
class JSONFilePage(Page):
    parser = JSONPageParser
    content = "path/to/json/file.json"

```

### JSON Collection

To create a JSON collection you will need the `JSONCollection` Object.

You can pass the collection a json string or a json file path.

#### As a string

```python
from render_engine import Site, Collection
from render_engine_json import JSONCollection, JSONPageParser

site = Site()

json_collection = """
[
    {
        "title": "My JSON Page",
        "content": "This is my json page"
    },
    {
        "title": "My JSON Page 2",
        "content": "This is my json page 2"
    }
]
"""

@site.collection
class JSONStringCollection(Collection):
    parser = JSONPageParser
    content = json_collection

```


```
