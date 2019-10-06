class BubbleSort:
    def bubblesort(self, arr):
        #记录最后一次交换的位置
        # lastExchangePosition = 0
        # 无序数列额边界，每次比到这里就i行了
        # sortBorder = len(arr) - 1    
        
        for i in range(len(arr)):
            # 优化(1): 加入bool类型的有序/无序判断， 如果发现了有序的话，就不需要把循环全部做完
            # 每一轮开始的时候，认为是有序的
            isSorted = True
            for j in range(i+1, len(arr)):
                if arr[i] >= arr[j]:
                    self.swap(arr,i,j)
                    # 因为发生了交换，此时肯定是无序的
                    isSorted = False
          #          lastExchangePosition = j
           # sortBorder = lastExchangePosition
            # 当有序的时候，直接跳出
            if isSorted:
                break
        return arr
    
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j] 
        arr[j] = temp

sol = BubbleSort()
print(sol.bubblesort([5,8,6,7,4,3,7,1]))
print(sol.bubblesort([5,8,6,3,9,2,1,7]))
print(sol.bubblesort([3,4,2,1,5,6,7,8]))
