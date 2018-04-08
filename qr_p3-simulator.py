# coding: utf-8 -*-

#################################
# Qualification Round 2018
# Problem 3
#   Go, Gopher!
#################################

import random

N = 100

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

def update_orchard(i, j, orchard, nbmap, marksmap):
	orchard[i][j] += 1

	nbmap[i][j] = -1
	for iii in (-1, 0, 1):
		for jjj in (-1, 0, 1):
			add2nbmap(nbmap, i+iii, j+jjj)

	update_marksmap(marksmap, nbmap)


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

def print_grids(counter, orchard, nbmap, marksmap):
	i_0, j_0, i_1, j_1 = N-1, N-1, 0, 0

	for i in range(N):
		for j in range(N):
			if orchard[i][j] != 0:
				if i_0 > i:
					i_0 = i
				if i_1 < i:
					i_1 = i
				if j_0 > j:
					j_0 = j
				if j_1 < j:
					j_1 = j
	if i_0 >= 2:
		i_0 -= 2
	if j_0 >= 2:
		j_0 -= 2
	if i_1 < N-2:
		i_1 += 2
	if j_1 < N-2:
		j_1 += 2
	print('DEBUG [%5d] print (%d, %d)->(%d, %d)' % (counter, i_0, j_0, i_1, j_1))

	print(' [RECHARD]      [NEIGHBOURS]       [MARKS]')

	for i in range(i_0, j_1+1):
		print('%s\t%s\t%s' % (' '.join(map(str, orchard[i][j_0:j_1+1])),\
		' '.join(map(str, nbmap[i][j_0:j_1+1])), \
		' '.join(map(str, marksmap[i][j_0:j_1+1]))))

	#print(orchard)

if '__main__' == __name__:

	random.seed(1986)

	orchard = init_map()
	marks_map = init_map()
	neighbours_map = init_map()

	# prepare_first_cell
	i_want, j_want = int(N/2), int(N/2)

	cnt = 1
	while True:
		i_go, j_go = deploy_gopher(i_want, j_want)
		print('DEBUG want(i,j)=(%d,%d)  go(i,j)=(%d,%d)' % (i_want, j_want, i_go, j_go))

		if (i_go == -1) or (j_go == -1):
			exit(1) # TODO ERROR

		update_orchard(i_go, j_go, orchard, neighbours_map, marks_map)

		print_grids(cnt, orchard, neighbours_map, marks_map)

		input('ENTER...') # DEBUG
		cnt += 1

		# NEXT
		i_want, j_want = prepare_cell(orchard, neighbours_map, marks_map)

