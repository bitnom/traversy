# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['traversy']

package_data = \
{'': ['*']}

install_requires = \
['dotty-dict>=1.3.0,<2.0.0',
 'mo-dots>=3.135.20303,<4.0.0',
 'switch>=1.1.0,<2.0.0']

setup_kwargs = {
    'name': 'traversy',
    'version': '0.1.0',
    'description': 'Fast data traversal & manipulation tools.',
    'long_description': '# traversy\n\nFast data traversal & manipulation tools for Python.',
    'author': 'Tom A.',
    'author_email': '14287229+TensorTom@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tensortom/traversy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9.0,<4.0.0',
}


setup(**setup_kwargs)
