

def main():
	filter_dict = {}
	with open('sample.csv', 'r', encoding='utf-8') as f:
		for line in f:
			key, val = line.strip().split(',')
			if key not in filter_dict:
				filter_dict[key] = val

	print(filter_dict['james'])


if __name__ == '__main__':
	main()
