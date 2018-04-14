# coding: utf-8 -*-

#################################
# Round 1A 2018
# Problem 1
#   Waffle Choppers
# 	(9pt 16pt)
# =>
#   VISIBLE : Correct
#   HIDDEN  : Correct
#################################
'''
Problem

The diners at the Infinite House of Pancakes have gotten tired of circular pancakes, so the chefs are about to offer a new menu option: waffles! As a publicity stunt, they have made one large waffle that is a grid of square cells with R rows and C columns. Each cell of the waffle is either empty, or contains a single chocolate chip.

Now it is time for the chefs to divide up the waffle among their hungry diners. A horizontal cut runs along the entire gridline between two of the rows; a vertical cut runs along the entire gridline between two of the columns. For efficiency's sake, one chef will make exactly H different horizontal cuts and another chef will make exactly V different vertical cuts. This will conveniently create one piece for each of the (H + 1) × (V + 1) diners. The pieces will not necessarily all be of equal sizes, but that is fine; market research has shown that the diners do not care about that.

What the diners do care about is the number of chocolate chips they get, so each piece must have exactly the same number of chocolate chips. Can you determine whether the chefs can accomplish this goal using the given numbers of horizontal and vertical cuts?
Input

The first line of the input gives the number of test cases, T; T test cases follow. Each begins with one line containing four integers R, C, H, and V: the number of rows and columns in the waffle, and the exact numbers of horizontal and vertical cuts that the chefs must make. Then, there are R more lines of C characters each; the j-th character in the i-th of these lines represents the cell in the i-th row and the j-th column of the waffle. Each character is either @, which means the cell has a chocolate chip, or ., which means the cell is empty.
Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is POSSIBLE if the chefs can accomplish the goal as described above, or IMPOSSIBLE if they cannot.
Limits

1 ≤ T ≤ 100.
Time limit: 6 seconds per test set.
Memory limit: 1GB.
Test set 1 (Visible)

2 ≤ R ≤ 10.
2 ≤ C ≤ 10.
H = 1.
V = 1.
Test set 2 (Hidden)

2 ≤ R ≤ 100.
2 ≤ C ≤ 100.
1 ≤ H < R.
1 ≤ V < C.
Sample

Input
  	
Output
 

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

	

Case #1: POSSIBLE
Case #2: IMPOSSIBLE
Case #3: POSSIBLE
Case #4: IMPOSSIBLE
Case #5: POSSIBLE
Case #6: IMPOSSIBLE

Note that the last two sample cases would not appear in test set 1.

In Sample Case #1, one possible strategy is to make the horizontal cut between the second and third rows from the top, and make the vertical cut between the fourth and fifth columns from the left. That creates the following pieces, each of which has exactly two chocolate chips:

.@@. .@
.... .@

@.@. @@

In Sample Case #2, no matter where you make the horizontal cut and the vertical cut, you will create pieces with unequal numbers of chocolate chips, so the case is impossible.

In Sample Case #3, there are no chocolate chips in the waffle. Any cutting strategy creates pieces which have the same number of chocolate chips (zero), so the diners are happy... but maybe not as happy as they would have been if they had gotten chocolate chips!

In Sample Case #4, just as in Sample Case #2, you cannot succeed regardless of where you make your horizontal cut and your vertical cut.

In Sample Case #5, the chefs can make the only two possible horizontal cuts, and make the two vertical cuts to the right of the first and third columns.

Although Sample Case #6 would be possible for other numbers of horizontal and vertical cuts, remember that you must use exactly H horizontal cuts and exactly V vertical cuts. No matter where you make your one horizontal cut and two vertical cuts, you cannot succeed.
'''

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
Input
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

Output
	Case #1: POSSIBLE
	Case #2: IMPOSSIBLE
	Case #3: POSSIBLE
	Case #4: IMPOSSIBLE
	Case #5: POSSIBLE
	Case #6: IMPOSSIBLE
'''
