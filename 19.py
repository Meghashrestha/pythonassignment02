# 19. Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
# These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid
open_list = ["[","{","("]
close_list = ["]","}",")"]

def validity(myStr):
	stack = []
	for i in myStr:
		if i in open_list:
			stack.append(i)
		elif i in close_list:
			pos = close_list.index(i)
			if ((len(stack) > 0) and
				(open_list[pos] == stack[len(stack)-1])):
				stack.pop()
			else:
				return "Unbalanced"
	if len(stack) == 0:
		return "Balanced"
	else:
		return "Unbalanced"


string = "{[]{()}}"
print(string,"-", validity(string))

string = "[{}{})(]"
print(string,"-", validity(string))

string = "((()"
print(string,"-",validity(string))
