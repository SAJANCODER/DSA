def reverse_string(string):
    n=string[::-1]
    return n

string=input("enter string:")
print("String:",string)
reversed_string=reverse_string(string)
if (reversed_string==string):
    print("palindrone")
else:
    print("not palindrone")


print("reversed string:",reversed_string)
