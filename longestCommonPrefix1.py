def longestCommonPrefix(strs):

        if len(strs) == 1:
            return ''.join(strs[0])

        prefix = []
        for i, j in zip(strs[0], strs[1]):
            if i == j:
                prefix.append(i)
            else:
                break
        strs[1] = prefix
        return longestCommonPrefix(strs[1:])

print(longestCommonPrefix(["flower","flow","flight"]))