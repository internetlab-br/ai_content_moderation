# -*- coding: utf-8 -*-
import csv
import random

def select_distribute():
    original_list = []

    with open('tweets_file.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            original_list.append(row[0])

    size = len(original_list)
    #the value of the sample size was calculated by hand using the finite population sampling formula
    sample_size = 100

    id_tweets_list = []
    researcher1_list = []
    researcher2_list = []
    researcher3_list = []
    researcher4_list = []
    researcher5_list = []

    for i in range(size):
        ids_list.append(i)

    #we decided to execute two shuffles
    random.shuffle(ids_list)
    random.shuffle(ids_list)

    count = 0
    for j in range(int(sample_size)):
        if count == 0:
            researcher1_list.append(ids_list[j])
        elif count == 1:
            researcher2_list.append(ids_list[j])
        elif count == 2:
            researcher3_list.append(ids_list[j])
        elif count == 3:
            researcher4_list.append(ids_list[j])
        elif count == 4:
            researcher5_list.append(ids_list[j])

            count = -1

        count = count + 1

    #write csv file for each researcher separately
    for index in researcher1_list:
        with open('researcher1.csv', mode='a') as r_file:
            employee_writer = csv.writer(r_file, delimiter=',')
            employee_writer.writerow([researcher1_list[index]])

    for index in researcher2_list:
        with open('researcher2.csv', mode='a') as r_file:
            employee_writer = csv.writer(r_file, delimiter=',')
            employee_writer.writerow([researcher2_list[index]])

    for index in researcher3_list:
        with open('researcher3.csv', mode='a') as r_file:
            employee_writer = csv.writer(r_file, delimiter=',')
            employee_writer.writerow([researcher3_list[index]])

    for index in researcher4_list:
        with open('researcher4.csv', mode='a') as r_file:
            employee_writer = csv.writer(r_file, delimiter=',')
            employee_writer.writerow([researcher4_list[index]])

    for index in researcher5_list:
        with open('researcher5.csv', mode='a') as r_file:
            employee_writer = csv.writer(r_file, delimiter=',')
            employee_writer.writerow([researcher5_list[index]])


select_distribute()
