#Создайте сценарий, который использует список имен файлов CSV в качестве источника для копирования файлов в плоский файл. 
#Текущая дата и время должны быть добавлены к имени файла в качестве префикса перед копированием. 
#Каждая операция копирования должна быть записана в файл журнала на локальном компьютере, после чего локальный файл 
#будет удален. 
#Исключения для файлов, которые не были найдены, также должны быть записаны в журнал.

import datetime
import csv
import logging
import os

# Список названий файлов
files = ['file_1.csv', 'file_2.csv', 'file_3.csv']
# текущая дата
d = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
logfile = 'logfile_' + d + '.log'
logfile_errors = 'logfile_errors' + d + '.log'
# строка название нового файла
MERGED_FILE = d + '_' + 'merged_file.csv'
for f in files:
    try:
        with open(f, 'r') as fil:
            a = fil.read()
            with open(MERGED_FILE, "a+") as newf:
                newf.write(a)
                #logging.basicConfig(filename = logfile, level=logging.DEBUG)
                #logging.debug('Запись в общий файл: \n' + a)
    except IOError as err:
        logging.basicConfig(filename=logfile_errors, level=logging.DEBUG)
        logging.debug(err)