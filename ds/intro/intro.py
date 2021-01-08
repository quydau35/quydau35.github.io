"""
Script cơ bản visualize Calorie tiêu thụ theo mạch đập trung bình, sử dụng linear regression
"""
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import os

file_name = "data.csv"
file_path = os.path.join(os.path.dirname(__file__), file_name)
full_health_data = pd.read_csv(file_path, header=0, sep=",")

x = full_health_data["Average_Pulse"]
y = full_health_data["Calorie"]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    """
    return data từ đồ thị tuyến tính ```y = ax + b``` với ```a = slope``` và ```b = intercept```
    """
    return slope * x + intercept

mymodel = list(map(myfunc, x))
print(mymodel)

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.ylim(ymin=0, ymax=2000)
plt.xlim(xmin=0, xmax=200)
plt.xlabel("Mạch trung bình")
plt.ylabel ("Calorie tiêu thụ")
plt.show()

#Two lines to make our compiler able to draw:
output_file = os.path.join(os.path.dirname(__file__),'intro.png')
plt.savefig(output_file)

