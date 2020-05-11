pos=-1

def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2

        if(list[mid]==n):
            globals()['pos']=mid
            return True
        else:
            if(list[mid]<n):
                l=mid+1
            else:
                u=mid+1        


list=[8,3,45,7,8]
n=int(input("Enter number for search"))
if(search(list,n)):
    print("Found",pos+1)
else:
    print("Not found")    
    #
