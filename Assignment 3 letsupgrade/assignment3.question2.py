#Question 2
#Take two lists as input list1 = [1,2,3,4,5] list2=[“a”, ”b”, ”c”, ”d”, ”e”] From that make a dictionary output {1:“a”, 2:”b”, 3:”c”, 4:”d”, 5:”e”}
#Program

list1 = [1,2,3,4,5]
list2 = ["a", "b", "c", "d", "e"]
dictionary = dict(zip(list1,list2))
print(dictionary)