# coding: utf-8 -*-


class CONST:
	POSSIBLE = 'POSSIBLE'
	IMPOSSIBLE = 'IMPOSSIBLE'

def read_int():
	return int(input())

def read_n_char(n):
	raw_in = input() # NOTE: n <= 10^5 so we will have enough memory
	ary = list(raw_in.strip())
	assert len(ary) == n

	return ary

def read_4int():
	raw_ints = input()
	raw_int_list = raw_ints.split()
	return int(raw_int_list[0]), int(raw_int_list[1]), int(raw_int_list[2]), int(raw_int_list[3])

def print_it_now(case_n, is_ok):
	if is_ok:
		ans = 'Case #%s: %s' % (case_n, CONST.POSSIBLE)
	else:
		ans = 'Case #%s: %s' % (case_n, CONST.IMPOSSIBLE)
	# ensure stdout flush
	print(ans, flush=True)

def is_dividable(ary, cut):
	total = sum(ary)
	if total % (cut+1) != 0:
		return False
	avg = int(total/(cut+1))

	cum = 0
	pos_ary = []
	last_i = len(ary) - 1
	for i, a in enumerate(ary):
		cum += a
		#print("#DEBUG check result:", cum, avg)
		if cum == avg:
			if i != last_i:
				pos_ary.append(i+1)
			cum = 0
		elif cum > avg:
			return None
	if cum != 0:
		return None
	return pos_ary

def full_check(wmap, hcuts, vcuts, avg):
	#print("#DEBUG h/vcuts:", hcuts, vcuts)
	i_0, j_0 = 0, 0
	for i in hcuts:
		for j in vcuts:
			total = 0
			for ii in range(i_0, i):
				for jj in range(j_0, j):
					a = wmap[ii][jj]
					if '@' == a:
						total += 1
			#print("#DEBUG [%d,%d]->[%d,%d] %d vs. %d" % (i_0, j_0, i, j, total, avg))
			if total != avg:
				return False
			j_0 = j
		i_0 = i
		j_0 = 0

	return True

def play_a_round(case_n):
	row, col, hori, vert = read_4int()

	waffle_map = []
	for _ in range(row):
		waffle_map.append(read_n_char(col))
	#print("#DEBUG input:", waffle_map)

	rows_ary = []
	for i in range(row):
		rows_ary.append(sum(x == '@' for x in waffle_map[i]))

	# Pre cals
	total = sum(rows_ary)
	hpvp = (hori+1)*(vert+1)
	if total > 0 and (total % hpvp) != 0:
		#print("#DEBUG pre check:", total, hori, vert)
		print_it_now(case_n, False)
		return
	avg = int(total / hpvp)

	#print("#DEBUG hori check:", rows_ary, hori)
	row_cut_pos_ary = is_dividable(rows_ary, hori)
	if row_cut_pos_ary is None:
		print_it_now(case_n, False)
		return

	cols_ary = []
	for j in range(col):
		total = 0
		for i in range(row):
			if waffle_map[i][j] == '@':
				total += 1
		cols_ary.append(total)
	#print("#DEBUG vert check:", cols_ary, vert)
	col_cut_pos_ary = is_dividable(cols_ary, vert)
	if col_cut_pos_ary is None:
		print_it_now(case_n, False)
		return

	rs = full_check(waffle_map, row_cut_pos_ary, col_cut_pos_ary, avg)
	print_it_now(case_n, rs)

if '__main__' == __name__:
	# Read number of test cases
	t = read_int()

	# Count up test cases
	t_count = 0
	while t_count < t:
		t_count += 1

		play_a_round(t_count)

'''
Case #1: POSSIBLE
Case #2: IMPOSSIBLE
Case #3: POSSIBLE
Case #4: IMPOSSIBLE
Case #5: POSSIBLE
Case #6: IMPOSSIBLE

6
3 6 1 1
.@@..@
.....@
@.@.@@
4 3 1 1
@@@
@.@
@.@
@@@
4 5 1 1
.....
.....
.....
.....
4 4 1 1
..@@
..@@
@@..
@@..
3 4 2 2
@.@@
@@.@
@.@@
3 4 1 2
.@.@
@.@.
.@.@
'''
