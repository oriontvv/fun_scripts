
class Integer:
	"""
	Only for class variables!
	If a descriptor is accessed as a class variable, 
	the instance argument is set to None.
	"""

	def __init__(self, name):
		self._name = name

	def __get__(self, instance, cls):
		if instance is None:
			return self
		return instance.__dict__[self._name]

	def __set__(self, instance, value):
		if not isinstance(value, int):
			raise TypeError('Expected an int')
		instance.__dict__[self._name] = value

	def __delete__(self, instance):
		del instance.__dict__[self._name]


class Typed:
	def __init__(self, name, expected_type):
		self._name = name
		self._expected_type = expected_type

	def __get__(self, instance, cls):
		if instance is None:
			return self
		return instance.__dict__[self._name]

	def __set__(self, instance, value):
		if not isinstance(value, self._expected_type):
			raise TypeError('Expected {}'.format(self._expected_type))
		instance.__dict__[self._name] = value

	def __delete__(self, instance):
		del instance.__dict__[self._name]


# class decorator that applies it to selected attributes
# just an example. do not use in real life :)
def type_assert(**kwargs):
	def decorator(cls):
		for name, expected_type in kwargs.items():
			setattr(cls, name, Typed(name, expected_type))
		return cls
	return decorator
