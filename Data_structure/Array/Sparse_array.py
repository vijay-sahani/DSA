"""
There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.

Example
4
aba
baba
aba
xzxb
3
aba
xzxb
ab

There are  instances of ',  of '' and  of ''. For each query, add an element to the return array, .

Function Description

Complete the function matchingStrings in the editor below. The function must return an array of integers representing the frequency of occurrence of each query string in strings.

matchingStrings has the following parameters:

string strings[n] - an array of strings to search
string queries[q] - an array of query strings
"""



def matchingStrings(strings, queries):
    occ=[]
    for i in range(len(queries)):
        count=0
        for j in range(len(strings)):
            if queries[i]==strings[j]:
                count+=1
        occ.append(count)
    return occ
string=[]
queries=[]