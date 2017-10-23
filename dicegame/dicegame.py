
import random


def play_game():
	score = 0

	for turn in range(1, 4):
		turn_score = 0
		print()
		print('Turn {} of 3'.format(turn))
		print('your current score : {} points'.format(score))
		print()
		dice_remain = 6

		while True:
			print('Rolling {} dice'.format(dice_remain))
			rand_list = [random.randint(1, 6) for _ in range(dice_remain)]
			rand_list.sort()

			print(rand_list)
			match_flag = False
			for num in range(1, 7):
				match = rand_list.count(num)

				if match >= 2:
					match_flag = True
					tmp_score = match * num
					print(num, 'x', match, '=', tmp_score, 'points')
					if 'yes' in input('set aside these dice, yes or no? '):
						print('you set aside {} points'.format(tmp_score))
						print()
						turn_score += tmp_score
						dice_remain -= match
					else:
						print()

			if not match_flag:
				print('no match')
				if turn_score > 0:
					print('you lost {} points'.format(turn_score))
				break

			if turn_score > 0:
				if dice_remain == 1:
					score += turn_score
					print('Only one dice left. Go to the next turn')
					print('you got {} points this turn'.format(turn_score))
					break
				elif dice_remain == 0:
					score += turn_score
					print('No dice left. Go to the next turn')
					print('you got {} points this turn'.format(turn_score))
					break

				print('{} dice remaining and {} points on the line'.format(dice_remain, turn_score))
				if 'end' in input('roll or end? '):
					score += turn_score
					print('you got {} points this turn'.format(turn_score))
					break
				else:
					print()

		print('your total score :', score)

	print()
	print('Game Over')
	return score


def check_score(score):
	print('your final score : {} points'.format(score))
	if score >= 60:
		print('Excellent score, well done!')

	elif score >= 50:
		print('Great score!')

	elif score >= 40:
		print('Good score!')
	else:
		print('')


if __name__ == '__main__':
	score = play_game()
	check_score(score)
