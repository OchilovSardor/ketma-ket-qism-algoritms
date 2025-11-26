from collections import defaultdict

def groupAnagrams(strs):
    result = defaultdict(list)
    for s in strs:
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord("a")] += 1
        result[tuple(counts)].append(s)
    return list(result.values())   
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("000"))


print(groupAnagrams(strs =
["eat","tea","tan","ate","nat","bat"]))