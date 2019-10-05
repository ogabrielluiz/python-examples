#Convert list into a Dictionary using python
  
#Input
list1=[1,2,3,4,1,2,7]

#Declaring a dictionary
d={}

# Using a for loop to iterate over the elements of the list
for i in list1:
#checking if the dictionary already has the element or not
    if i in d:
        d[i]+=1
    else:
        d[i]=1
#Final output required
print d

