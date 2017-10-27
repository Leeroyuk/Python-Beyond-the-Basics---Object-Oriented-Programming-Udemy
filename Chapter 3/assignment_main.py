from assignments import MaxSizeList  # assumes "class MaxSizeList"
                                     # is in a script called "assignments.py"

a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

print(a.get_list())
print(b.get_list())