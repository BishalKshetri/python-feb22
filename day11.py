# TUPLES
# Can't change when running stage
# If we need any changes, we need to convert to the list and make changes and then we can convert to tuples again.

# a = (1,2,3,4,5,6)
# data = list(a) # converting to list
# data.pop()
# print(data)
# a = tuple(data) # converting to tuples
# print(a)
# print(a[0])
# hip memory , what is it ? 

# set
# doesn't support duplicate data, multiple 2 are there then only 2 will give here
# can be accessed by loops
# a = {1,1,1,1,2,2,2,2,"test","hello",5} # doesn't stay in order, hard to access data
# print(a)

# creating list and removing duplicates

num = [1,2,3,4,4,4,5]
num = list(set(num))
print(num)