// Mr Ajay Sharma is working woth words.
// He found that few words in the langugage have same meaning.
// Such words are given as a list of pairs as mappedpairs[],
// where mappedpairs[i] = [word1, word2] indicates that word1 and word2 are 
// the words with same meaning.

// He is given phrase, and he wants to apply all the mappedpairs[] on the phrase.

// Your task is to help Mr.Ajay Sharma to find and return all possible 
// Mapped Phrases generated after applying all the mapped words,
// and print them in lexicographical order.


// Input Format:
// -------------
// Line-1: An integer N, number of mapped pairs.
// Next N lines: Two space separated words, mappedpair[].
// Last Line: A line of words, the phrase.

// Output Format:
// --------------
// Print the list of mapped phrases in sorted order.


// Sample Input-1:
// ---------------
// 3
// hi hello
// sweet sugar
// candy chocolate
// hi sam! ram has a sugar candy

// Sample Output-1:
// ----------------
// [hello sam! he has sugar candy, hello sam! he has sugar chocolate, 
// hello sam! he has sweet candy, hello sam! he has sweet chocolate, 
// hi sam! he has sugar candy, hi sam! he has sugar chocolate, 
// hi sam! he has sweet candy, hi sam! he has sweet chocolate]



// Sample Input-2:
// ---------------
// 2
// hi hey
// hey hello
// hi how are you

// Sample Output-2:
// ----------------
// [hello how are you, hey how are you, hi how are you]