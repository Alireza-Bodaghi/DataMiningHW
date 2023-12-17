#%%
import numpy as np
import matplotlib.pyplot as plt

# پارامترهای توزیع نرمال
mean = 170
std_dev = 5

# تولید یک نمونه تصادفی از توزیع نرمال
sample = np.random.normal(mean, std_dev, 1000)


# رسم نمودار توزیع نرمال
plt.hist(
    sample, 
    bins=30, 
    density=True, 
    alpha=0.7, 
    color='blue'
)

# تنظیم نام محور x و y
plt.xlabel('Height (Centimeter)') # قد (سانتی‌متر)
plt.ylabel('probability density') # چگالی احتمال

# نمایش نمودار
plt.show()

# %%
