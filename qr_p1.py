# coding: utf-8 -*-

#################################
# Qualification Round 2019
# Problem 1
#    Foregone Solution (6pts, 10pts, 1pts)
#################################
'''
Problem

Someone just won the Code Jam lottery, and we owe them N jamcoins! However, when we tried to print out an oversized check, we encountered a problem. The value of N, which is an integer, includes at least one digit that is a 4... and the 4 key on the keyboard of our oversized check printer is broken. 
Fortunately, we have a workaround: we will send our winner two checks for positive integer amounts A and B, such that neither A nor B contains any digit that is a 4, and A + B = N. Please help us find any pair of values A and B that satisfy these conditions. 

Input

The first line of the input gives the number of test cases, T. T test cases follow; each consists of one line with an integer N. 

Output

For each test case, output one line containing Case #x: A B, where x is the test case number (starting from 1), and A and B are positive integers as described above. 
It is guaranteed that at least one solution exists. If there are multiple solutions, you may output any one of them. (See "What if a test case has multiple correct solutions?" in the Competing section of the FAQ. This information about multiple solutions will not be explicitly stated in the remainder of the 2019 contest.) 

Limits

1 ≤ T ≤ 100.
Time limit: 10 seconds per test set.
Memory limit: 1GB.
At least one of the digits of N is a 4.
Test set 1 (Visible)
1 < N < 105.
Test set 2 (Visible)
1 < N < 109.
Solving the first two test sets for this problem should get you a long way toward advancing. The third test set is worth only 1 extra point, for extra fun and bragging rights! 
Test set 3 (Hidden)
1 < N < 10100.
Sample

Input	Output 
  
3	Case #1: 2 2
4	Case #2: 852 88
940	Case #3: 667 3777
4444
  
In Sample Case #1, notice that A and B can be the same. The only other possible answers are 1 3 and 3 1. 
'''

class CONST:
	CHARGE = 'C'
	SHOOT = 'S'
	IMPOSSIBLE = 'IMPOSSIBLE'

def read_int():
	return int(input())

def read_int_str():
	raw_two_int = input()
	raw_int_list = raw_two_int.split()
	return int(raw_int_list[0]), raw_int_list[1]

def print_it_now(case_n, hack_num=None):
	if hack_num is None:
		ans = 'Case #%s: %s' % (case_n, CONST.IMPOSSIBLE)
	else:
		ans = 'Case #%s: %d' % (case_n, hack_num)
	# ensure stdout flush
	print(ans, flush=True)

def cal_damage(instruction_chars):
	damage = 0
	strength = 1

	pos_last_movable_c = -1
	last_c = -1
	for i, ch in enumerate(instruction_chars):
		if CONST.CHARGE == ch:
			last_c = i
			strength *= 2
		elif CONST.SHOOT == ch:
			pos_last_movable_c = last_c
			damage += strength
	#print("#DEBUG damage = %d" % damage)
	#print("#DEBUG pos_last_movable_c = %d" % pos_last_movable_c)
	return damage, pos_last_movable_c

def hack_it(swap_pos, instruction_chars):
	return instruction_chars[:swap_pos] + \
		instruction_chars[swap_pos+1] + \
		instruction_chars[swap_pos] + \
		instruction_chars[(swap_pos+2):]

def play_a_round(case_n):
	max_demage, instructions = read_int_str()

	#print("#DEBUG input: %d %s" % (max_demage, instructions))

	# Fail at the beginning
	if instructions.count(CONST.SHOOT) > max_demage:
		print_it_now(case_n, None)
		return

	hack_count = 0
	while True:
		damage, pos_c = cal_damage(instructions)
		# We made it!!!
		if damage <= max_demage:
			print_it_now(case_n, hack_count)
			break

		# We failed!
		if pos_c == -1:
			print_it_now(case_n, None)
			break

		# Now we hack
		hack_count += 1
		instructions = hack_it(pos_c, instructions)
		#print("#DEBUG instructions = %s" % instructions)


if '__main__' == __name__:
	# Read number of test cases
	t = read_int()

	# Count up test cases
	t_count = 0
	while t_count < t:
		t_count += 1

		play_a_round(t_count)

'''
Input
	6
	1 CS
	2 CS
	1 SS
	6 SCCSSC
	2 CC
	3 CSCSS

Output
	Case #1: 1
	Case #2: 0
	Case #3: IMPOSSIBLE
	Case #4: 2
	Case #5: 0
	Case #6: 5
'''
