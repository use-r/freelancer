import json
import collections

def main():
	try:
		with open('data.txt', 'r', encoding='utf-8') as f:
			data = json.load(f)
	except Exception as e:
		data = []

	print('Welcome to the Quizle Admin Program')

	while True: 
		print('Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
		val = inputSomething('> ')

		if val == 'a':
			quest = collections.OrderedDict()
			quest['question'] = inputSomething('Enter the question: ')
			ansList = []
			while True:
				ans = inputSomething('Enter a valid answer (enter "q" when done): ')
				if ans == 'q': break
				ansList.append(ans)
			quest['answers'] = ansList
			while True:
				difficulty = inputInt('Enter question difficulty (1-5): ')
				if difficulty >= 1 and difficulty <= 5:
					break
				else:
					print('invalid number .. must be an integer 1-5 ')

				quest['difficulty'] = difficulty
			data.append(quest)
			saveChanges(data)
			print('Question added!')

		elif val == 'l':
			print('Current questions:')
			for i, q in enumerate(data):
				print('{}) {}'.format(str(i), q['question']))

		elif val == 'v':
			if len(data) == 0:
				print('No questions saved')
				continue
			view_idx = inputInt('Question number to view: ')
			try:
				print('Question:' + '\n' + data[view_idx]['question'])
				print('Valid Answers: {}'.format(', '.join(data[view_idx]['answers'])))
				print('Difficulty: {}'.format(data[view_idx]['difficulty']))
			except IndexError:
				print('Invalid index number')

		elif val == 's':
			term = inputSomething('Enter a serach term: ').lower()

			for i, q in enumerate(data):
				if term in q['question'].lower(): print(str(i) + ')', q['question'])

		elif val == 'd':
			if len(data) == 0:
				print('No questions saved')
				continue

			del_idx = inputInt('Question number to delete: ')

			try:
				del data[del_idx]
				print('Question deleted! ')
				saveChanges(data)
			except IndexError:
				print('Invalid index number')

		elif val == 'q':
			print('Goodbye!')
			break
		else:
			print('Invalid choice')

def inputInt(prompt):
	while True:
		try:
			val = int(input(prompt))
			return val
		except ValueError:
			print('Invalid input')
			continue

def inputSomething(prompt):
	while True:
		val = input(prompt).strip()
		if val != '':
			return val
		else:
			print('Invalid input')
			continue

def saveChanges(dataList):
	with open('data.txt', 'w', encoding='utf-8') as f:
		json.dump(dataList, f)

if __name__ == '__main__':
	main()
