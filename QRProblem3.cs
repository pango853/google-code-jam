/*
Qualification Round 2020
Contestants with a final score of at least 30 points in this round will advance to Round 1.

    1. Vestigium                    7 points
    2. Nesting Depth                5, 11 points
    3. Parenting Partnering Returns 7, 12 points
    4. ESAb ATAd                    1, 9, 16 points
    5. Indicium                     7, 25 points

# Parenting Partnering Returns (7pts, 12pts)

Last updated: Apr 4 2020, 10:23

## Problem
Cameron and Jamie's kid is almost 3 years old! However, even though the child is more independent now, scheduling kid activities and domestic necessities is still a challenge for the couple.

Cameron and Jamie have a list of N activities to take care of during the day. Each activity happens during a specified interval during the day. They need to assign each activity to one of them, so that neither of them is responsible for two activities that overlap. An activity that ends at time t is not considered to overlap with another activity that starts at time t.

For example, suppose that Jamie and Cameron need to cover 3 activities: one running from 18:00 to 20:00, another from 19:00 to 21:00 and another from 22:00 to 23:00. One possibility would be for Jamie to cover the activity running from 19:00 to 21:00, with Cameron covering the other two. Another valid schedule would be for Cameron to cover the activity from 18:00 to 20:00 and Jamie to cover the other two. Notice that the first two activities overlap in the time between 19:00 and 20:00, so it is impossible to assign both of those activities to the same partner.

Given the starting and ending times of each activity, find any schedule that does not require the same person to cover overlapping activities, or say that it is impossible.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a line containing a single integer N, the number of activities to assign. Then, N more lines follow. The i-th of these lines (counting starting from 1) contains two integers Si and Ei. The i-th activity starts exactly Si minutes after midnight and ends exactly Ei minutes after midnight.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is IMPOSSIBLE if there is no valid schedule according to the above rules, or a string of exactly N characters otherwise. The i-th character in y must be C if the i-th activity is assigned to Cameron in your proposed schedule, and J if it is assigned to Jamie.

If there are multiple solutions, you may output any one of them. (See "What if a test case has multiple correct solutions?" in the Competing section of the FAQ. This information about multiple solutions will not be explicitly stated in the remainder of the 2020 contest.)

Limits
Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
0 ≤ Si < Ei ≤ 24 × 60.

Test set 1 (Visible Verdict)
2 ≤ N ≤ 10.

Test set 2 (Visible Verdict)
2 ≤ N ≤ 1000.

Sample

Input
 	
Output
 
4
3
360 480
420 540
600 660
3
0 1440
1 3
2 4
5
99 150
1 100
100 301
2 5
150 250
2
0 720
720 1440

  
Case #1: CJC
Case #2: IMPOSSIBLE
Case #3: JCCJJ
Case #4: CC

  
Sample Case #1 is the one described in the problem statement. As mentioned above, there are other valid solutions, like JCJ and JCC.

In Sample Case #2, all three activities overlap with each other. Assigning them all would mean someone would end up with at least two overlapping activities, so there is no valid schedule.

In Sample Case #3, notice that Cameron ends an activity and starts another one at minute 100.

In Sample Case #4, any schedule would be valid. Specifically, it is OK for one partner to do all activities.

*/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Collections; 

namespace google_code_jam
{
    class QRProblem3ParentingPartneringReturns
	{
		const string IMPOSSIBLE = "IMPOSSIBLE";
		const char Cameron = 'C';
		const char Jamie = 'J';

		struct Activity{
			public int Start;
			public int End;
			public int Position;

			public override string ToString(){return String.Format("Activity: Position={0} - Start:{1}, End:{2}", Position, Start, End);}
		}

		private static Activity ParseActivity(string input, int idx)
		{
			string[] rawData = input.Split(' ');
			return new Activity(){
				Start = Int32.Parse(rawData[0]),
				End = Int32.Parse(rawData[1]),
				Position = idx
			};
		}

