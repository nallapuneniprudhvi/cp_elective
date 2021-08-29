# limitedPowerSet(n, k)
# Write a function limitedPowerSets(n, k) that takes possibly 
# a non-negative integer n and k and returns the list that 
# contains k number of subsets from the power set as sets. 
# (The values in the set will range from 1 to n).
# Example:
# 	limitedPowerSet(5, 7) => 
# [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ]


import itertools
def limitedPowerSet(n, k):
    values = list()
    lis = [{}]
    for i in range(1, n+1):
        values.append(i)
    for i in range(1, len(values)+1):
        combi_list = list(map(set, itertools.combinations(values,i)))
        for j in range(len(combi_list)):
            if len(lis) != k:
                lis.append(combi_list[j])
            else:
                return lis
 
assert(limitedPowerSet(5, 7) == [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ])
assert(limitedPowerSet(6,10) == [{}, {1}, {2}, {3}, {4}, {5}, {6}, {1, 2}, {1, 3}, {1, 4}])
assert(limitedPowerSet(8,19) == [{}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {1, 2}, {1, 3}, {1, 4}, {1, 5}, {1, 6}, {1, 7}, {8, 1}, {2, 3}, {2, 4}, {2, 5}])
print("\nAll test cases passed...!")