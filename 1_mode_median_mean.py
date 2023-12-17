from statistics import mode, median

# calculating mode. مد
data_sequence_1 = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 10]
mode_value = mode(data_sequence_1)
print("mode is :", mode_value )


# calculating median. میانه
median_value = median(data_sequence_1)
print("median is: ", median_value)

# میانگین
# calculating mean by creating our own mean function
def calculate_mean(numbers: list[int]) -> int:
    sum_value = sum(numbers)
    return sum_value/len(numbers)

data_sequence_2 = [2, 4, 6, 8, 10, 15, 25]
mean_value = calculate_mean(data_sequence_2)
print("mean is: ", mean_value)