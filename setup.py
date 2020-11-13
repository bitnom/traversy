# -*- coding: utf-8 -*-
import sys

if sys.version_info.major >= 3:
    from setuptools import setup
else:
    from distutils.core import setup

packages = \
['traversy']

package_data = \
{'': ['*']}

install_requires = \
['dotty-dict>=1.3.0,<2.0.0', 'mo-dots>=3.135.20303']

setup_kwargs = {
    'name': 'traversy',
    'version': '0.1.1',
    'description': 'Fast data traversal & manipulation tools.',
    'long_description': '# traversy\n\nFast data traversal & manipulation tools for Python.\n\n`traverse()`: \nTraverse deep data structures such as dict, mo-dots, and\ndotty_dict. Supports nested lists & data.\n\n```python\nfrom traversy import traverse, set_output_format\nimport json\n\n\njo = json.loads("""{\n  "2019": {\n    "uat": {\n      "pkey": true,\n      "user": "testval",\n      "testkey": true,\n      "mylist": [\n      {\n        "foo": "bar",\n        "foo2": "bar2"\n      },\n      {\n        "baz": "milk",\n        "bar": "foo"\n      }\n      ]\n    },\n    "dev": {\n      "pkey": true,\n      "testval": "testval",\n      "testval2": true\n    },\n    "test1": [1, 2, "testval"],\n    "test2": [{"one": "foo", "two": "bar", "three": "testval"}]\n  }\n}""")\n\ndef is_eq(key, val, opath, query):\n    return val == query\n\n\nfor node in traverse(jo, is_eq, query="milk"):\n    print("Found", node.key, \':\', node.value)  # baz : milk\n    print("Full path access:", jo[node.path_str])  # "2019.uat.mylist.1.baz"\n```\n\nFor each iteration, traverse() returns a dict or data object of...\n\n```\n{\'key\', \'value\', \'node_path\', \'path_str\', \'filter_func\',\n\'filter_args\': (data, kwargs), \'parent_node\', \'output_formatter\'}\n```\n\nFor more information on these non-built-in data structure (Which are optional\nto use), check out [mo-dots](https://pypi.org/project/mo-dots/) and\n[dotty_dict](https://pypi.org/project/dotty-dict/).\n\nLicense: MIT\n\n\n### Changelog\n\n- **11/13/2020** - Deprecated `set_output_format()` and made package compatible with both Python 2 and Python 3.',
    'author': 'Tom A.',
    'author_email': '14287229+TensorTom@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tensortom/traversy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
