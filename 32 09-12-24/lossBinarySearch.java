/*
Mr Ravi is a business man, he does business weekly Q times, 
and records his PROFIT or LOSS every time in to data[][] array. 
He records the LOSS as a negative value and PROFIT as a positive value.

Your task is to help Mr Ravi to know that how many total number of times,
he was in LOSS after P weeks.

NOTE: The values in data[][] are in descending order both row-wise and 
column-wise as given in sample testcases.

Input Format:
-------------
Line-1: Two space separated integers, P and Q
Next P lines: Q space separated integers, data[][].   

Output Format:
--------------
Print an integer result.


Sample Input-1:
---------------
4 4
5 4 2 -2
4 3 1 -2
2 2 -1 -3
-1 -1 -2 -4

Sample Output-1: 
----------------
8

Explanation: 
------------
8 days in LOSS,since there are 8 negative values.

Sample Input-2:
---------------
4 4
8 7 1 -2
7 6 2 -3
3 -1 -2 -4
-2 -3 -4 -7
	 
Sample Output-2:
----------------
9

Explanation:
------------
9 days in LOSS,since there are 8 negative values.

Sample Input-3:
---------------
2 2
9 3
5 0

Sample Output-3:
----------------
0
*/

import java.util.*;

public class lossBinarySearch {
    public static int sol(int[][] d) {
        int count = 0;
        
        for(int[] x: d) {
            int l = 0, h = x.length - 1;
            
            while(l <= h) {
                int mid = l + (h - l) / 2;
                
                if(x[mid] < 0) {
                    h = mid - 1;
                } else {
                    l = mid + 1;
                }
            }
            
            count += x.length - l;
        }
        
        return count;
    }
    
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int a = sc.nextInt();
        int b = sc.nextInt();
        
        int[][] d = new int[a][b];
        
        for (int i = 0; i < a; i++) {
            for (int j = 0; j < b; j++) {
                d[i][j] = sc.nextInt();
            }
        }
        
        System.out.println(sol(d));

        sc.close();
    }
}