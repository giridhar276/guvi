

name = "python programming"
print(name)

aname  = 'unix'
print(aname)

bname  = """java programming"""
print(bname)
# string[start:stop:step]
# string slicing
print(name[0])
print(name[1])
print(name[0:5])
print(name[5:9])
print(name[::])
print(name[:])
print(name[0:17:2])
print(name[1:17:2])
print(name[0:16:4])
print(name[-1])
print(name[-3:-1])
print(name[::-1])

# looping
# range(start,stop,step)
print("numbers from 1 to 9")
for val in range(1,10):
    print(val)
    
print("Even numbers")
for val in range(2,10,2):
    print(val)

print(" odd numbers")
for val in range(1,10,2):
    print(val)

## iterating string
print("Iterating string")
cname = "python"
for char in cname:
    print(char)



# methods
name = "python programming"

print(name.upper())
print(name.isupper())
print(name.islower())
print(name.count('p'))
print(name.count('z'))
print(name.replace('python','ruby'))
print(name.startswith('z'))
print(name.startswith('p'))
print(name.find('gra'))
# will display all the methods available for string name
print(dir(name))




    











