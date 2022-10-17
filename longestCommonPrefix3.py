def longestCommonPrefix(strs):
        common_prefix = ""
        for i in range(len(strs[0])):
            for s in strs:
              
                if i == len(s) or s[i] != strs[0][i]:
                    return common_prefix
 
            common_prefix += strs[0][i]
        return common_prefix

print(longestCommonPrefix(["flower","flow","flight"]))


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"