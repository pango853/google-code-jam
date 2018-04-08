# coding: utf-8 -*-

#################################
# Qualification Round 2018
# Problem 3
#   Go, Gopher!
#################################
'''
Problem

The Code Jam team has just purchased an orchard that is a two-dimensional matrix of cells of unprepared soil, with 1000 rows and 1000 columns. We plan to use this orchard to grow a variety of trees — AVL, binary, red-black, splay, and so on — so we need to prepare some of the cells by digging holes:

    In order to have enough trees to use for each year's tree problems, we need there to be at least A prepared cells.
    In order to care for our trees properly, the set of all prepared cells must form a single grid-aligned rectangle in which every cell within the rectangle is prepared.

Note that the above also implies that none of the cells outside of that rectangle can be prepared. We want the orchard to look tidy!

For example, when A=11, although the eleven prepared cells in the left figure below form a 3x4 rectangle (that is, with 3 rows and 4 columns), the cell in the center of the rectangle is not prepared. As a result, we have not yet completed preparing our orchard, since not every cell of the 3x4 rectangle is prepared. However, after just preparing the center cell, the rectangle of size at least 11 is fully filled, and the orchard is ready.
✔ ✘ ⇨

See below for another example. In this case, A=6. Note that the middle figure prepares a cell outside the 3x2 rectangle, so although the rightmost figure prepares a rectangle of size 6, the entire set of the prepared cells does not form a rectangle (due to the extra cell on the left). As a result, the orchard is not ready.
✘ ⇨ ⇨ ✘ ✘

Digging is hard work for humans, so we have borrowed the Go gopher from the Google Go team and trained it to help us out by preparing cells. We can deploy the gopher by giving it the coordinates of a target cell in the matrix that is not along any of the borders of the matrix. However, we have not yet perfected the gopher's training, so it will choose a cell uniformly at (pseudo-)random from the 3x3 block of nine cells centered on the target cell, and then prepare the cell it has chosen. (If it chooses a cell that was already prepared, it will uselessly prepare it again.)

We can only deploy the gopher up to 1000 times before it gets too tired to keep digging, so we need your help in figuring out how to deploy it strategically. When you deploy the gopher, you will be told which cell the gopher actually prepared, and you can take this information into account before deploying it again, if needed. Note that you do not have to declare the dimensions or location of a rectangle in advance.
Input and output

This problem is interactive, which means that the concepts of input and output are different than in standard Code Jam problems. You will interact with a separate process that both provides you with information and evaluates your responses. All information comes into your program via standard input; anything that you need to communicate should be sent via standard output. Remember that many programming languages buffer the output by default, so make sure your output actually goes out (for instance, by flushing the buffer) before blocking to wait for a response. See the FAQ for an explanation of what it means to flush the buffer. Anything your program sends through standard error is ignored, but it might consume some memory and be counted against your memory limit, so do not overflow it. To help you debug, a local testing tool script (in Python) is provided at the very end of the problem statement. In addition, sample solutions to a previous Code Jam interactive problem (in all of our supported languages) are provided here.

Initially, your program should read a single line containing a single integer T indicating the number of test cases. Then, you need to process T test cases.

For each test case, your program will read a single line containing a single integer A indicating the minimum required prepared rectangular area. Then, your program will process up to 1000 exchanges with our judge.

For each exchange, your program needs to use standard output to send a single line containing two integers I and J: the row and column number you want to deploy the gopher to. The two integers must be between 2 and 999, and written in base-10 without leading zeroes. If your output format is wrong (e.g., out of bounds values), your program will fail, and the judge will send you a single line with -1 -1 which signals that your test has failed, and it will not send anything to your input stream after that. Otherwise, in response to your deployment, the judge will print a single line containing two integers I' and J' to your input stream, which your program must read through standard input.

If the last deployment caused the set of prepared cells to be a rectangle of area at least A, you will get I' = J' = 0, signaling the end of the test case. Otherwise, I' and J' are the row and column numbers of the cell that was actually prepared by the gopher, with abs(I'-I) ≤ 1 and abs(J'-J) ≤ 1. Then, you can start another exchange.

If your program gets something wrong (e.g. wrong output format, or out-of-bounds values), as mentioned above, the judge will send I' = J' = -1, and stop sending output to your input stream afterwards. If your program continues to wait for the judge after reading in I' = J' = -1, your program will time out, resulting in a Time Limit Exceeded error. Notice that it is your responsibility to have your program exit in time to receive the appropriate verdict (Wrong Answer, Runtime Error, etc.) instead of a Time Limit Exceeded error. As usual, if the total time or memory is exceeded, or your program gets a runtime error, you will receive the appropriate verdict.

If the test case is solved within 1000 deployments, you will receive the I' = J' = 0 message from the judge, as mentioned above, and then continue to solve the next test case. After 1000 exchanges, if the test case is not solved, the judge will send the I' = J' = -1 message, and stop sending output to your input stream after.

You should not send additional information to the judge after solving all test cases. In other words, if your program keeps printing to standard output after receiving I' = J' = 0 message from the judge for the last test case, you will receive a Wrong Answer judgment.

Please be advised that for a given test case, the cells that the gopher will pick from each 3x3 block are (pseudo-)random and independent of each other, but they are determined using the same seed each time for the same test case, so a solution that gives an incorrect result for a test case will do so consistently across all attempts for the same test case. We have also set different seeds for different test cases.
Limits

1 ≤ T ≤ 20.
Memory limit: 1 GB.
Test set 1 (Visible)

A = 20.
Time limit (for the entire test set): 20 seconds.
Test set 2 (Hidden)

A = 200.
Time limit (for the entire test set): 60 seconds.

Sample interaction
  ... omitted ...

Local Testing Tool
  ... omitted ...
'''

