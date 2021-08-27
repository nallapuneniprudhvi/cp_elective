# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest 
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to 
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"

def longestcommonsubstring(s1, s2):
    # Yourcode goes here
    start = 0
    end = len(s2)
    l = [[0 for i in range(len(s2)+1)] for j in range(len(s1) + 1)]
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1): 
            if s1[i-1] == s2[j-1]:
                print(s1[i-1])
                print("i,j",l[i-1][j-1]+1)
                l[i][j] = l[i-1][j-1] + 1
                if l[i][j] >= start:
                    start = l[i][j]
                    end = i
    return s1[end - start: end]
