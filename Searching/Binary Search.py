def bs(arr,t):
    n=len(arr)
    l=0
    h=n-1
    m=0
    while l<=h:
        m=(l+h)//2
        if arr[m]==t:
            print(m)
            break
        elif arr[m]<t:
            l=m+1
        else:
            h=m-1
    return -1


arr=[1,2,3,4,5,6,7,8]
bs(arr,3)
    
