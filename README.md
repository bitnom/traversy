# traversy

Fast data traversal & manipulation tools for Python.

`traverse()`: 
Traverse deep data structures such as dict, mo-dots, and
dotty_dict. Supports nested lists & data.

```python
from traversy import traverse, set_output_format
import json


jo = json.loads("""{
  "2019": {
    "uat": {
      "pkey": true,
      "user": "testval",
      "testkey": true,
      "mylist": [
      {
        "foo": "bar",
        "foo2": "bar2"
      },
      {
        "baz": "milk",
        "bar": "foo"
      }
      ]
    },
    "dev": {
      "pkey": true,
      "testval": "testval",
      "testval2": true
    },
    "test1": [1, 2, "testval"],
    "test2": [{"one": "foo", "two": "bar", "three": "testval"}]
  }
}""")

def is_eq(key, val, opath, query):
    return val == query

set_output_format('mo-dots')  # Can be dict (Default), mo-dots, or dotty_dict

for node in traverse(jo, is_eq, query="milk"):
    print("Found", node.key, ':', node.value)  # baz : milk
    print("Full path access:", jo[node.path_str])  # "2019.uat.mylist.1.baz"
```

For each iteration, traverse() returns a dict or data object of...

```
{'key', 'value', 'node_path', 'path_str', 'filter_func',
'filter_args': (data, kwargs), 'parent_node'}
```

For more information on these non-built-in data structure (Which are optional
to use), check out [mo-dots](https://pypi.org/project/mo-dots/) and
[dotty_dict](https://pypi.org/project/dotty-dict/).

License: MIT
