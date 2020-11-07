from mo_dots import from_data, to_data, Data, Null, DataObject, FlatList
from dotty_dict import dotty, Dotty
from switch import Switch

format_output = dict


def traverse(data, filter_func=None, node_path=None, parent_node=None, **kwargs):
	"""
	Traverse deep data structures such as dict, mo-dots, and dotty_dict. Supports
	nested lists & data.
		:param data: Data dict or object to traverse
		:param filter_func: Callback function which returns a boolean filter.
		:param node_path: Path to start from.
		:param parent_node: Parent of starting node.
		:param kwargs: All extra keyword args are sent to the filter_func()
		:return:
	"""
	global format_output
	node_path = [] if node_path is None else node_path
	path_str = '.'.join([str(n) for n in node_path])
	if isinstance(data, dict) or isinstance(data, Data) or isinstance(data, Dotty):
		for x in data.keys():
			local_path = node_path[:]
			local_path.append(x)
			yield from traverse(data[x], filter_func=filter_func, node_path=local_path,
			                    parent_node=data, **kwargs)
	elif isinstance(data, list) or isinstance(data, FlatList):
		for x, y in enumerate(data):
			local_path = node_path[:]
			local_path.append(x)
			yield from traverse(data[x], filter_func=filter_func, node_path=local_path,
			                    parent_node=data, **kwargs)
	elif filter_func is None:
		key = node_path[-1:][0] if len(node_path[-1:]) > 0 else ''
		yield format_output({'key': key, 'value': data, 'node_path': node_path, 'path_str': path_str,
		                     'filter_func': None, 'filter_args': None, 'parent_node': parent_node})
	elif filter_func(node_path[-1:], data, node_path, **kwargs):
		key = node_path[-1:][0] if len(node_path[-1:]) > 0 else ''
		yield format_output({'key': key, 'value': data, 'node_path': node_path, 'path_str': path_str,
		                     'filter_func': filter_func.__name__, 'filter_args': (data, kwargs),
		                     'parent_node': parent_node})


def set_output_format(_output_format=None):
	"""
	Set the output format of subsequent calls to traversy functions.
	:param _output_format: "dict", "mo-dots", or "dotty_dict"
	:return: None
	"""
	global format_output
	with Switch(_output_format) as case:
		if case("mo-dots"):
			format_output = to_data
		if case("dotty_dict"):
			format_output = dotty
		if case.default:
			format_output = dict
