from arvore_binaria_busca import Tree

nodos = list()

arv = Tree(200)
nodos.append(arv)
nodos.append(arv.insert(100))
nodos.append(arv.insert(150))
nodos.append(arv.insert(80))
nodos.append(arv.insert(300))
nodos.append(arv.insert(250))
nodos.append(arv.insert(400))
nodos.append(arv.insert(220))
nodos.append(arv.insert(270))
nodos.append(arv.insert(350))
nodos.append(arv.insert(500))
nodos.append(arv.insert(260))
nodos.append(arv.insert(255))
nodos.append(arv.insert(265))

arv.remove(400)

for n in nodos:
	print(n)
