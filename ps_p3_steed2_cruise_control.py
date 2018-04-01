# coding: utf-8 -*-

#################################
# Practice Session 2018
# Problem 2
#   Steed 2: Cruise Control
#################################
'''
Problem

Annie is a bus driver with a high-stress job. She tried to unwind by going on a Caribbean cruise, but that also turned out to be stressful, so she has recently taken up horseback riding.

Today, Annie is riding her horse to the east along a long and narrow one-way road that runs west to east. She is currently at kilometer 0 of the road, and her destination is at kilometer D; kilometers along the road are numbered from west to east.

There are N other horses traveling east on the same road; all of them will go on traveling forever, and all of them are currently between Annie's horse and her destination. The i-th of these horses is initially at kilometer Ki and is traveling at its maximum speed of Si kilometers per hour.

Horses are very polite, and a horse H1 will not pass (move ahead of) another horse H2 that started off ahead of H1. (Two or more horses can share the same position for any amount of time; you may consider the horses to be single points.) Horses (other than Annie's) travel at their maximum speeds, except that whenever a horse H1 catches up to another slower horse H2, H1 reduces its speed to match the speed of H2.

Annie's horse, on the other hand, does not have a maximum speed and can travel at any speed that Annie chooses, as long as it does not pass another horse. To ensure a smooth ride for her and her horse, Annie wants to choose a single constant "cruise control" speed for her horse for the entire trip, from her current position to the destination, such that her horse will not pass any other horses. What is the maximum such speed that she can choose?
Input

The first line of the input gives the number of test cases, T; T test cases follow. Each test case begins with two integers D and N: the destination position of all of the horses (in kilometers) and the number of other horses on the road. Then, N lines follow. The i-th of those lines has two integers Ki and Si: the initial position (in kilometers) and maximum speed (in kilometers per hour) of the i-th of the other horses on the road.
Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum constant speed (in kilometers per hour) that Annie can use without colliding with other horses. y will be considered correct if it is within an absolute or relative error of 10-6 of the correct answer. See the FAQ for an explanation of what that means, and what formats of real numbers we accept.
Limits

1 ≤ T ≤ 100.
0 < Ki < D ≤ 109, for all i.
Ki ≠ Kj, for all i ≠ j. (No two horses start in the same position.)
1 ≤ Si ≤ 10000.
Time limit: 10 seconds per test set.
Memory limit: 1GB.
Test set 1 (Visible)

1 ≤ N ≤ 2.
Test set 2 (Hidden)

1 ≤ N ≤ 1000.
Sample

Input
  	
Output
 

3
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10

	

Case #1: 101.000000
Case #2: 100.000000
Case #3: 33.333333

In Sample Case #1, there is one other (very slow!) horse on the road; it will reach Annie's destination after 25 hours. Anything faster than 101 kilometers per hour would cause Annie to pass the horse before reaching the destination.

In Sample Case #2, there are two other horses on the road. The faster horse will catch up to the slower horse at kilometer 240 after 2 hours. Both horses will then go at the slower horse's speed for 1 more hour, until the horses reach Annie's destination at kilometer 300. The maximum speed that Annie can choose without passing another horse is 100 kilometers per hour. 
'''

def read_int():
	return int(input())

def read_two_int():
	raw_two_int = input()
	raw_int_list = raw_two_int.split()
	return int(raw_int_list[0]), int(raw_int_list[1])

def print_it_now(case_n, speed):
	# y(speed) will be considered correct if it is within an absolute or
	# relative error of 10-6 of the correct answer.

	ans = 'Case #%s: %.6f' % (case_n, speed)
	# ensure stdout flush
	print(ans, flush=True)

def play_a_round(case_n):
	d, n = read_two_int()
	k_ = []
	s_ = []
	for _ in range(n):
		k, s = read_two_int()
		k_.append(k)
		s_.append(s)

	# Just find the slowest
	# Note that: Two or more horses can share the same position for any amount of time;
	# you may consider the horses to be single points

	t_slowest = 0.0
	for i, k in enumerate(k_):
		s = s_[i]
		t = (d - k)/s
		if t > t_slowest:
			t_slowest = t
	s = 1.00 * d / t_slowest
	print_it_now(case_n, s)

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
	3

2525 1
2400 5		2525-2400 / 5 = 25; 2525/25 = 101

300 2
120 60		300-120 / 60 = 3;  -> slowest		300/3 = 100
60 90		300-60 / 90 = 2.67;

100 2
80 100		100-80 / 100 = 0.2;
70 10		100-70 / 10 = 3; -> slowest			100/3 = 33.3

Output
	Case #1: 101.000000
	Case #2: 100.000000
	Case #3: 33.333333

'''
