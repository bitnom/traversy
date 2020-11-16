from mo_dots import Data, FlatList
from dotty_dict import Dotty
import copy


def func(var):
	return var


def return_all(*args, **kwargs):
	return True


def traverse(data, filter_func=return_all, node_path=None,
             parent_node=None, output_formatter=func,
             val_transformer=func, **kwargs):
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
		:return:
	"""
	node_path = [] if node_path is None else node_path
	path_str = '.'.join([str(n) for n in node_path])
	if isinstance(data, (dict, Data, Dotty)):
		for x in data.keys():
			local_path = node_path[:]
			local_path.append(x)
			yield from traverse(data[x], filter_func=filter_func, node_path=local_path,
			                    parent_node=data, output_formatter=output_formatter,
			                    val_transformer=val_transformer, **kwargs)
	elif isinstance(data, (list, FlatList)):
		for x, y in enumerate(data):
			local_path = node_path[:]
			local_path.append(x)
			yield from traverse(data[x], filter_func=filter_func, node_path=local_path,
			                    parent_node=data, output_formatter=output_formatter,
			                    val_transformer=val_transformer, **kwargs)
	elif filter_func(node_path[-1:], data, node_path, **kwargs):
		key = node_path[-1:][0] if len(node_path[-1:]) > 0 else ''
		yield output_formatter({'key': key, 'value': val_transformer(data), 'node_path': node_path,
		                        'path_str': path_str, 'filter_func': filter_func.__name__,
		                        'filter_args': (data, kwargs), 'parent_node': parent_node,
		                        'output_formatter': output_formatter.__name__})


def duplicate(data):
	"""
	Convenience method for copy.deepcopy()
	:param data: Any dict, mo-dots, or dotty object.
	:return: A deep copy of the data.
	"""
	return copy.deepcopy(data)


def add_sibling(data, node_path, new_key, new_data, _i=0):
	"""
	Traversal-safe method to add a siblings data node.
	:param data: The data object you're traversing.
	:param node_path: List of path segments pointing to the node you're creating a
			sibling of. Same as node_path of traverse()
	:param new_key: The sibling key to create.
	:param new_data: The new data to be stored at the key.
	"""
	if _i < len(node_path) - 1:
		return add_sibling(data[node_path[_i]], node_path, new_key, new_data, _i + 1)
	else:
		data[new_key] = new_data



