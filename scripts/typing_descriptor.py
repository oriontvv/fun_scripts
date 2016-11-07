
class Integer:
	def __init__(self, name):
		self.name = name

	def __get__(self, instance, cls):
		if instance is None:
			return self
		return instance.__dict__[self.name]

	def __set__(self, instance, value):
		if not isinstance(value, int):
			raise TypeError('Expected an int')
		instance.__dict__[self.name] = value

	def __delete__(self, instance):
		del instance.__dict__[self.name]
