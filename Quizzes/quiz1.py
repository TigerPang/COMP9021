# Uses data available at http://data.worldbank.org/indicator
# on Forest area (sq. km) and Agricultural land area (sq. km).
# Prompts the user for two distinct years between 1990 and 2004
# as well as for a strictly positive integer N,
# and outputs the top N countries where:
# - agricultural land area has increased from oldest input year to most recent input year;
# - forest area has increased from oldest input year to most recent input year;
# - the ratio of increase in agricultural land area to increase in forest area determines
#   output order.
# Countries are output from those whose ratio is largest to those whose ratio is smallest.
# In the unlikely case where many countries share the same ratio, countries are output in
# lexicographic order.
# In case fewer than N countries are found, only that number of countries is output.


# Written by *** and Jack for COMP9021


import sys
import os
import csv
from collections import defaultdict


agricultural_land_filename = 'API_AG.LND.AGRI.K2_DS2_en_csv_v2.csv'
if not os.path.exists(agricultural_land_filename):
    print(f'No file named {agricultural_land_filename} in working directory, giving up...')
    sys.exit()
forest_filename = 'API_AG.LND.FRST.K2_DS2_en_csv_v2.csv'
if not os.path.exists(forest_filename):
    print(f'No file named {forest_filename} in working directory, giving up...')
    sys.exit()
try:
    years = {int(year) for year in
                           input('Input two distinct years in the range 1990 -- 2014: ').split('--')
            }
    if len(years) != 2 or any(year < 1990 or year > 2014 for year in years):
        raise ValueError
except ValueError:
    print('Not a valid range of years, giving up...')
    sys.exit()
try:
    top_n = int(input('Input a strictly positive integer: '))
    if top_n < 0:
        raise ValueError
except ValueError:
    print('Not a valid number, giving up...')
    sys.exit()


countries = []
year_1, year_2 = None, None

###### Insert your code here

years = list(years)
year_1 = years[0]
year_2 = years[1]
if year_1 > year_2:
    year_1, year_2 = year_2, year_1

ratio = {}
py1 = year_1 - 1990 + 34
py2 = year_2 - 1990 + 34


with open(agricultural_land_filename,encoding = "utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        if len(line) == 0:
            continue
        
        if line[0] == '﻿"Data Source"' or line[0] == 'Last Updated Date' or line[0] == 'Country Name':
            continue
        country = line[0]

        a = 1
        try:
            difference = float(line[py2]) - float(line[py1])
        except ValueError:
            a = 0
        if a == 1 and difference > 0:
            ratio[country] = difference

with open(forest_filename,encoding = "utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        if len(line) == 0:
            continue
        
        if line[0] == '﻿"Data Source"' or line[0] == 'Last Updated Date' or line[0] == 'Country Name':
            continue

        country = line[0]
        if country not in ratio.keys():
            continue
        a = 1
        try:
            difference = float(line[py2]) - float(line[py1])
        except ValueError:
            a = 0
        if a == 1 and difference > 0:
            ratio[country] =ratio[country]/difference
        else:
            del ratio[ country ]

topcpuntries = sorted(ratio, key=ratio.get, reverse=True)[:top_n]

countries = [(country + ' ' + "(" + str("%.2f" %ratio[country]) + ')')  for country in topcpuntries]







print(f'Here are the top {top_n} countries or categories where, between {year_1} and {year_2},\n'
      '  agricultural land and forest land areas have both strictly increased,\n'
      '  listed from the countries where the ratio of agricultural land area increase\n'
      '  to forest area increase is largest, to those where that ratio is smallest:')
print('\n'.join(country for country in countries))
    