import sys
import math

def read_int():
	return int(input())

def read_two_int():
	raw_two_int = input()
	raw_int_list = raw_two_int.split()
	return int(raw_int_list[0]), int(raw_int_list[1])

def init_map(m, n):
	empty_map = []
	for _ in range(m):
		empty_map.append([0] * n)
	return empty_map

def print_it_now(i, j):
	ans = '%d %d' % (i, j)
	print(ans, flush=True)

def deploy_gopher(i, j):
	print_it_now(i, j)
	i_go, j_go = read_two_int()
	return i_go, j_go

def add2nbmap(nbmap, i, j):
	if nbmap[i][j] != -1:
		nbmap[i][j] += 1

def update_orchard(i, j, orchard):
	orchard[i][j] += 1

def is_edge_filled(i, j, orchard, offset=-1):
	#print('DEBUG orchard[%d][%d] = %d', i-1, j+offset, orchard[i-1][j+offset])
	#print('DEBUG orchard[%d][%d] = %d', i, j+offset, orchard[i][j+offset])
	#print('DEBUG orchard[%d][%d] = %d', i+1, j+offset, orchard[i+1][j+offset])

	return orchard[i-1][j+offset] > 0 and orchard[i][j+offset] > 0 and orchard[i+1][j+offset] > 0

def debug_grids(round_n, orchard, m, n):
	print('===== [%5d] =====' % (round_n), end='')
	for i in range(m):
		print()
		for j in range(n):
			sys.stdout.write('%4s' % orchard[i][j])
	print()
	print('----------------------')
	print(flush=True)

def play_a_round():
	area = read_int()

	last_col_idx = math.ceil(1.0*area/3)
	m = 3+1
	n = last_col_idx + 1

	#print('DEBUG last_col_idx = %d' % (last_col_idx))
	#sys.stderr.write('!!! EDEBUG m,n = %d,%d   area=%d\n' % (m, n, area))
	orchard = init_map(m, n)

	# Start from (1,1)
	i_target, j_target = 2, 2
	for _ in range(3):
		i_go, j_go = deploy_gopher(i_target, j_target)
		update_orchard(i_go, j_go, orchard)

	# Coz A=20, just try to form a 3x7 farm filling rows by rows
	# X......  O:Target; X:Filled
	# XO.....
	# X......
	# -->
	# XX.....
	# XXO....
	# XX.....

	cnt = 3
	while True:
		if is_edge_filled(i_target, j_target, orchard):
			j_target += 1

		if j_target > last_col_idx-1:
			j_target = last_col_idx-1
			if is_edge_filled(i_target, j_target, orchard, -1) and \
				is_edge_filled(i_target, j_target, orchard, 0) and \
				is_edge_filled(i_target, j_target, orchard, 1):
				break # OK We go it!

		cnt += 1
		i_go, j_go = deploy_gopher(i_target, j_target)
		#sys.stderr.write('!!! DEBUG want(i,j)=(%d,%d)  go(i,j)=(%d,%d)\n' % (i_target, j_target, i_go, j_go))
		update_orchard(i_go, j_go, orchard)
		#print('DEBUG want(i,j)=(%d,%d)  go(i,j)=(%d,%d)' % (i_target, j_target, i_go, j_go))

		if (i_go == 0) or (j_go == 0):
			break # We made it!!

		if (i_go == -1) or (j_go == -1):
			#print('DEBUG ERROR')
			#exit(1)
			break

		if cnt >= 1000:
			break

		#input('DEBUG ENTER...')
		#debug_grids(cnt, orchard, m, n)


if '__main__' == __name__:
	# Read number of test cases
	t = read_int()

	# Count up test cases
	t_count = 0
	while t_count < t:
		t_count += 1

		play_a_round()

'''
Input
	10
	20
	1 2
	...

Output

	2 2
	...

'''
