"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

"""

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    from collections import defaultdict
    
    anagrams_group = defaultdict(list)

    for word in strs:
        counter = [0]*26
        for c in word:
            counter[ord(c) - ord("a")] += 1
        
        
        anagrams_group[str(counter)] += [word]

    return list(anagrams_group.values())





print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))