# Guilherme Azambuja — 149 429


class Tree:

	def __init__(self, info: int):
		self.rs: Tree
		self.ls: Tree
		self.h: int

		self.info = info
		self.rs = None
		self.ls = None
		self.h = 0

	def __str__(self):
		return str(self.info)

	def insert(self, info: int):
		if info > self.info:
			if self.rs is None:
				self.rs = Tree(info)
				return self.rs
			else:
				return self.rs.insert(info)
		elif info < self.info:
			if self.ls is None:
				self.ls = Tree(info)
				return self.ls
			else:
				return self.ls.insert(info)
		else:
			return None  # Info já existe na árvore

	def remove(self, info: int):
		target = self.search(info)
		if target is not None:
			pass
		else:
			return None

	def search(self, info: int):
		if info == self.info:
			return self
		else:
			if info > self.info:
				if self.rs is not None:
					return self.rs.search(info)
				else:
					return None
			else:
				if self.ls is not None:
					return self.ls.search(info)
				else:
					return None


teste = Tree(4)
teste.insert(7)
teste.insert(5)
teste.insert(9)
teste.insert(1)
teste.insert(3)
teste.insert(10)
teste.insert(14)
teste.insert(18)
teste.insert(15)
teste.insert(13)
teste.remove(2)
print(teste)
