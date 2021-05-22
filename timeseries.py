import quandl
import matplotlib.pyplot as plt
# Getting time seies data

Stock_data = quandl.get("BSE/BOM500209", api_key="TtZtaGu6jwgrTF9wDky3")
print(Stock_data.tail())
print("\n\n")
print(Stock_data.columns)

Stock_data[['Open', 'Total Turnover']].plot(subplots=True, legend=False)
plt.show()

