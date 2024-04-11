# Introduction to elementary analysis using Python 3

This repository represents all basic tasks as an introduction to analysis using **Python3.7 (Reviewed on 3.11)**.

## Projects

Projects in this repository cover the following topics: 
- using iterative basic types: list, tuple, set, dictionary, string
- basics of datetime module to work with date and time data
- read/write text data and XML
- find specified files in directory
- basics of numpy arrays
- pandas module for effective analysis
- matplotlib module for plotting data


## [Text Analysis](https://github.com/LSIND/intro-python3-analysis/tree/master/TextAnalysis)
> *Using built-in capabilities for string data processing*

Read .txt file, delete all punctuations, break text into independent words and write them to a new text file. Print word(s) with maximum length.  
*File*: [CrimeAndPunishment.txt](https://github.com/LSIND/intro-python3-analysis/blob/master/TextAnalysis/CrimeAndPunishment.txt). Chapter 6 of Dostoevsky's "Crime and Punishment" (text in English and Russian).

Script:
 - reads contents from .txt file (incl. unicode) 
 - deletes all punctuations from the text
 - breaks text into independent words. In case of complex word containing hyphen it should be divided into two different words (f.e., *ninety-nine = ninety nine*).
 - prints word(s) with maximum length
 - writes clean text to a new .txt file (one word per row).

## [Analysis of 1-dimensional data](https://github.com/LSIND/intro-python3-analysis/tree/master/TemperaturesAnalysis)
> *Using built-in capabilities for elementary analysis*

Read .txt file, which contains a list of decimal numbers (temperatures), find and print maximum, minimum and average temperatures, print number of elements and unique elements, print number of occurances for every value in the form of: *temperature : occurrences*. Ask user to input an interval and print temperatures and occurences in this interval.  
*File*: [1tempdata.txt](https://github.com/LSIND/intro-python3-analysis/blob/master/TemperaturesAnalysis/1tempdata.txt). One column of temperature data (the monthly high temperatures at Heathrow Airport 1948 - 2016).

Script:
 - reads all text from .txt file which contains list of tempreratures
 - prints maximum, minimum and average temperatures
 - prints number of values
 - prints number of unique values
 - prints number of occurrences for every value in the form of: *temperature : occurrences* sorted by occurrences in ascending order
 - asks a user to input the value interval of temperatures *[a; b]* and prints temperatures and their occurrences sorted by temperature from *a* to *b* in ascending order

## [Analysis of multidimensional data](https://github.com/LSIND/intro-python3-analysis/tree/master/TrainDepAnalysis)
> *Using built-in list and comprehensions*  
> *Using datetime module*  
> *Using Counter class from collections module*

Read text file, which contains data with train departures (train no, datetime of scheduled department, datetime of actual department), find and print number of not operated trains, departures on time, late departures and next day departures.  
*File*: [depsalem.txt](https://github.com/LSIND/intro-python3-analysis/blob/master/TrainDepAnalysis/depsalem.txt) with a set of [train departures](https://juckins.net/amtrak_status/archive/html/history.php) from Salem in period 09/01/2018 - 09/01/2019.

| Train # | Sch Dp                    | Act Dp |
|---------|---------------------------|--------|
| 505     | 09/01/2019 7:11   PM (Su) | 7:39PM |
| 508     | 09/01/2019   5:41 PM (Su) | 5:47PM |
| 505     | 08/10/2019 7:11   PM (Sa) |        |
| ...     | ...                       | ...    |

Script:
- reads .txt file with data of scheduled and actual departures of trains with the help of module *datetime*
- counts the number of not operated trains (column *Act Dp* is empty) and prints the number of not operated trains by day of the week using class Counter module *collections*;
- counts the number of departed trains, on time departures, late departures and next day departures.

## [Read XML-data](https://github.com/LSIND/intro-python3-analysis/tree/master/PlotCurrencyRates "PlotCurrencyRates")
> *Using xml module to parse XML-data*  
> *Using matplotlib to plot data*

Read XML-data from [Central Bank of Russia](http://www.cbr.ru/development/SXML/) with currency information depending on period with ratio to Russian ruble. Parse the result. Plot the currency rates.

Script **readcbr.py**:
 - reads data from [Central Bank of Russia](http://www.cbr.ru/development/SXML/) containing currency information in XML-format:
    * [XML with currency names and codes (ids)](http://www.cbr.ru/scripts/XML_val.asp?d=0). Retrieve names and unique codes, f.e. Euro = R01239;
    * [XML with currency rates](http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=05/09/2019&date_req2=30/09/2019&VAL_NM_RQ=R01239). Depends on unique currency code and two dates. Element < Value > contains ratio to Russian ruble at a specific date, f.e. 1 Euro = 73,0638 Rub at 05/09/2019 (dd/mm/YY);
    * uses modules *urllib.request* and *xml.etree.ElementTree* to retrieve and parse XML data:
  
```python
from urllib.request import urlopen
from xml.etree.ElementTree import parse
```
    
Script **main. py**:
- provides initial variables: currency name and two dates (period). You can change it or ask user for input.
  
```python
cur = "Turkish Lira"    
startdate = "03.05.2023"    
enddate = "26.05.2023"
```
- plots a graph of currency rates Currency/Russian ruble using *matplotlib* (if matplotlib is installed).
```python
try:
    import matplotlib.pyplot as plt
except:
    print('Matplotlib module not found. No plot output')
```

![currency rates](https://www.dropbox.com/s/8y5bg7mm28v98s7/plot_currency.png?raw=1)


## [Count files and subfolders (opt: specify file extension)](https://github.com/LSIND/intro-python3-analysis/tree/master/CountFilesAndFolders)
> *Using os and sys modules*   
> *Using command line arguments*

Provide the root directory and count files/subfolders inside it recursively. Example for `intro-python3-analysis-master`:
```Console
py -3 main.py C:\Users\Admin\Downloads\intro-python3-analysis-master

------> intro-python3-analysis-master :  7 folders,  2 files
--------> CountFilesAndFolders :         0 folders,  1 files
--------> EmployeesCounts :      0 folders,  2 files
--------> NPArrayVSList :        0 folders,  3 files
--------> PlotCurrencyRates :    0 folders,  2 files
--------> TemperaturesAnalysis :         0 folders,  2 files
--------> TextAnalysis :         0 folders,  3 files
--------> TrainDepAnalysis :     0 folders,  2 files
```

Optionally you can provide file extension to search for files with specified extension (recursively):

```Console
py -3 main.py C:\Users\Admin\Downloads\intro-python3-analysis-master .txt

------> intro-python3-analysis\TemperaturesAnalysis -> 1 .txt files
------> intro-python3-analysis\TextAnalysis -> 2 .txt files
------> intro-python3-analysis\TrainDepAnalysis -> 1 .txt files
```

## [List vs. Array vs. Numpy Array](https://github.com/LSIND/intro-python3-analysis/tree/master/NPArrayVSList)
> *Using array module*   
> *Using numpy module*  
> *Create simple decorator function to count time of execution*

Compare working time of built-in lists, arrays from module arrays and numpy arrays.  
*Three arrays contain int data. Please note that the size of objects (bytes) may vary in different versions of the interpreter. The following describes how to work with Python 3.11. Also don't forget that new int object itself consumes 28 bytes.*
  
Python built-in list without any elements (`list1 = []`) consumes 56 bytes. For every new element, it needs another 8 bytes for the reference to the new object. The size of a list `list1 = [5, 10, 15]` can be calculated with:

`56 + 8 * len(list1) = 88 bytes`

Array from module array without any elements (`array1 = array.array('X')` where 'T' is a [type of array](https://docs.python.org/3/library/array.html)) consumes 80 bytes. For every new element, it needs another X bytes for the reference to the new object. The size of an array with signed int values (one element X = 4 bytes) `array1 = array.array('i', [5, 10, 15])` can be calculated with:

`80 + 4 * len(array1) = 92 bytes`

NumPy array without any elements (`n1 = np.array([])`) consumes 112 bytes. For every new element, it also needs another 4 bytes for the reference to the new object. The size of a numpy array `n1 = np.array([5, 10, 15])` with int64 elements can be calculated with:

`112 + 4 * len(n1) = 124 bytes`

Script **merge.py**:
- Creates identical built-in lists L1 and L2, arrays A1 and A2 and numpy arrays N1 and N2 in a range of 100 000 000
- Merge two lists, two arrays and two numpy arrays

Script **zip.py**:
- Creates two identical built-in lists L1 and L2 and numpy arrays N1 and N2
- Zip two lists and two numpy arrays

Script **deco_time.py**:
- Decorator which counts execution time of each function

| Type        | Size (1 Obj), kB | Create 2 Objects, s | Merge 2 Objects, s | Zip 2 Objects, s |
|-------------|----------|----------------------|---------------------|-------------------|
| List        | 781250.05 | 9.66863            | 44.79549           | 156.99227        |
| Array       | 400563.94 | 15.70866            | 0.294982           |                   |
| Numpy Array | 390625.11 |  0.356011            | 0.343011           | 0.5320076        |

Pay attention to the size (kB) of the list.

## [Analyse CSV using Pandas](https://github.com/LSIND/intro-python3-analysis/tree/master/EmployeesCounts)
> *Using pandas module*

Create a dataframe from .csv file containing information about Employee and his hire datetime. Plot a graph with quantity of hired people by days of specified month.  
*File*: [empl.csv](https://github.com/LSIND/intro-python3-analysis/blob/master/EmployeesCounts/empl.csv) with a set of employees names and hire date and time.
    
| ID  | LastName | FirstName | HireDate  | HireTime |
|-----|----------|-----------|-----------|----------|
| 1   | Newell   | Pamella   | 9/9/2018  | 14:57:00 |
| 2   | Green    | Edna      | 8/28/2018 | 7:27:00  |
| ... | ...      |  ...      | ...       | ...      |

Script:
 - reads all data from .csv file containing employees names and hire dates/time using *pandas* module into dataframe
 - converts column 'HireDate' to date format *%Y-%m-%d*
 - creates series of column 'HireDate' and applies a condition to it within a period
 - prints number of occurrences in the series (hired people per date)
 - plots a bar graph of occurrences, f.e.:
 
![employees counts](https://www.dropbox.com/s/zplryx10b7o7iqr/plotemplcount.PNG?raw=1)