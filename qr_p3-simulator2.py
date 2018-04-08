# coding: utf-8 -*-

#################################
# Qualification Round 2018
# Problem 3
#   Go, Gopher!
#################################

import sys
import random

N = 100
random.seed(1986)


def read_int():
	return int(input())

def init_map():
	empty_map = []
	for i in range(N):
		empty_map.append([0] * N)
	return empty_map

def deploy_gopher(i, j):
	r = random.randint(0, 8)
	i_diff = r % 3 - 1
	j_diff = int(r/3) - 1
	return (i+i_diff), (j+j_diff)

def add2nbmap(nbmap, i, j):
	if nbmap[i][j] != -1:
		nbmap[i][j] += 1

def update_marksmap(marksmap, nbmap):
	for i in range(1, N-1):
		for j in range(1, N-1):
			total = 0
			if nbmap[i][j] == 0:
				for iii in (-1, 0, 1):
					for jjj in (-1, 0, 1):
						total += nbmap[i+iii][j+jjj]
			marksmap[i][j] = total

def update_orchard(i, j, orchard):
	orchard[i][j] += 1

def is_edge_filled(i, j, orchard, offset=-1):
	return orchard[0][j+offset] > 0 and orchard[1][j+offset] > 0 and orchard[2][j+offset] > 0

def prepare_cell(orchard, nbmap, marksmap):
	found_i, found_j = -1, -1
	tmp = 0
	for i in range(N):
		for j in range(N):
			mark = marksmap[i][j]
			if mark > tmp:
				tmp = mark
				found_i, found_j = i, j

	if found_i == -1:
		print('DEBUGGING!!!')
		exit(1)
	return found_i, found_j

def print_grids(round, orchard):
	print('===== [%5d] =====' % (round), end='')
	for i in range(5):
		print()
		for j in range(10):
			sys.stdout.write('%4s' % orchard[i][j])
	print()
	print('----------------------')
	print(flush=True)

def play_a_round():
	orchard = init_map()

	# Start from (1,1)
	i_target, j_target = 1, 1
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

		if j_target > 6:
			j_target = 6
			if is_edge_filled(i_target, j_target, orchard, -1) and \
				is_edge_filled(i_target, j_target, orchard, 0) and \
				is_edge_filled(i_target, j_target, orchard, 1):
				break # OK We go it!

		cnt += 1
		i_go, j_go = deploy_gopher(i_target, j_target)
		update_orchard(i_go, j_go, orchard)
		#print('DEBUG want(i,j)=(%d,%d)  go(i,j)=(%d,%d)' % (i_target, j_target, i_go, j_go))

		if (i_go == -1) or (j_go == -1):
			#print('DEBUG ERROR')
			#exit(1)
			break

		if cnt >= 1000:
			break

		#input('DEBUG ENTER...')
		#print_grids(cnt, orchard)

	return cnt

if '__main__' == __name__:
	# Read number of test cases
	t = read_int()

	# Count up test cases
	t_count = 0
	total = 0
	threshold = 900
	out_count = 0
	while t_count < t:
		t_count += 1

		times = play_a_round()
		total += times
		if times > threshold:
			out_count += 1

		print('Case #%d: %d' % (t_count, times))
		print('avg = %3.2d, failed = %.2f' % (total/t_count, 100.0*out_count/times))
