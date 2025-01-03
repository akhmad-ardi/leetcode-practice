from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for string in strs[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]   
            if not prefix:
                return ""   

    return prefix     

print(longestCommonPrefix(["flower", "flow", "flight"])) # fl          
print(longestCommonPrefix(["dog", "racecar", "car"])) # ""          
    