def bubbleSort(numbers):
    
    n = len(numbers)
    for i in range(n-1):
        for j in range(n-1-i):
            # Сравниваем соседние элементы j и j+1
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    
    return numbers

numbers = [34, 12, 5, 67, 23, 5, 2, 50, 11, 7, 30, 1, 88, 56, 14, 4, 72, 25]
sortedArr = bubbleSort(numbers)
print(bubbleSort(numbers))

nums =[12,45,119,2,4,25,57]
n = len(nums)

#сортировка вставками
def InsertionSort(nums):
    for i in range(1, n):
        curentElement = nums[i] #текущий элемент 
        j = i - 1 #индекс предыдущего элемента
        while j >= 0 and nums[j] > curentElement:
            nums[j+1] = nums[j]
            j -=1
        
        nums[j+1] = curentElement 
    return nums

print(f"сортировка вставками: {InsertionSort(numbers)}")


    

