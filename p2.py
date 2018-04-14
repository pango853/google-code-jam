# coding: utf-8 -*-


def read_int():
	return int(input())

def read_3int():
	raw_ints = input()
	raw_int_list = raw_ints.split()
	return int(raw_int_list[0]), int(raw_int_list[1]), int(raw_int_list[2])

def print_it_now(case_n, t):
	ans = 'Case #%s: %d' % (case_n, t)
	# ensure stdout flush
	print(ans, flush=True)

def select(msp_map, currenttime):
	best = None
	found_i = None
	for i, msp in enumerate(msp_map):
		cnt = msp[3]
		print("#DEBUG msp       :", i, msp, cnt)
		if cnt >= msp[0]:
			continue
		if cnt > 0:
			cost = msp[1]
		else:
			cost = msp[1] + msp[2]
		if (best is None) or (best > cost):
			best = cost
			found_i = i

	msp_map[found_i][3] = cnt + 1
	lasttime = msp_map[found_i][4]
	aftertime = lasttime + best
	timediff = aftertime - currenttime
	msp_map[found_i][4] = aftertime
	print("#DEBUG found best :", found_i, best, msp_map, timediff)
	if timediff < 0:
		timediff = 0
	return timediff

def play_a_round(case_n):
	rn, bn, cn = read_3int()

	msp_map = []
	for i in range(cn):
		msp = list(read_3int())
		msp.append(0) # count
		msp.append(0) # time
		msp_map.append(msp)

	print("#DEBUG input     :", msp_map)

	total = 0
	bits = bn

	while bits > 0:
		print("#DEBUG bits      :", bits)
		total += select(msp_map, total)
		bits -= 1

	print_it_now(case_n, total)

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
2 2 2
1 2 3
1 1 2

2 2 2
1 2 3
2 1 2

3 4 5
2 3 3
2 1 5
2 4 2
2 2 4
2 5 1

	
Output

Case #1: 5
Case #2: 4
Case #3: 7
'''
