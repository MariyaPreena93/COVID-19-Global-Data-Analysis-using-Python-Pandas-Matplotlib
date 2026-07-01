import pandas as pd
import matplotlib.pyplot as plt


data =pd.read_csv("COVID_19.csv")
final_data = data.drop_duplicates().dropna(subset=["continent","location","date"])
before =len(data)
after = len(final_data)

print("Total records before cleaning:",before)
print("Total records after cleaning:",after)

final_data["date"]=pd.to_datetime(final_data["date"],format="%d-%m-%Y")
cols = [
    "total_cases",
    "new_cases",
    "total_deaths",
    "new_deaths",
    "total_tests",
    "people_vaccinated"
]
final_data[cols] = final_data[cols].apply(pd.to_numeric, errors="coerce")

#Total Cases by Continent

df =final_data.groupby("continent")["total_cases"].max().sort_values(ascending=False)
plt.bar(df.index,df.values,color='lightcoral',width=0.5)
plt.xlabel("Continent")
plt.ylabel("Total cases")
plt.title("COVID-19 Total Cases by Continent")
plt.xticks(rotation=45)
plt.savefig("continent_cases.png")
plt.show()

#Top 10 Countries by Total Cases
top =final_data.groupby("location")["total_cases"].max().nlargest(10)
plt.barh(top.index,top.values,color ='orchid',height=0.3)
plt.xlabel("Country")
plt.ylabel("Total Cases")
plt.title("Top 10 Countries by Total Cases")
plt.savefig("Top10countries_cases.png")
plt.show()

#Top 10 Countries by Deaths
df = final_data.groupby("location")["total_deaths"].max().nlargest(10)
plt.barh(df.index,df.values)
plt.xlabel("country")
plt.ylabel("total_deaths")
plt.title("Top 10 Countries by Total Deaths")
plt.savefig("Top10countries_Deaths.png")
plt.show()

#Monthly New Cases Trend in Canada 
final_data["month_year"] = final_data["date"].dt.to_period("M")
Trnd = final_data[(final_data["month_year"]>"2020-12") & (final_data["location"]=="Canada")].groupby("month_year")["new_cases"].sum()
plt.plot(Trnd.index.astype(str),Trnd.values,marker='o',ms=10,ls='--',c='pink',mec='k',mfc='pink')
plt.xlabel("month_year")
plt.ylabel("New cases")
plt.title("New Cases Trend in Canada")
plt.xticks(rotation=45)
plt.savefig("newcase_trend_Canada.png")
plt.show()

#Daily death Trend in India

data=final_data[final_data["location"]=="India"].groupby("date")["new_deaths"].sum()
plt.plot(data.index,data.values,c='green')
plt.xlabel("date")
plt.ylabel("Deaths")
plt.title("Daily death Trend in India")
plt.xticks(rotation=45)
plt.savefig("DeathTrend_India.png")
plt.show()

#total cases vs total death
latest = (final_data.sort_values("date").groupby("location").last())
x=latest["total_cases"]
y=latest["total_deaths"]
plt.scatter(x,y,c='grey')
plt.xlabel("total_cases")
plt.ylabel("total_deaths")
plt.title("Total_cases vs Total_death")
plt.savefig("casesvsDeath.png")
plt.show()

print("------Summary------")

print("Records before cleaning:", before)
print("Records after cleaning:", after)
print("Countries:", final_data["location"].nunique())
print("Continents:", final_data["continent"].nunique())

print("Latest Date:", final_data["date"].max())

print("Total Cases:",
      final_data["total_cases"].max())

print("Total Deaths:",
      final_data["total_deaths"].max())

summary = pd.DataFrame({
    "Metric":[
        "Records Before Cleaning",
        "Records After Cleaning",
        "Countries",
        "Continents"
    ],
    "Value":[
        before,
        after,
        final_data["location"].nunique(),
        final_data["continent"].nunique()
    ]
})

summary.to_csv("summary_report.csv",index=False)
 
