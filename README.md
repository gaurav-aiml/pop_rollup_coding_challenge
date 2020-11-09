# pop_rollup_coding_challenge
This project is completed as a part of the Insight Data Engineering Coding Challenge for the Jan 2021 Cohort.

The problem is solved using Python 3.7

1. No external packages is used.

2. Regular expression is used to convert a line in the input CSV file to an entry in a data dictionary

3. While creating an entry for a unique CBSA code (if there are no CBSA code and CBSA title, then the entry it omitted from the calculations), 
the TRACTS are added into a Set. The Population in the year 2000 and Population in the 2010 for all the TRACTS in a CBSA are added.

4. While writing to the report, for each unique CBSA, the following format is followed
  a. CBSA Code
  b. CBSA Title
  c. Length of the TRACTS set
  d. Population in the year 2000 added up for all the TRACTS in a CBSA
  e. Population in the year 2010 added up for all the TRACTS in a CBSA
  f. Percentage change in population for the CBSA from 2000 to 2010 rounded to 2 decimal places

