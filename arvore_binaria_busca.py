# Guilherme Azambuja — 149 429


class Tree:

	def __init__(self, info: int):
		self.rs: Tree
		self.ls: Tree

		self.info = info
		self.rs = None
		self.ls = None

	def __str__(self):
		if self.ls:
			li = self.ls.info
		else:
			li = '---'
		if self.rs:
			ri = self.rs.info
		else:
			ri = '---'
		return f'{self.info} [{li} | {ri}]'

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
		parent, side = self.searchParent(target)
		if target:
			if target.ls is None and target.rs is None:
				setattr(parent, side, None)
			elif target.ls and not target.rs:
				setattr(parent, side, target.ls)
			elif target.rs and not target.ls:
				setattr(parent, side, target.rs)
			else:
				aux = target.ls
				while aux.rs:
					aux = aux.rs
				value = aux.info
				self.remove(value)
				target.info = value
		else:
			return None

	def searchParent(self, nodo):
		if nodo == self:
			return None
		else:
			if nodo.info > self.info:
				if nodo is self.rs:
					return self, 'rs'
				else:
					return self.rs.searchParent(nodo)
			else:
				if nodo is self.ls:
					return self, 'ls'
				else:
					return self.ls.searchParent(nodo)

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
