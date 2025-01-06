// Mr Parandhamayya working with words.
// He is given a word W, you need to divide the word into N non-empty parts, 
// such that all the newly formed words should be distinct, and 
// if you append all those words should form original word W.

// Your task is to help Mr Parandhamayya to divide the word into N parts,
// such that, the value of N should be maximized, and print N.

// Input Format:
// -------------
// Line-1: A string W, a word.

// Output Format:
// --------------
// Print an integer result, the value of N.


// Sample Input-1:
// ---------------
// banana

// Sample Output-1:
// ----------------
// 4

// Explanation: 
// ------------
// One way to divide the word is "b","a","n","ana".
// If you divide it like "b","a","n","an","a".The word "a" will be repeated.
// So it is not allowed to divide like the second way.


// Sample Input-2:
// ---------------
// mississippi

// Sample Output-2:
// ----------------
// 7

// Explanation: 
// ------------
// One of the way to divide the word is "m","i","s","si","ssi","p","pi".

// NOTE: Subsequences are not allowed.


import java.util.*;

public class divideWord {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int result = divWord(s);
        System.out.println(result);
        sc.close();
    }

    public static int divWord(String s) {
        Set<String> set = new HashSet<>();
        StringBuilder currentSubstring = new StringBuilder();
        int count = 0;
        for (char c : s.toCharArray()) {
            currentSubstring.append(c);
            String substring = currentSubstring.toString();
            if (set.contains(substring)) {
                set.add(currentSubstring.toString());
                count++;
                currentSubstring = new StringBuilder();
                currentSubstring.append(c);
            }
        }
        if (currentSubstring.length() > 0) {
            set.add(currentSubstring.toString());
            count++;
        }
        return count;
    }
}