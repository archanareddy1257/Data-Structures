class Solution:
    def selectionSort(self, arr,n):
            #code here
            for i in range(0,n):
                min=i
                for j in range(i+1,n):
                    if arr[min]>arr[j]:
                        min=j
                arr[i],arr[min]=arr[min],arr[i]
            return arr
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
