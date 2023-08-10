arr = [64, 25, 12, 22, 11]


def SelectionSort(unsortedArray):
    for i in range(len(unsortedArray)):
        minIndex = i
        for j in range(i+1, len((unsortedArray))):
            if (unsortedArray[j] < unsortedArray[minIndex]):
                minIndex = j

        unsortedArray[i], unsortedArray[minIndex] = unsortedArray[minIndex], unsortedArray[i]

    return arr


result = SelectionSort(arr)
print(result)
