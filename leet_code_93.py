#https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/
#Count the Number of Vowel Strings in Range
#You are given a 0-indexed array of string words and two integers left and right.
#A string is called a vowel string if it starts with a vowel character and ends with a vowel 
#character where vowel characters are 'a', 'e', 'i', 'o', and 'u'.
#Return the number of vowel strings words[i] where i belongs to the inclusive range [left, right].
#Input: words = ["are","amy","u"], left = 0, right = 2
#Output: 2
#Explanation: 
#- "are" is a vowel string because it starts with 'a' and ends with 'e'.
#- "amy" is not a vowel string because it does not end with a vowel.
#- "u" is a vowel string because it starts with 'u' and ends with 'u'.
#The number of vowel strings in the mentioned range is 2.
#Input: words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4
#Output: 3
#Explanation: 
#- "aeo" is a vowel string because it starts with 'a' and ends with 'o'.
#- "mu" is not a vowel string because it does not start with a vowel.
#- "ooo" is a vowel string because it starts with 'o' and ends with 'o'.
#- "artro" is a vowel string because it starts with 'a' and ends with 'o'.
#The number of vowel strings in the mentioned range is 3.

list(filter(lambda n: n[-1] =='a' or n[-1] =='e' or n[-1] =='o' or n[-1] =='i' or 
           n[-1]=='u',filter(lambda n: n[0] =='a' or n[0] =='e' or n[0] =='o' or n[0] =='i' 
              or n[0]=='u',[i for i in words if 'a' in i or 'e' in i or 'i' in i or 'o' in i or 'u' in i])))