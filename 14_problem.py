# Leecode Problem 14 : Longest Common Prefix
strs = ["flower", "flow", "flight"]
if not strs:
    prefix = ""
else:
    prefix = ""
    
    for i in range(len(strs[0])):  # go character by character
        char = strs[0][i]
        
        for s in strs:
            # check boundary + mismatch
            if i >= len(s) or s[i] != char:
                print(prefix)
                exit()
        
        prefix += char

print(prefix)