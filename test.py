import ast


with open('test.txt', 'r', encoding='utf-8') as f:
	list_str = f.read()


l = ast.literal_eval(list_str)

for i, x in enumerate(l): print(i, x)