# reserve keyword findout
import keyword
print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 
# 'assert', 'async', 'await', 'break', 'class', 
# 'continue', 'def', 'del', 'elif', 'else', 
# 'except', 'finally', 'for', 'from', 'global', 
# 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
#  'not', 'or', 'pass', 'raise', 'return', 'try', 
# 'while', 'with', 'yield']
name = 10
print(type(name))    #it returens the data type of the given value
print(id(name))     #it returens the id of the given value 
print("integer")
#decimal number
var = 123
print(type(var))
print("decimal")
#  binary number
bvar = 0b1111
print(type(bvar))
print(bvar)
print("binary")
# octal number
ovar = 0o3133
print(type(ovar))
print(ovar)
print("octal")
#  hexadecimal form
hvar = 0XFACE
print(type(hvar))
print(hvar)
print("hexadecimal")
# dec, bin , hex , oct 

#  complex number form
cvar = 20 + 40j
print(type(cvar))
print("complex number")
