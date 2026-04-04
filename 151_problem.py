# Leetcode Problem 151 : Reverse Words in a String
s = " the sky is blue "
s = s.strip() # "the sky is blue"
s = s.split() # "the" "sky" "is" "blue"
string = s.reverse() # "blue" "is" "sky" "the"
s = " ".join(s) # "blue is sky the"
print(s) # s = "blue is sky the"