		private static void AddToSortedActivities(Activity[] activities, Activity activity){
			int found = -1;
			int idx = 0;
			foreach(Activity one in activities)
			{
				if(0 == one.End) break; // End=0 indicates it is not initialized
				idx++;

				//Console.WriteLine("\t\tDebug: one.Start={0}, new.Start={1}", one.Start, activity.Start);
				if( -1 == found ){
					if(one.Start > activity.Start)
					{
						found = idx;
					}else if(one.Start == activity.Start && one.End == activity.End){
						found = idx;
					}
				}
			}
			//Console.WriteLine("\tDebug: idx={0}, found={1}", idx, found);
			if(-1 != found){
				for(int i=idx; i>=found; i--)
				{
					activities[i] = activities[i-1];
				}
				activities[found-1] = activity;

				//Console.Write("\t\tDebug: ");
				//foreach(Activity one in activities){ Console.Write("{0} ", one.Start); }
				//Console.WriteLine();
			}else{
				activities[idx] = activity;
			}
		}

		private static string GoNext(int pos, int size, Activity[] activities, List<int> stackC, List<int> stackJ, string answer){
			// Debugging
			//Console.WriteLine("\tDebug: pos: {0}", pos);

			if(pos >= size){
				//Console.WriteLine("\tDebug: I found it! {0}", answer);
				return answer;
			}

			Activity nextAct = activities[pos];
			bool isC_ok = true;
			bool isJ_ok = true;
			foreach(int i in stackC)
			{
				if(activities[i].End > nextAct.Start)
				{
					isC_ok = false;
				}
			}
			foreach(int i in stackJ)
			{
				if(activities[i].End > nextAct.Start)
				{
					isJ_ok = false;
				}
			}
			string nextAnswer = null;
			// First try C
			if( isC_ok )
			{
				//Console.WriteLine("\tDebug: curr {0}, try {1}", answer, Cameron);
				List<int> newStackC = new List<int>(stackC.ToArray());
				newStackC.Add(pos);
				nextAnswer = GoNext(pos+1, size, activities, newStackC, stackJ, answer+Cameron);
			}
			if(isJ_ok && null == nextAnswer)
			{
				//Console.WriteLine("\tDebug: curr {0}, try {1}", answer, Jamie);
				List<int> newStackJ = new List<int>(stackJ.ToArray());
				newStackJ.Add(pos);
				nextAnswer = GoNext(pos+1, size, activities, stackC, newStackJ, answer+Jamie);
			}
			// means if(isC_ok == false && isJ_ok == false)
			return nextAnswer;
		}

		private static void FindSolution(int c_ase, int size, Activity[] activities){

			List<int> stackC = new List<int>();
			List<int> stackJ = new List<int>();

			int i = 0;
			string answer = "" + Cameron; // Just start from Cameron's kid
			stackC.Add(i);

			answer = GoNext(i+1, size, activities, stackC, stackJ, answer);

			// Re-ordering answer
			if(null == answer){
				Console.WriteLine("Case #{0}: {1}", c_ase, IMPOSSIBLE);
			}
			else
			{
				char[] charAry = answer.ToCharArray();
				int idx = 0;
				foreach(Activity one in activities)
				{
					if(one.Position != idx)
					{
						char swp = charAry[idx];
						charAry[idx] = charAry[one.Position];
						charAry[one.Position] = swp;
					}
					idx++;
				}
				Console.WriteLine("Case #{0}: {1}", c_ase, new string(charAry));
			}
		}

		//static void Main(string[] args){ SubMain(args); }
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

				Activity[] activities = new Activity[N];

				// 1. Load into a sorted list
				int i = 0;
				do
				{
					line = Console.ReadLine();

					Activity activity = ParseActivity(line, i);
					AddToSortedActivities(activities, activity);

		        }while(++i < N);

				// 2. recursively exploring
				// Debugging
				//foreach(Activity one in activities){ Console.WriteLine("\tDebug: {0}", one);}

				FindSolution(c_ase, N, activities);
			}
		}
	}
}
