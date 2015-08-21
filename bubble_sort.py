def bubbleSort(list):
    k = 1
    while k < len(list):
        swap = 0
        for i in range(len(list)-k):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                swap += 1

        k += 1
        print list, swap
        if swap == 0: break
        	
        


a = [2, 1, 6, 4, 3, 7, 1, 2, 2, 9, 5]

bubbleSort(a)        