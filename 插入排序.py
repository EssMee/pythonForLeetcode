class InsertSort:
    def insertSort(self, arr):
        for i in range(1, len(arr)):
            for j in range(i,0,-1):
                if arr[j] < arr[j-1]:
                    self.swap(arr, j, j-1)
                else:
                    break
        return arr
    def swap(self, arr, i, j):
        temp = arr[i] 
        arr[i] = arr[j]
        arr[j] = temp

sol = InsertSort()
print(sol.insertSort([5,4,3,2,1]))
    
