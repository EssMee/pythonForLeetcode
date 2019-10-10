class Quick_Sort(object):
    def quickSort(self, arr, start, end):
        # "rtype": List[]
        if start >= end:
            return 
        
        pviot = self.partition(arr, start, end)
        self.quickSort(arr, start, pviot-1 )
        self.quickSort(arr, pviot+1,end)

    # get the position of pviot
    def partition(self, arr, start, end):
        pivot = arr[start]
        left = start
        right = end
        
        # traverse from the right hand side
        while left != right:
            while  left < right and arr[right] > arr[pivot]:
                right -= 1
            while left < right and arr[left] <= arr[pivot]:
                left += 1
            
            if (left < right):
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp
            
        # when left = right
        # change the value of arr[left] and arr[pviot]
        arr[start] = arr[left] 
        arr[left] = pivot
        return left
    
        
sol = Quick_Sort()
test = [5,8,7,6,1,3,2]
print(sol.quickSort(test, 0,len(test) -1 ))
