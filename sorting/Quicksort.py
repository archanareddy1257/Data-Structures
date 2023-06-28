class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low<high:
            q=self.partition(arr,low,high)
            self.quickSort(arr,low,q-1)
            self.quickSort(arr,q+1,high)
        return arr
    def partition(self,arr,low,high):
        # code here
        y=low
        for i in range(low,high):
            if arr[i]<=arr[high]:
                arr[i],arr[y]=arr[y],arr[i]
                y+=1
        arr[y],arr[high]=arr[high],arr[y]
        return y

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
