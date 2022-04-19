#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 21:01:26 2022

@author: laurenodonnell
"""

# Research question
# Four follow up questions
# need to have at least 2 unit tests to test the data
# possibly write at least one function
# include some visualizations





# response variable will be the happiness score
# what is the most influential predictor on the happiness score of a country? (pick a year)
# how has the overall average of happiness changed over the years? 

import pandas as pd
import numpy as np
import seaborn as sb

data = pd.read_csv('Documents/Repos/DS_5100/Project_1/data_all.csv')
data = data.drop(columns = "Unnamed: 0")



# QUESTION: how has the overall happiness of countries changes over the years? 
sb.lineplot(data = data, x = "Year", y = "Happiness Score")
# Happiness generall appears to increase over the years overall. 
# What leads to happiness increases? 


# Investigating individual variable over the course of the years (in averages)
# Creating new dataframe that averages all of the columns by year
avgHappinessYr = data.groupby('Year').mean()
# dropping columns that are not needed for averages
avgHappinessYr = avgHappinessYr.drop(columns = ("Happiness Rank", "Standard Error", "Lower Confidence Interval", "Upper Confidence Interval", "Whisker.high", "Whisker.low"))

sb.lineplot(data = avgHappinessYr, x = "Year", y = "Economy (GDP per Capita)")
# GPD seems inconsistent in change, but clearly increases in 2021 and 2022 where the most increase is in happiness overall

sb.lineplot(data = avgHappinessYr, x = "Year", y = "Family")
# Family does not appear related to the overall happiness increase

sb.lineplot(data = avgHappinessYr, x = "Year", y = "Health (Life Expectancy)")
# Health does not appear consisent either, though there is a clear drop with COVID - when were these surveys sent in 2020 and 2022??

sb.lineplot(data = avgHappinessYr, x = "Year", y = "Freedom")

sb.lineplot(data = avgHappinessYr, x = "Year", y = "Trust (Government Corruption)")

sb.lineplot(data = avgHappinessYr, x = "Year", y = "Generosity")

sb.lineplot(data = avgHappinessYr, x = "Year", y = "Dystopia Residual")

# Interestingly, none of these variables seem to consistently align with overal happiness, but GDP seems to have the closest shape.
# Additionally, generosity over the years appears to have a steep decline. What is the relationship here?


# QUESTION: Do the countries with the highest and lowest happiness see the same changes in GDP, generosity, a happiness? 
# ordering dataset from happiness country to lowest and extracing the top 5
happiestData = data[data["Happiness Rank"] < 6]

# issue with using the countries with the lowest happiness level: there is a different number of countries reporting data over the years
# adjusting top 5 to top 15 so there is enough data
# happiestData.append(data["Happiness Rank"] > (data["Happiness Rank"].max() - 5)]

sb.lineplot(data = happiestData, x = "Year", y = "Happiness Score", hue = "Country")
# observed there is not necessarialy a consistent set of countries that is always ranked in the top 5 of the world in happiness. 

# Instead observing if there is a consistent variable that tends to be higher across these countries
sb.lineplot(data = happiestData, x = "Year", y = "Economy (GDP per Capita)", hue = "Country")
sb.lineplot(data = happiestData, x = "Year", y = "Family", hue = "Country")
sb.lineplot(data = happiestData, x = "Year", y = "Health (Life Expectancy)", hue = "Country")
sb.lineplot(data = happiestData, x = "Year", y = "Freedom", hue = "Country")
sb.lineplot(data = happiestData, x = "Year", y = "Trust (Government Corruption)", hue = "Country")
sb.lineplot(data = happiestData, x = "Year", y = "Generosity", hue = "Country")
sb.lineplot(data = happiestData, x = "Year", y = "Dystopia Residual", hue = "Country")
# Interestingly, each plot appears to have a very similar shape across all top countries. This may imply countries across the world had similar feelings toward each of these variables due to other influencing world events



# Now turning to look at each of the variables against happiness rank to explore any potential relationships
# starting with the overall model containing all predictors
sb.lineplot(data = data, x = "Economy (GDP per Capita)", y = "Happiness Score")


sb.scatterplot(data = data, x = "Economy (GDP per Capita)", y = "Happiness Score", hue = "Year")
sb.scatterplot(data = data, x = "Family", y = "Happiness Score", hue = "Year")
sb.scatterplot(data = data, x = "Health (Life Expectancy)", y = "Happiness Score", hue = "Year")
sb.scatterplot(data = data, x = "Freedom", y = "Happiness Score", hue = "Year")
sb.scatterplot(data = data, x = "Trust (Government Corruption)", y = "Happiness Score", hue = "Year")
sb.scatterplot(data = data, x = "Generosity", y = "Happiness Score", hue = "Year")
sb.scatterplot(data = data, x = "Dystopia Residual", y = "Happiness Score", hue = "Year")



data2015 = data[data["Year"] == 2015]
data2016 = data[data["Year"] == 2016]
data2017 = data[data["Year"] == 2017]
data2018 = data[data["Year"] == 2018]
data2019 = data[data["Year"] == 2019]
data2020 = data[data["Year"] == 2020]
data2021 = data[data["Year"] == 2021]
data2022 = data[data["Year"] == 2022]


# each year's Economy and Happiness Score
sb.scatterplot(data = data2015, x = "Economy (GDP per Capita)", y = "Happiness Score")
sb.scatterplot(data = data2016, x = "Economy (GDP per Capita)", y = "Happiness Score")
sb.scatterplot(data = data2017, x = "Economy (GDP per Capita)", y = "Happiness Score")
sb.scatterplot(data = data2018, x = "Economy (GDP per Capita)", y = "Happiness Score")
sb.scatterplot(data = data2019, x = "Economy (GDP per Capita)", y = "Happiness Score")
sb.scatterplot(data = data2020, x = "Economy (GDP per Capita)", y = "Happiness Score")
sb.scatterplot(data = data2021, x = "Economy (GDP per Capita)", y = "Happiness Score")
sb.scatterplot(data = data2022, x = "Economy (GDP per Capita)", y = "Happiness Score")


# each year's Family and Happiness Score
sb.scatterplot(data = data2015, x = "Family", y = "Happiness Score")
sb.scatterplot(data = data2016, x = "Family", y = "Happiness Score")
sb.scatterplot(data = data2017, x = "Family", y = "Happiness Score")
sb.scatterplot(data = data2018, x = "Family", y = "Happiness Score")
sb.scatterplot(data = data2019, x = "Family", y = "Happiness Score")
sb.scatterplot(data = data2020, x = "Family", y = "Happiness Score")
sb.scatterplot(data = data2021, x = "Family", y = "Happiness Score")
sb.scatterplot(data = data2022, x = "Family", y = "Happiness Score")

# each year's Health and Happiness Score
sb.scatterplot(data = data2015, x = "Health (Life Expectancy)", y = "Happiness Score")
sb.scatterplot(data = data2016, x = "Health (Life Expectancy)", y = "Happiness Score")
sb.scatterplot(data = data2017, x = "Health (Life Expectancy)", y = "Happiness Score")
sb.scatterplot(data = data2018, x = "Health (Life Expectancy)", y = "Happiness Score")
sb.scatterplot(data = data2019, x = "Health (Life Expectancy)", y = "Happiness Score")
sb.scatterplot(data = data2020, x = "Health (Life Expectancy)", y = "Happiness Score")
sb.scatterplot(data = data2021, x = "Health (Life Expectancy)", y = "Happiness Score")
sb.scatterplot(data = data2022, x = "Health (Life Expectancy)", y = "Happiness Score")

# each year's Freedom and Happiness Score
sb.scatterplot(data = data2015, x = "Freedom", y = "Happiness Score")
sb.scatterplot(data = data2016, x = "Freedom", y = "Happiness Score")
sb.scatterplot(data = data2017, x = "Freedom", y = "Happiness Score")
sb.scatterplot(data = data2018, x = "Freedom", y = "Happiness Score")
sb.scatterplot(data = data2019, x = "Freedom", y = "Happiness Score")
sb.scatterplot(data = data2020, x = "Freedom", y = "Happiness Score")
sb.scatterplot(data = data2021, x = "Freedom", y = "Happiness Score")
sb.scatterplot(data = data2022, x = "Freedom", y = "Happiness Score")

# each year's Trust and Happiness Score
sb.scatterplot(data = data2015, x = "Trust (Government Corruption)", y = "Happiness Score")
sb.scatterplot(data = data2016, x = "Trust (Government Corruption)", y = "Happiness Score")
sb.scatterplot(data = data2017, x = "Trust (Government Corruption)", y = "Happiness Score")
sb.scatterplot(data = data2018, x = "Trust (Government Corruption)", y = "Happiness Score")
sb.scatterplot(data = data2019, x = "Trust (Government Corruption)", y = "Happiness Score")
sb.scatterplot(data = data2020, x = "Trust (Government Corruption)", y = "Happiness Score")
sb.scatterplot(data = data2021, x = "Trust (Government Corruption)", y = "Happiness Score")
sb.scatterplot(data = data2022, x = "Trust (Government Corruption)", y = "Happiness Score")

# each year's Generosity and Happiness Score
sb.scatterplot(data = data2015, x = "Generosity", y = "Happiness Score")
sb.scatterplot(data = data2016, x = "Generosity", y = "Happiness Score")
sb.scatterplot(data = data2017, x = "Generosity", y = "Happiness Score")
sb.scatterplot(data = data2018, x = "Generosity", y = "Happiness Score")
sb.scatterplot(data = data2019, x = "Generosity", y = "Happiness Score")
sb.scatterplot(data = data2020, x = "Generosity", y = "Happiness Score")
sb.scatterplot(data = data2021, x = "Generosity", y = "Happiness Score")
sb.scatterplot(data = data2022, x = "Generosity", y = "Happiness Score")

# each year's Dystopia Residual and Happiness Score
sb.scatterplot(data = data2015, x = "Dystopia Residual", y = "Happiness Score")
sb.scatterplot(data = data2016, x = "Dystopia Residual", y = "Happiness Score")
sb.scatterplot(data = data2017, x = "Dystopia Residual", y = "Happiness Score")
sb.scatterplot(data = data2018, x = "Dystopia Residual", y = "Happiness Score")
sb.scatterplot(data = data2019, x = "Dystopia Residual", y = "Happiness Score")
sb.scatterplot(data = data2020, x = "Dystopia Residual", y = "Happiness Score")
sb.scatterplot(data = data2021, x = "Dystopia Residual", y = "Happiness Score")
sb.scatterplot(data = data2022, x = "Dystopia Residual", y = "Happiness Score")
