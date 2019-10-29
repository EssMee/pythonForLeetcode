import time
class QuickSort:
    def quickSort(self ,arr:list):
        self.__quickSort(arr, 0, len(arr))
        return arr

    # 私有函数对[l,r]区间内进行快速排序
    def __quickSort(self, arr:list,l,r):
        if l >= r: return
        p = self.__partition(arr, l, r)
        self.__quickSort(arr,0,p)
        self.__quickSort(arr, p+1, r)
        
    
    def __partition(self, arr:list, l, r):
        v = arr[l]
        j = l
        for i in range(l+1,r):
            if arr[i] < v:
                self.swap(arr, j+1, i)
                j += 1
        
        self.swap(arr, l, j)
        return j
    
    def swap(self,arr:list,i,j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

sol = QuickSort()
print("algo starts at: " + time.ctime())
print(sol.quickSort([10,9,8,7,6,5,4,3,2,1]))
print("algo ends at: " + time.ctime() )
