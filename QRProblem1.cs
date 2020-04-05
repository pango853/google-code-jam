/*
Qualification Round 2020
Contestants with a final score of at least 30 points in this round will advance to Round 1.

    1. Vestigium                    7 points
    2. Nesting Depth                5, 11 points
    3. Parenting Partnering Returns 7, 12 points
    4. ESAb ATAd                    1, 9, 16 points
    5. Indicium                     7, 25 points
  
# Vestigium (7pts)

Last updated: Apr 4 2020, 10:23

## Problem
Vestigium means "trace" in Latin. In this problem we work with Latin squares and matrix traces.

The trace of a square matrix is the sum of the values on the main diagonal (which runs from the upper left to the lower right).

An N-by-N square matrix is a Latin square if each cell contains one of N different values, and no value is repeated within a row or a column. In this problem, we will deal only with "natural Latin squares" in which the N values are the integers between 1 and N.

Given a matrix that contains only integers between 1 and N, we want to compute its trace and check whether it is a natural Latin square. To give some additional information, instead of simply telling us whether the matrix is a natural Latin square or not, please compute the number of rows and the number of columns that contain repeated values.

## Input
The first line of the input gives the number of test cases, T. T test cases follow. Each starts with a line containing a single integer N: the size of the matrix to explore. Then, N lines follow. The i-th of these lines contains N integers Mi,1, Mi,2 ..., Mi,N. Mi,j is the integer in the i-th row and j-th column of the matrix.

## Output
For each test case, output one line containing Case #x: k r c, where x is the test case number (starting from 1), k is the trace of the matrix, r is the number of rows of the matrix that contain repeated elements, and c is the number of columns of the matrix that contain repeated elements.

## Limits
Test set 1 (Visible Verdict)
Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
2 ≤ N ≤ 100.
1 ≤ Mi,j ≤ N, for all i, j.

## Sample

Input
3
4
1 2 3 4
2 1 4 3
3 4 1 2
4 3 2 1
4
2 2 2 2
2 3 2 3
2 2 2 3
2 2 2 2
3
2 1 3
1 3 2
1 2 3

  
Output
Case #1: 4 0 0
Case #2: 9 4 4
Case #3: 8 0 2

  
In Sample Case #1, the input is a natural Latin square, which means no row or column has repeated elements. All four values in the main diagonal are 1, and so the trace (their sum) is 4.

In Sample Case #2, all rows and columns have repeated elements. Notice that each row or column with repeated elements is counted only once regardless of the number of elements that are repeated or how often they are repeated within the row or column. In addition, notice that some integers in the range 1 through N may be absent from the input.

In Sample Case #3, the leftmost and rightmost columns have repeated elements.

*/

using System;
using System.Collections.Generic;
using System.Linq;

namespace google_code_jam
{

	class QRProblem1Vestigium
	{
    const double EPS = 0.001;

    private static void ParseIntegers(string input, int len, int[] data)
    {
      string[] rawData = input.Split(' ');
      for(int i=0; i<len; i++){
        data[i] = Int32.Parse(rawData[i]);
      }
    }

    private static int Sum(int n)
    {
      return n*(n+1)/2;
    }
    private static void SumUp(int len, int[] sum, double[] div, int[] data, double avg)
    {
      for(int i=0; i<len; i++){
        sum[i] += data[i];
        div[i] += Math.Abs(data[i]-avg);
      }
    }
    private static bool CheckIfRepeated(int len, int[] data, int sum, int div)
    {
      //(sum != M_i.Sum())
      int mySum = 0;
      double myDiv = 0;
      double avg = 1.0*sum/len;
      for(int i=0; i<len; i++){
        mySum += data[i];
        myDiv += Math.Abs(data[i]-avg);
      }
      //Console.WriteLine("\tDebug sum={0}, div={1}, {2}, {3}", sum, div, mySum, myDiv);
      return !(mySum == sum) || !(Math.Abs(myDiv-div) < EPS);
    }

    private static int CountDiff(int len, int[] sumAry, double[] divAry, int sum, int div)
    {
      int count = 0;
      for(int i=0; i<len; i++){
        count += ( !(sum == sumAry[i]) || !(Math.Abs(divAry[i]-div) < EPS) )? 1 : 0;
      }
      return count;
    }

		public static void SubMain(string[] args)
		{
			string line;
      int T;

			// The first line of the input gives the number of test cases, T.
      line = Console.ReadLine();
      T = Int32.Parse(line);

      IEnumerable<int> rangeT = Enumerable.Range(1, T);
      foreach (int c_ase in rangeT)
      {
        line = Console.ReadLine();
        int N = Int32.Parse(line);
        int[] Sum_j = Enumerable.Repeat(0, N).ToArray();
        double[] Div_j = Enumerable.Repeat(0.0, N).ToArray();
        int sum = Sum(N);
        double avg = 1.0 * sum/N;
        int div = sum - Sum((int)Math.Ceiling(0.5 * N)) - Sum((int)Math.Floor(0.5 * N));
        //Console.WriteLine("\tDebug sum={0}, div={1}", sum, div);

        int k=0, r=0, c;

        int i = 0;
        do
        {
          line = Console.ReadLine();
          int[] M_i = new int[N];
          ParseIntegers(line, N, M_i);

          SumUp(N, Sum_j, Div_j, M_i, avg);

          k += M_i[i];

          r += CheckIfRepeated(N, M_i, sum, div)? 1 : 0;
        }while(++i < N);

        // Array.ForEach(Sum_j, Console.WriteLine);
        c = CountDiff(N, Sum_j, Div_j, sum, div);
        Console.WriteLine("Case #{0}: {1} {2} {3}", c_ase, k, r, c);
      }
		}
	}
}
