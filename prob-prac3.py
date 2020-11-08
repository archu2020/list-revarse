# list reversing

print("Enter the number of list one by one\n")
size=int(input("Enter the size of the list\n"))

mylist=[]

for i in range(size):
    mylist.append(int(input("Enter the numbrt of list \n")))
print(f"My original list is {mylist}")

revs1=mylist[:]
revs1.reverse()
print(f"the 1st reverse of {mylist} is {revs1}")

revs2=mylist[::-1]
print(f"the 2nd reverse of {mylist} is {revs2}")

revs3=mylist[:]
for i in range(len(mylist)//2):
    revs3[i],revs3[len(revs3)-i -1] = revs3[len(revs3)-i -1],revs3[i]
print(f"the 3rd reverse of {mylist} is {revs3}")

if revs1==revs2 and revs2==revs3:
    print("All method gives same resuls")
else:
    print("not gives the same ruselt")

