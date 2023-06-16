def fun(arr,n,t):
    for i in range(n):
        if arr[i]==t:
            print(i)
    return -1
        

n=6
arr=[1,4,2,5,9,8]
t=5
fun(arr,n,t)
