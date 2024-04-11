# Основы анализа данных с использованием Python 3

Репозиторий содержит основные задачи элементарного анализа данных в Python версии **3.7** и выше (**Reviewed on 3.11**).

## Проекты

Проекты данного репозитория охватывают следующие темы:
- встроенные итерируемые типы данных: список (list), кортеж (tuple), словарь (dict), множество (set), строка (str)
- основы модуля datetime для работы с типом дата/время
- чтение / запись текстовых данных и XML-данных
- поиск файлов в каталогах
- основы массивов numpy
- модуль pandas для более оптимального анализа данных
- модуль matplotlib для построения графиков


## [Анализ текста](https://github.com/LSIND/intro-python3-analysis/tree/master/TextAnalysis)
> *Использование встроенных возможностей Python для обработки текста*  
> *Использование строкового типа str*

Прочитайте текстовый файл, удалите все знаки препинания, разбейте текст на отдельные слова и запишите их в новый текстовый файл. Выведите слово(а) максимальной длины.  
*Файл*: [CrimeAndPunishment.txt](https://github.com/LSIND/intro-python3-anaлиз/blob/master/TextAnalysis/CrimeAndPunishment.txt). Ф.М. Достоевский, «Преступление и наказание», Глава 6 (текст на английском и русском языках).

Скрипт:
  - читает весь текст из файла .txt (включая юникод)
  - удаляет все знаки препинания из текста
  - разбивает текст на независимые слова. В случае сложного слова, содержащего дефис, его следует разделить на два разных слова (например, *черно-белый = черно белый*).
  - печатает слово (слова) с максимальной длиной
  - записывает очищенный текст в новый файл .txt (по одному слову на строку).

## [Анализ одномерного списка](https://github.com/LSIND/intro-python3-analysis/tree/master/TemperaturesAnalysis)
> *Использование встроенных возможностей Python для анализа большого одномерного списка*  
> *Использование типов list, set, dict*  

Прочитайте текстовый файл, который содержит список десятичных чисел (температур), выведите максимальные, минимальные и средние температуры, выведите общее количество значений температур, а также уникальных значений. Определите количество вхождений для каждого значения в виде: *температура: вхождения *. Попросите пользователя ввести интервал с клавиатуры и вывести ему температуры и количество их вхождений в этом интервале.  
*Файл*: [1tempdata.txt](https://github.com/LSIND/intro-python3-anaлиз/blob/master/TemperaturesAnasis/1tempdata.txt). Один столбец данных о температуре (ежемесячные высокие температуры в аэропорту Хитроу, 1948–2016 гг.).

Скрипт:
  - читает весь текст из .txt файла, содержащего одномерный список (месячные значения температур)
  - печатает максимальные, минимальные и средние значения температур
  - печатает общее количество значений
  - печатает количество уникальных значений
  - печатает количество вхождений для каждого значения в виде: *температура: кол-во вхождений*, отсортированные по количеству вхождений в порядке возрастания
  - запрашивает у пользователя интервал значений температур *[a; b]* и печатает температуры и их количество вхождений, отсортированные по значению температуры от *a* до *b* в порядке возрастания

## [Анализ многомерного списка](https://github.com/LSIND/intro-python3-analysis/tree/master/TrainDepAnalysis)
> *Использование типа list и генераторов*  
> *Использование модуля datetime*  
> *Использование класса Counter из модуля collections*  

Прочитайте текстовый файл, который содержит данные об отправлении поездов (номер поезда, дату и время запланированного отправления, дату и время фактического отправления). Выведите количество отмененных поездов, поездов, отправленных вовремя, отправлений с задержкой и отправлений на следующий день.  
*Файл*: [depsalem.txt](https://github.com/LSIND/intro-python3-anaанализ/blob/master/TrainDepAnalysis/depsalem.txt) содержит строки с [расписанием поездов](https://juckins.net/amtrak_status/archive/html/history.php) из Салема в период с 01.09.2018 по 01.09.2019.

Скрипт:
- читает файл .txt с данными о плановых и фактических отправлениях поездов в list  

| Train # | Sch Dp                    | Act Dp |
|---------|---------------------------|--------|
| 505     | 09/01/2019 7:11   PM (Su) | 7:39PM |
| 508     | 09/01/2019   5:41 PM (Su) | 5:47PM |
| 505     | 08/10/2019 7:11   PM (Sa) |        |
| ...     | ...                       | ...    |

- с помощью модуля *datetime* преобразует Sch Dp и Act Dp в формат дата/время  
    `import datetime`
- подсчитывает количество не отправленных поездов (столбец *Act Dp* пуст) и печатает количество не отправленных поездов по дням недели с использованием модуля *collections*;  
- подсчитывает общее количество отправленных поездов, поездов, отправленных по расписанию, поездов вышедших с задержкой и поездов, отправленных на следующий день.

## [Работа с XML-данными](https://github.com/LSIND/intro-python3-analysis/tree/master/PlotCurrencyRates)
> *Использование модуля xml для анализа XML-данных*  
> *Использование модуля matplotlib для построения данных*  

Получите XML-данные [Центрального банка России](http://www.cbr.ru/development/SXML/) с информацией о валюте в зависимости от периода в соотношении к российскому рублю. Распарсите результат. Постройте график курсов валют.

Скрипт (модуль **readcbr.py**):  
- читает данные с сайта [Центрального банка России](http://www.cbr.ru/development/SXML/), который содержит информацию о валюте в XML-формате:
    * [XML с названиями валют и кодами (идентификаторами)](http://www.cbr.ru/scripts/XML_val.asp?d=0). Код должен извлекать идентификатор из предоставленного имени, например Euro = R01239;
    * [XML с курсами валют](http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=05/09/2019&date_req2=30/09/2019&VAL_NM_RQ=R01239) в зависимости от идентификатора валюты и промежутка времени (двух дат). Элемент Value содержит отношение валюты к российскому рублю на определенную дату, например 1 евро = 73,0638 руб. на 05/09/2019 (дд/мм/гг);
- использует модули *urllib.request* и *xml.etree.ElementTree* для извлечения и анализа данных XML:
 ```python
 from urllib.request import urlopen 
 from xml.etree.ElementTree import parse
 ```
    
Скрипт (**main.py**):  
- предоставляет начальные переменные: название валюты и две даты (период). Их можно изменить или запросить у пользователя.  
```python
cur = "Turkish Lira"    
startdate = "03.05.2023"    
enddate = "26.05.2023"
```
- строит график курсов валют: Валюта / Российский рубль, используя *matplotlib* (если этот модуль установлен):  
```python
try:
    import matplotlib.pyplot as plt
except:
    print('Matplotlib module not found. No plot output')
```
![currency rates](https://www.dropbox.com/s/8y5bg7mm28v98s7/plot_currency.png?raw=1)

## [Подсчет количества файлов и вложенных каталогов (+ указание расширения файла)](https://github.com/LSIND/intro-python3-analysis/tree/master/CountFilesAndFolders)
> *Использование модулей os и sys*   
> *Использование аргументов командной строки*

На вход поступает корневая директория. Скрипт рекурсивно подсчитывает количество файлов и вложенных каталогов. Пример вывода для `intro-python3-analysis-master`:
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

Дополнительно можно передать расширение файла для поиска:
```Console
py -3 main.py C:\Users\Admin\Downloads\intro-python3-analysis-master .txt

------> intro-python3-analysis\TemperaturesAnalysis -> 1 .txt files
------> intro-python3-analysis\TextAnalysis -> 2 .txt files
------> intro-python3-analysis\TrainDepAnalysis -> 1 .txt files
```

## [List vs. Array vs. Numpy Array](https://github.com/LSIND/intro-python3-analysis/tree/master/NPArrayVSList)
> *Использование модуля array*  
> *Использование модуля numpy*
> *Создание простого декоратора для расчета времени выполнения*  

Сравнение скорости работы встроенного списка (list), array из модуля Array и массива NumPy.  
*Все три массива содержат целочисленные данные int. Учитывайте, что размер объектов (байты) может быть различным в разных версиях интерпретатора. Ниже описана работа с Python 3.11. Также учитывайте, что каждый новый объект int занимает 28 байт.* 

1. Встроенный пустой список (list) Python (`l1 = []`) занимает 56 б. Для каждого нового элемента требуется еще 8 байт - ссылка на новый объект. Размер списка `l1 = [5, 10, 15]` равен:  
`56 + 8 * len(l1) = 88 б`

2. Пустой массив из модуля array (`a1 = array.array('X')`), где 'T' - [тип массива](https://docs.python.org/3/library/array.html), занимает 80 б. Для каждого нового элемента требуется еще X байт - ссылка на новый объект. Размер массива с целым числом со знаком (один int элемент занимает X=4 б) `a1 = array.array('i', [5, 10, 15])` равен:    
`80 + 4 * len(a1) = 92 б`

3. Пустой массив NumPy (`n1 = np.array([])`) занимает 112 байт. Для каждого нового элемента ему также нужно 8 б для ссылки на новый объект. Размер массива numpy `n1 = np.array ([5, 10, 15])`, где элементы являются типом int64, равен:  
`112 + 8 * len(n1) = 124 б`  

Скрипт **merge.py**:
- создает три пары идентичных целочисленных встроенных списка L1 и L2, массивов A1 и A2 из модуля array, массивов NumPy N1 и N2 в промежутке от 1 до 100 000 000
- рассчитывает размер объекта каждого типа с помощью функции getsizeof() модуля sys
- "склеивает" два списка, два массива и два массива NumPy

Скрипт **zip.py**:
- создает две пары идентичных встроенных списка L1 и L2 и массивов NumPy N1 и N2  
- объединяет итерируемые объекты в группы

Скрипт **deco_time.py**:
- функция-декоратор без параметров, которая рассчитывает время выполнения любой функции и выводит ее имя и время выполнения (в секундах) на консоль  

| Type        | Size (1 Obj), kB | Create 2 Objects, s | Merge 2 Objects, s | Zip 2 Objects, s |
|-------------|----------|----------------------|---------------------|-------------------|
| List        | 781250.05 | 9.66863            | 44.79549           | 156.99227        |
| Array       | 400563.94 | 15.70866            | 0.294982           |                   |
| Numpy Array | 390625.11 |  0.356011            | 0.343011           | 0.5320076        |

Обратите внимание на размер (кБ) списка.


## [Анализ csv-файла с помощью pandas](https://github.com/LSIND/intro-python3-analysis/tree/master/EmployeesCounts)
> *Использование модуля pandas*

Создайте датафрейм из csv-файла, который содержит информацию о сотруднике и дате и времени его найма. Постройте график количества нанятых людей по дням указанного месяца.  
*Файл*: [empl.csv](https://github.com/LSIND/intro-python3-anaанализ/blob/master/EmployeesCounts/empl.csv). Имена сотрудников, дата и время приема на работу.
 
| ID  | LastName | FirstName | HireDate  | HireTime |
|-----|----------|-----------|-----------|----------|
| 1   | Newell   | Pamella   | 9/9/2018  | 14:57:00 |
| 2   | Green    | Edna      | 8/28/2018 | 7:27:00  |
| ... | ...      |  ...      | ...       | ...      |

Скрипт:
- считывает данные из CSV-файла, содержащего имена сотрудников и даты/время найма, используя модуль *pandas* в датафрейм
- преобразует столбец «HireDate» в формат даты *%Y-%m-%d*
- создает вектор столбца «HireDate» и применяет к нему условие - определенный период
- выводит количество вхождений в вектор (количество нанятых людей в определенную дату)
- строит гистограмму вхождений, например:
 
![employees counts](https://www.dropbox.com/s/zplryx10b7o7iqr/plotemplcount.PNG?raw=1)