import pandas
import numpy
import matplotlib.pyplot as plt

clean_complete_data_frame = pandas.read_csv("covid_19_clean_complete.csv")

# print(clean_complete_data_frame, usa_data_frame, world_data_frame)
# print("DTypes:- ", clean_complete_data_frame.dtypes) # datatypes
# print(clean_complete_data_frame.head(10)) # top 10
# print(clean_complete_data_frame.to_numpy()) # convert to array
# print(clean_complete_data_frame.describe()) # summary

# clean_complete_data_frame.sort_index(axis=1, ascending=True)
# print(clean_complete_data_frame)

print(list(clean_complete_data_frame.columns))
clean_complete_data_frame.dropna()
clean_complete_data_frame = clean_complete_data_frame[["Date", "Country/Region", "Confirmed", "Recovered", "Deaths"]]
# clean_complete_data_frame = clean_complete_data_frame[clean_complete_data_frame["WHO Region"] == "paho"]
clean_complete_data_frame = clean_complete_data_frame[clean_complete_data_frame["Country/Region"] == "US"]
# print(clean_complete_data_frame)
clean_complete_data_frame = clean_complete_data_frame[["Date", "Confirmed", "Recovered", "Deaths"]]
clean_complete_data_frame.plot(x="Date", y=["Confirmed", "Recovered", "Deaths"])
plt.show()

# result_array = clean_complete_data_frame.to_numpy()
# print(result_array.tolist())

# plt.plot()


