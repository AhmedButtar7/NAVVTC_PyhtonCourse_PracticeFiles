import pandas as pd
import matplotlib.pyplot as plt

# Download the dataset
download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv"
df = pd.read_csv(download_url)

# Scatter plot: Median salary vs. Unemployment rate
plt.scatter(df["Median"], df["Unemployment_rate"])
plt.xlabel("Median Salary")
plt.ylabel("Unemployment Rate")
plt.title("Median Salary vs. Unemployment Rate for College Majors")
plt.grid(True)
plt.show()

plt.plot(df["Median"], df["Unemployment_rate"], 'o:g')
plt.xlabel("Median Salary")
plt.ylabel("Unemployment Rate")
plt.title("Median Salary vs. Unemployment Rate for College Majors")
plt.show()


