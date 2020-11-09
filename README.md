# pop_rollup_coding_challenge
This project is completed as a part of the Insight Data Engineering Coding Challenge for the Jan 2021 Cohort.

The problem is solved using Python 3.7

a. No external packages is used.

b. Regular expression is used to convert a line in the input CSV file to an entry in a data dictionary

c. While creating an entry for a unique CBSA code (if there are no CBSA code and CBSA title, then the entry it omitted from the calculations), 
the TRACTS are added into a Set. The Population in the year 2000 and Population in the year 2010 respectively are cumulatively added, for each of the TRACTS as they are encountered.

d. While writing to the report, for each unique CBSA, the following format is followed

1. CBSA Code
  
2. CBSA Title
  
3. Length of set of TRACTS in the CSBA
  
4. Population in the year 2000 in a CBSA
  
5. Population in the year 2010 in a CBSA
  
6. Percentage change in population for the CBSA from 2000 to 2010 rounded to 2 decimal places
