from statistics import variance, stdev
# واریانس و انحراف معیار
# انحراف معیار: پراکندگی داده ها از میانگین
data = [2, 4, 6, 8, 10]

Variance = variance(data)
standard_deviation = stdev(data)

print("Variance : ", Variance)
print("Standard Deviation : ", standard_deviation)
