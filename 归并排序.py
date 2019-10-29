class MergeSort:
    def mergeSort(self, arr):
        """
        注意,i和j代表两个已经排序好的数组，当前正在考虑的元素索引。
        k表示经过比较之后，应该放入的索引位置。
        """
        self.__mergeSort(arr, 0, len(arr) - 1)
    
    # 对[l,r]区间内的数递归地进行排序
    def __mergeSort(self, arr, l , r):
        if l > r:
            return 
        mid = ( l + r ) / 2 
        self.__mergeSort(arr, 0, mid)
        self.__mergeSort(arr, mid + 1, r)
        # 最后，对排序完成的两部分进行merge操作
        self.__merge(arr, l, mid , r)
    def __merge(self, arr, l, mid, r): # 将arr[l...mid]和[mid+1, r]的两部分进行归并
        aux = arr
        i, j = l, r
        for k in range(l, len(arr)):
            if i > mid:
                arr[k] = aux[j]
                j += 1
            elif j > r:
                arr[k] = aux[i]
                i += 1
        
            elif aux[i] < aux[j]:
                arr[k] = aux[i]
                i += 1
            else:
                arr[k] = aux[j]
                j += 1
sol = MergeSort()
print(sol.mergeSort([5,4,3,2,1]))
