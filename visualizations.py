import os
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np 

os.makedirs("graphs", exist_ok = True)

class Visualizations:
    def __init__(self, file):
        self.df = pd.read_csv(file)

# method to create vizualization on the connection between total_deaths and vaccination_rate

    def connect_deaths_vaccine(self): #scatter plot 
        """Creates a scatterplot showing the correlation between total_deaths and vaccinations"""
        plt.figure(figsize = (10, 6))
        plt.scatter(self.df['total_deaths'], self.df['vaccinated_rate'], alpha = 0.5, color = 'blue', edgecolors = 'w')
        plt.title("Correlation between number of deaths and vaccination amounts.")
        plt.xlabel("Number of deaths")
        plt.ylabel("Vaccinations")
        plt.savefig("graphs/scatterplot.png")
        plt.show()
        plt.close()

         
    def show_deaths_p_million_per_country(self): # boxplot
        """
            Creates a boxplot showing hte distribution of deaths casued by Covid - 19, showing their means, medians, quartiles.
        """
        top_10 = self.df[self.df["year"] == 2020].nlargest(10, "total_deaths")["country"]
        filtered = self.df[self.df["country"].isin(top_10)]
        plt.figure(figsize = (12, 8))
        sns.boxplot(data = filtered, x= "total_deaths", y = "country")
        plt.tight_layout()
        plt.savefig("graphs/boxplot_final.png")
        plt.show()
        plt.close()

         
    def show_deaths_p_million_per_country_bars(self): # boxplot
        """
            Creates a barplot summarizing hte number of deaths in each country.
        """
        top_10 = self.df[self.df["year"] == 2020].nlargest(10, "total_deaths")["country"]
        filtered = self.df[self.df["country"].isin(top_10)]
        plt.figure(figsize = (12, 8))
        sns.barplot(data = filtered, x= "total_deaths", y = "country", color ="green")
        plt.tight_layout()
        plt.savefig("graphs/barplot.png")
        plt.show()
        plt.close()

         
    def correlate_total_case_and_death(self): # bubbles represent countries where the population was significantly higher
        """
            Correlates total cases and death cases through a scatterplot.
        """
        plt.figure(figsize = (10, 6))
        scatter = plt.scatter(self.df["total_cases"], self.df["total_deaths"], s = self.df["population"]/10000000, alpha = 0.6) # populations were too large so decided to divide by the number to scale them
        plt.title("Bubble plot correlating between cases, deaths and populations.")
        plt.xlabel("Number of cases")
        plt.ylabel("Number of deaths")
        plt.savefig("graphs/bubble.png")
        plt.show()
        plt.close()

    
    def density_plot(self):
        """
            Creates density graphs, showing the distribution of cases in years 2020,2021, and 2022. Shows the skew of the statistical distribution.
        """
        data_df = self.df[self.df["year"].isin([2020,2021,2022])]
        data_df = data_df[data_df["total_cases"] > 0]
        plt.figure(figsize = (12,8))
        sns.kdeplot(data = data_df,x = "total_cases", hue= "year", common_norm=False, fill = True, log_scale = True)
        plt.title("Density plot with years")
        plt.savefig("graphs/density_plot_with_years.png")
        plt.show()
        plt.close()
 
    def line_chart(self):
        """
            Uses time-series analysis and shows how the number of Covid cases progressed from 2020 to 2022 in distinct countries though a line chart.
        """
        total_deaths = self.df.groupby("country")["total_deaths"].sum()
        countries = total_deaths.nlargest(10).index.tolist()
        plot_data = self.df[self.df["country"].isin(countries)]
        plt.figure(figsize = (12,8))
        sns.lineplot(data = plot_data, x = "year", y = "total_cases", hue = "country", marker = "o")
        plt.title("Covid-19 Time Series Analysis by countries from 2020 to 2022.")
        plt.xlabel("Year")
        plt.ylabel("Total Cases")
        plt.xticks([2020,2021,2022])
        plt.tight_layout()
        plt.savefig("graphs/line_chart.png")
        plt.show()
        plt.close()

    
        
#dataset = Visualizations('cleaned_data.csv')
#print(dataset.connect_deaths_vaccine())
#print(dataset.show_deaths_p_million_per_country())
#print(dataset.show_deaths_p_million_per_country_bars())
#print(dataset.correlate_total_case_and_death())
#print(dataset.density_plot())
#print(dataset.line_chart())