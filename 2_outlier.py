# داده های پرت
def detect_outliers(data: list[int]) -> list[int]:
    outliers = []
    threshold = 1.5  # آستانه مشخص کننده داده‌های پرت
    mean = sum(data) / len(data)
    # محاسبه انحراف معیار
    std_dev = (
        sum(
        (x - mean) ** 2 for x in data) / len(data)
    ) ** 0.5

    for x in data:
        z_score = (x - mean) / std_dev
        if abs(z_score) > threshold:
            outliers.append(x)
    return outliers

data = [1, 2, 3, 4, 100]
outliers = detect_outliers(data)
print("outliers are : ", outliers)
