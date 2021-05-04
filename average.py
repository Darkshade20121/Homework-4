def average_list(list):
    average = 0
    for i in range(len(list)):
        average = average + list[i]
    average = average/len(list)
    return average
