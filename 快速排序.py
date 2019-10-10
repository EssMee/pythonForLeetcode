class Quick_Sort(object):
    ## 为什么不对啊？ ？ 
    def quickSort(self, arr, start, end):
        # "rtype": List[]
        if start >= end:
            return 
        
        pviot = self.partition(arr, start, end)
        self.quickSort(arr, start, pviot-1 )
        self.quickSort(arr, pviot+1,end)

    # get the position of pviot
    # 双边循环法
    def partition1(self, arr, start, end):
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
        def partition1(self, arr, start, end):
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

    def partition2(self, arr, start, end):
        pviot = arr[start]
        mark = start
        
        for i in range(start+1, end+1):
            if arr[i] < pviot:
                mark += 1
                temp = arr[i]
                arr[i] = arr[mark]
                arr[mark] = arr[i]
            
        
        arr[start] = arr[mark]
        arr[mark] = pviot
        return mark
                

        
sol = Quick_Sort()
test = [5,8,7,6,1,3,2]
print(sol.quickSort(test, 0,len(test) -1 ))
