class Solution:
    def merge(self,arr, l, m, r): 
        # code here
        a=arr[l:m+1]
        b=arr[m+1:r+1]
        i,j,k=0,0,l
        while i<len(a) and j<len(b):
            if a[i]<b[j]:
                arr[k]=a[i]
                i+=1
                k+=1
            else:
                arr[k]=b[j]
                j+=1
                k+=1
        while i<len(a):
            arr[k]=a[i]
            i+=1
            k+=1
        while j<len(b):
            arr[k]=b[j]
            j+=1
            k+=1
            
    def mergeSort(self,arr,l,r):
        if l<r:
            m=(l+(r-1))//2
            self.mergeSort(arr,l,m)
            self.mergeSort(arr,m+1,r)
            self.merge(arr,l,m,r)
import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
