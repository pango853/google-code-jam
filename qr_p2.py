# coding: utf-8 -*-

#################################
# Qualification Round 2019
# Problem 2
#    You Can Go Your Own Way (5pts, 9pts, 10pts)
#################################
'''
Problem

You have just entered the world's easiest maze. You start in the northwest cell of an N by N grid of unit cells, and you must reach the southeast cell. You have only two types of moves available: a unit move to the east, and a unit move to the south. You can move into any cell, but you may not make a move that would cause you to leave the grid. 
You are excited to be the first in the world to solve the maze, but then you see footprints. Your rival, Labyrinth Lydia, has already solved the maze before you, using the same rules described above! 
As an original thinker, you do not want to reuse any of Lydia's moves. Specifically, if her path includes a unit move from some cell A to some adjacent cell B, your path cannot also include a move from A to B. (However, in that case, it is OK for your path to visit A or visit B, as long as you do not go from A to B.) Please find such a path. 
In the following picture, Lydia's path is indicated in blue, and one possible valid path for you is indicated in orange: 

// Figure omitted //

Input

The first line of the input gives the number of test cases, T. T test cases follow; each case consists of two lines. The first line contains one integer N, giving the dimensions of the maze, as described above. The second line contains a string P of 2N - 2 characters, each of which is either uppercase E (for east) or uppercase S (for south), representing Lydia's valid path through the maze. 

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is a string of 2N - 2 characters each of which is either uppercase E (for east) or uppercase S (for south), representing your valid path through the maze that does not conflict with Lydia's path, as described above. It is guaranteed that at least one answer exists. 

Limits

1 ≤ T ≤ 100.
Time limit: 15 seconds per test set.
Memory limit: 1GB.
P contains exactly N - 1 E characters and exactly N - 1 S characters.
Test set 1 (Visible)
2 ≤ N ≤ 10.
Test set 2 (Visible)
2 ≤ N ≤ 1000.
Test set 3 (Hidden)
For at most 10 cases, 2 ≤ N ≤ 50000.
For all other cases, 2 ≤ N ≤ 10000.

Sample


Input 	Output 
  
2
2	Case #1: ES
SE	Case #2: SEEESSES
5
EESSSESE

  
In Sample Case #1, the maze is so small that there is only one valid solution left for us. 
Sample Case #2 corresponds to the picture above. Notice that it is acceptable for the paths to cross. 
'''

#from pprint import pprint

def read_int():
	return int(input())

def read_str():
	return input().strip()

def answer(case_n, footprints):
	ans = 'Case #%d: %s' % (case_n, footprints)
	# ensure stdout flush
	print(ans, flush=True)


def play_a_round(case_n):
	n = read_int()
	footprints = read_str()
	##n = 5
	##footprints = 'EESSSESE'
	##print('         ' + footprints)

	mine = ''
	for d in footprints:
		print(d)
		if 'E' == d:
			d_mine = 'S'
		else:
			d_mine = 'E'
		mine += d_mine

	answer(case_n, mine)


if '__main__' == __name__:
	# Read number of test cases
	t = read_int()
	##t = 1

	# Count up test cases
	t_count = 0
	while t_count < t:
		t_count += 1

		play_a_round(t_count)

'''
Think

0 1 2 3 4 5 6 7
E E S S S E S E
S E E E S S E S
0 1 0 1 0 1 0 1
x o x x o x x x

EES  SSE  SE
SEE  ESS  ES



Input 

2
2
SE
5
EESSSESE


Output 

Case #1: ES
Case #2: SEEESSES
'''