

filter_dict = {}

with open('sample.csv', 'r', encoding='utf-8') as f:
	for line in f:
		info, val = line.strip().split(',')
		if not info in filter_dict: filter_dict[info] = val



print(filter_dict['james'])