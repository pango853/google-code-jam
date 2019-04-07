# coding: utf-8 -*-

#################################
# Practice Session 2018
# Question 1
#   Number Guessing
#################################
'''
Sample interaction

Here is a piece of pseudocode that demonstrates an interaction for one test set. Suppose there are three test cases in this test set. The pseudocode first reads an integer t, representing the number of test cases. Then the first test case begins. Suppose the correct answer P is 9 for the first test case. The pseudocode first reads three integers a, b, and n, representing the guessing range and maximum number of tries, respectively, and then outputs a guess 30. Since 30 is greater than 9, the string TOO_BIG is received through stdin from the judge. Then the pseudocode guesses 5 and receives TOO_SMALL in response. The guess 10 is subsequently printed to stdout which is again too big. Finally the pseudocode guesses 9, and receives CORRECT because 9 is the correct answer.

  t = read_int()         // reads 3 into t
  a, b = read_two_int()  // reads 0 into a and 30 into b; note that 0 30 is one line
  n = read_int()         // reads 30 into n
  print 30 to stdout     // guesses 30
  flush stdout
  string s = read()      // because 30 > 9, reads TOO_BIG into s
  print 5 to stdout      // guesses 5
  flush stdout
  s = read()             // reads TOO_SMALL into s since 5 < 9
  print 10 to stdout     // guesses 10
  flush stdout
  s = readline()         // reads TOO_BIG into s since 10 > 9
  print 9 to stdout      // guesses 9
  flush stdout
  s = read()             // reads CORRECT into s

The second test case shows what happens if the code continues to read from stdin after the judge stops sending info. In this example, the contestant guesses 31, which is outside the range (0, 30]. As a result, the judging system sends WRONG_ANSWER to the input stream of the pseudocode and stops sending anything after that. However, after reading WRONG_ANSWER into string s, the code continues to read for the next test case. Since there is nothing in the input stream (judge has stopped sending info), the code hangs and will eventually receive a Time Limit Exceeded Error.

  a, b = read_two_int()  // reads 0 into a and 30 into b; note that 0 30 is one line
  n = read_int()         // reads 30 into n
  print 31 to stdout     // guesses 31
  flush stdout
  string s = read()      // reads WRONG_ANSWER
  a, b = read_two_int()  // tries to read for the third test case but hangs since
                         // judge has stopped sending info to stdin

If the code in the example above exits immediately after reading WRONG_ANSWER, it will receive a Wrong Answer judgment instead.

  a, b = read_two_int()  // reads 0 into a and 30 into b; note that 0 30 is one line
  n = read_int()         // reads 30 into n
  print 31 to stdout     // guesses 31
  flush stdout
  string s = read()      // reads WRONG_ANSWER
  exit                   // receives a Wrong Answer judgment
'''

import random


def read_int():
	return int(input())

def read_two_int():
	raw_two_int = input()
	raw_int_list = raw_two_int.split()
	return int(raw_int_list[0]), int(raw_int_list[1])

def read_result():
	raw = input()
	return raw.strip()

def guess(exclusive_min, inclusive_max):
	q = random.randint(exclusive_min+1, inclusive_max)
	return q

def print_it_now(q):
	# ensure stdout flush
	print(q, flush=True)

def play_a_round():
	a, b = read_two_int()  #// reads 0 into a and 30 into b; note that 0 30 is one line
	n = read_int()         #// reads 30 into n

	n_count = 0
	while n_count < n:
		n_count += 1

		# Make a guess
		q = guess(a, b)
		print_it_now(q)

		rs = read_result()
		if 'TOO_BIG' == rs:
			b = q - 1
		elif 'TOO_SMALL' == rs:
			a = q
		elif 'CORRECT' == rs:
			break
		elif 'WRONG_ANSWER' == rs:
			# If your program gets something wrong
			# (e.g., wrong output format, or out-of-bounds values),
			# the judge will send WRONG_ANSWER to your input stream
			# and it will not send any other output after that.
			break
		else:
			raise ValueError('Unknown result : %s' % rs)

if '__main__' == __name__:
	# 0. Setup
	random.seed(1986)

	# 1. Read inputs
	t = read_int()         #// reads 3 into t: Number of test cases

	t_count = 0
	while t_count < t:
		t_count += 1

		play_a_round()
