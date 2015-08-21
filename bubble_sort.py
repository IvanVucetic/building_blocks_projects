def bubbleSort(list):
    k = 1
    while k < len(list):
        for i in range(len(list)-k):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
        print list
        k += 1


a = [2, 1, 6, 4, 3]

bubbleSort(a)        