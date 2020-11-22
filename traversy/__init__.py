from mo_dots import Data, FlatList, DataObject
from dotty_dict import Dotty
import copy
from datafunc import listlike, dictlike
from typing import Dict, List, Literal, Tuple, Union, Any, Callable, Set, Optional, AnyStr


def func(var):
	return var


def return_all(*args, **kwargs):
	return True


def traverse(data: Union[Dict, Data, DataObject, Dotty, List, FlatList],
             filter_func: Callable = return_all, node_path: Optional[List] = None,
             parent_node: Optional[Any] = None, output_formatter: Callable = func,
             val_transformer: Callable = func, **kwargs):
	"""
	Traverse deep data structures such as dict, mo-dots, and dotty_dict. Supports
	nested lists & data.
		:param data: Data dict or object to traverse
		:param filter_func: Callback function which returns a boolean filter.
		:param node_path: Path to start from.
		:param parent_node: Parent of starting node.
		:param output_formatter: Function applied to entire return dict.
		:param val_transformer: Apply func to yielded return val.
		:param kwargs: All extra keyword args are sent to the filter_func()
		:return: Yields an iterator result-set for each traversable key/value pair
					and/or list item to an infinite depth.
	"""
	node_path = [] if node_path is None else node_path
	path: AnyStr = '.'.join([str(n) for n in node_path])
	key: AnyStr = node_path[-1:][0] if node_path is not None and len(node_path[-1:]) > 0 else ''
	if dictlike(data):
		for x in data.keys():
			local_path: List = node_path[:]
			local_path.append(x)
			yield from traverse(data[x], filter_func=filter_func, node_path=local_path,
			                    parent_node=data, output_formatter=output_formatter,
			                    val_transformer=val_transformer, **kwargs)
	elif listlike(data):
		for x, y in enumerate(data):
			local_path: List = node_path[:]
			local_path.append(x)
			yield from traverse(data[x], filter_func=filter_func, node_path=local_path,
			                    parent_node=data, output_formatter=output_formatter,
			                    val_transformer=val_transformer, **kwargs)
	elif filter_func(key, data, node_path, **kwargs):
		yield output_formatter({'key': key, 'value': val_transformer(data), 'node_path': node_path,
		                        'path': path, 'filter_func': filter_func.__name__,
		                        'filter_args': (data, kwargs), 'parent_node': parent_node,
		                        'output_formatter': output_formatter.__name__})
