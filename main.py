from DataMax import DataMax

details = DataMax("Australia")
getDetails = details.countries()
print(getDetails)

import pandas as pd

countries = pd.read_excel('Project_File.xlsx')
print(countries)

country = countries.iloc[0:122, 30:35]
print(country)

total = countries.iloc[0:122, 30:35].sum()
df = pd.DataFrame(total, columns=['Total visitors'])
print(df)

newdf = df.sort_values(by='Total visitors', ascending=0)
print(newdf.head(3))
print(newdf)


ax = newdf.plot(kind='bar', title='Total visitors in other countries', xlabel='Countries', ylabel='Total visitors * 10000000', figsize=(15, 15), legend=True, fontsize=10)
my_fig = ax.get_figure()
my_fig.savefig("Total_visitors_HP.png")
