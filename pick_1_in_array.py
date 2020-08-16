#this method return the unique number of the array
def find_unique_number(array):
    array_length = len(array)
    array_set = set()
    array_set.add(array[0])

    for item in range(1,len(array)):
        set_len = len(array_set)
        array_set.add(array[item])

        if set_len != len(array_set):
            if array_length!=item+1 :
                if (array[item] == array[item+1]) :
                    return array[item-1]
            return array[item]
