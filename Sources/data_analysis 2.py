#Data Analysis part -----------------------------------------------------------------------------------------------------------------------
#1) correlation analysis
#2) statistcis summary
#3) group aggragetion 

import pandas as pd

class DataAnalysis: #the following class does data analysis by finding correlations between attributes,does  statistical summary and aggregation by grouping data.
    def __init__(self, file):
        self.df = pd.read_csv(file)

    def vaccination_death_correlation_rate(self):  # 1.1 correlation analysis #finds correlatiion between vaccionation and death rate
        data = self.df[['fully_vaccinated_rate','deaths_per_million']]#.dropna()
        mean_for_vaccination = data['fully_vaccinated_rate'].mean() #computes the mean for vaccination in order to make comparisons
        high_vacc_rate = data[data['fully_vaccinated_rate']>= mean_for_vaccination]['deaths_per_million'].mean()# first it looks for the rate that is above average then for that specific rates it finds the avg of death 
        low_vacc_rate = data[data['fully_vaccinated_rate']< mean_for_vaccination]['deaths_per_million'].mean() #first it looks for the rate that is belowaverage then for that specific rates it finds the avg of death 
        
        if high_vacc_rate > low_vacc_rate: #checks whether for high vaccination rate the death average was high or low
            print("Countries with higher vaccination had more death rates")
        else:
            print("Countries with higher vaccination had less death rates")

    def population_cases_correlation(self):  # 1.2 correlation analysis #finds correlation among population cases and total cases
        data = self.df[['population', 'total_cases']]
        mean_population = data['population'].mean() #computes the avg for the population attribute
        large_population = data[data['population'] >= mean_population]['total_cases'].mean() #firstly it looks for the rate that is above above avg then for that specific rates it computes the mean for total cases
        small_population = data[data['population'] < mean_population]['total_cases'].mean()  #firstly it looks for the rate that is below  above avg then for that specific rates it computes the mean for total cases
        if large_population>small_population: # makes a comparison between to see whther for larger population there were more or less total cases
            print("Countries with larger population had higher total cases")
        else:
            print("Countries with larger population had lower total cases")
    
    def vaccination_total_cases_correlation_rate(self): #1.3 makes correlaation between vaccination rate and total cases
        data = self.df[["fully_vaccinated_rate", "total_cases"]]
        mean_for_vaccination = data['fully_vaccinated_rate'].mean() #computes mean for the vaccination rate
        high_vacc_rate = data[data['fully_vaccinated_rate']>=mean_for_vaccination]["total_cases"].mean() #first it looks for the rate that is above average then for that specific rates it finds the avg of total cases
        low_vacc_rate = data[data['fully_vaccinated_rate'] < mean_for_vaccination]["total_cases"].mean() #first it looks for the rate that is above average then for that specific rates it finds the avg of total cases
        if high_vacc_rate>low_vacc_rate: #makes a comparison to see whether for high vaccionation rate there were more total cases or not
            print("Countries with higher vaccination had more total cases")
        else:
            print("Countries with higher vaccination had less total cases")
  #2----------------------------------------------------------------------------------------------------------------------------------------
    
    def statistical_summary(self): #2.1 statistics 
        columns = ['total_cases', 'total_deaths', 'deaths_per_million', 'fully_vaccinated_rate'] # selects those specific attributes 
        data = self.df[columns] 
        print(f"Statistical summary:\n{data.describe()}") 
# Also shows some other statistics regarding the data set
        print(f"Median total_cases: {data['total_cases'].median()}") 
        print(f"Median total_deaths: {data['total_deaths'].median()}")
        print(f"Median deaths_per_million: {data['deaths_per_million'].median()}")
        print(f"Median fully_vaccinated_rate:{data['fully_vaccinated_rate'].median()}")

#3------------------------------------------------------------------------------------------------------------------------------------------------
    def aggregation_by_year(self): #3.1 aggregation 
      
        years = self.df['year'].unique() #finds unique years
        for year in sorted(years): #sorts those unique years and iterates over those years 
            year_data = self.df[self.df['year'] == year] #filters the rows with that represent the current year
            mean_cases = year_data['total_cases'].mean() #computes avg cases according to that specific year
            mean_deaths = year_data['total_deaths'].mean() #computes avg death cases according to that specific year
        print(f"{year} mean cases: {mean_cases}, mean deaths: {mean_deaths}")

#checking 1.1, 1.2 and 1.3
#analysis = DataAnalysis("cleaned_data.csv")

#print("Correlation summary")
#print(analysis.vaccination_death_correlation_rate())
#print(analysis.population_cases_correlation())
#print(analysis.vaccination_total_cases_correlation_rate())
#2.1
#print(analysis.statistical_summary())
#3.1
#print("Aggregation by year")
#print(analysis.aggregation_by_year())
