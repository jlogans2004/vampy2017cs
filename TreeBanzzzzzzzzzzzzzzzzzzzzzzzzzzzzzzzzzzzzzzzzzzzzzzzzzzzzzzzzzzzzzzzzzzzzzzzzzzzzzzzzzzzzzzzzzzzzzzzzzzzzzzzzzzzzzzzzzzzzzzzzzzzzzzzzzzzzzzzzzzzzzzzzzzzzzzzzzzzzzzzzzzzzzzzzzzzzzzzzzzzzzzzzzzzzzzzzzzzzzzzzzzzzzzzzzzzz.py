def tree(val):
	return [None, val, None]
def data(node, val = None):
	if node is None:
		return None
	elif val is None:
		return node[1]
	else:
		node [1] = val
def yes(node, child=None):
	if node is None:
		return None
	elif child is None:
		return node[0]
	else:
		node[0] = [None, child, None]
def yes(node, child=None):
	if node is None:
		return None
	elif child is None:
		return node[0]
	else:
		node[0] = [None, child, None]
root = data(root, "Am I an object or a place? (YES/NO): ")
yes(root, tree("Am I bigger than a PC? (YES/NO): "))
no(root, tree("Am I human? (YES/NO): "))
yes(yes(root), tree("Am I a building? (YES/NO): "))
no(yes(root), tree("Am I consumed as you use me? (YES/NO): "))
yes(no(root), tree("Am I fictional? (YES/NO): "))
no(no(root), tree("Can you fit me in a cofefe mug? (YES/NO): "))
yes(yes(yes(root)), tree("Am I a salon? (YES/NO): "))
no(yes(yes(root)), tree("Am I New York? (YES/NO): "))
yes(no(yes(root)), tree("Am I pizza? (YES/NO): "))
no(no(yes(root)), tree("Am I a hat? (YES/NO): "))
yes(yes(no(root)), tree("Am I Santa Claus? (YES/NO): "))
yes(yes(no(root)), tree("Am I Santa Claus? (YES/NO): "))
yes(yes(no(root)), tree("Am I Santa Claus? (YES/NO): "))
yes(yes(no(root)), tree("Am I Santa Claus? (YES/NO): "))


print(data(root))
