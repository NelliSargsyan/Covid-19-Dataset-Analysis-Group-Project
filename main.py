import numpy as np
import pandas as pd
from Sources.data_analysis import DataAnalysis
from Sources.visualizations import Visualizations

class DataCleaning:  #Data Cleaning and prepocessing
    def __init__(self, file):  #reading the dataset file
        self.df = pd.read_csv(file)

    def missing_data(self):  #for the initial stage - to see how many missing values
        missing = self.df.isnull().sum()
        return missing 

    def remove_mostly_empty_rows(self, missing = 7):  #remove the rows where we have more than 7 missing values
        missing_per_row = self.df.isnull().sum(axis=1)
        self.df = self.df[missing_per_row < missing]
        #return(self.df.isnull().sum())
    
    def quant_data(self):  #handle the missing values in numerical columns
        self.df['total_deaths'] = self.df['total_deaths'].fillna(self.df['total_deaths'].mean()) #only 10 missing -> mean
        self.df['total_cases'] = self.df['total_cases'].fillna(self.df['total_cases'].mean()) #they had only 10, so mean
        self.df['population'] = self.df['population'].fillna(self.df['population'].median()) #we use this to not give small countries "fake" population
        self.df['cases_per_million'] = self.df['cases_per_million'].fillna(self.df['cases_per_million'].median())
        self.df['deaths_per_million'] = self.df['deaths_per_million'].fillna(self.df['deaths_per_million'].median())
        self.df.drop(columns=["booster_rate"], inplace=True) #dropping this column because it's mostly missing values 411/745
        self.df.drop(columns=["date"], inplace=True)  #year is the same

        np.random.seed(42)
        self.df.loc[self.df['vaccinated_rate'].isna(), 'vaccinated_rate'] = np.random.uniform(0, 0.35, self.df['vaccinated_rate'].isna().sum()) #values in vaccinated_rate are either missing, 0, or numbers between 0 and 0.35, so we handle the missing values by filling them with random numbers in (0, 0.35)
        self.df['fully_vaccinated_rate'] = self.df['vaccinated_rate'] * 0.9 #the average difference ratio for vaccinated_rate and fully_vaccinated_rate
        self.df.drop_duplicates(inplace = True)
        #return(self.df.isnull().sum())

    def save_cleaned_data(self, new_file): #saving cleaned data in a new dataset
        self.df.to_csv(new_file, index=False)

dataset = DataCleaning("covid_dataset_ready.csv")
cleaned_data = dataset.remove_mostly_empty_rows()
cleaned_data = dataset.quant_data()
dataset.save_cleaned_data("cleaned_data.csv")


#Data Analysis----------------------------------------------------------------------------------------------------------------------------------------

print("Data Analysis")
print("-" * 40)
analysis = DataAnalysis("cleaned_data.csv")

print("Correlation summary")
print(analysis.vaccination_death_correlation_rate())
print(analysis.population_cases_correlation())
print(analysis.vaccination_total_cases_correlation_rate())
#2.1
print(analysis.statistical_summary())
#3.1
print("Aggregation by year")
print(analysis.aggregation_by_year())
 
#Visualization----------------------------------------------------------------------------------------------------------------------------------------
print("Data Visualizations")
visualizations = Visualizations('cleaned_data.csv')
visualizations.connect_deaths_vaccine()
visualizations.show_deaths_p_million_per_country()
visualizations.show_deaths_p_million_per_country_bars()
visualizations.correlate_total_case_and_death()
visualizations.density_plot()
visualizations.line_chart()

