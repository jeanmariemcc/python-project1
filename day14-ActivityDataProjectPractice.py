# Joy of coding Day 14 Activity: Data Project Practice
# Author JeanMarie McCormack    Composition date: Sept 28, 2022  Last update: Sept 28, 2022


from statistics import mean
from statistics import stdev
from statistics import median


def stats(the_list):
    # given a list of numbers, return a list containing the mean, median and std deviation
    # (in that order) rounded to two decimal places
    answer_list = [round(mean(the_list), 2), round(median(the_list), 2), round(stdev(the_list), 2)]
    return answer_list


def semester_sort(infile):
    # create a function that compares the statistics of the "Fall 2016" and "Spring 2016" semesters
    # input: a csv file containing student name, semester, grade
    # output: print the mean, median, and standard deviation of each semester
    semester1 = []
    semester2 = []
    data_file = open(infile, "r")
    for line in data_file:
        linesplit = line.split(",")
        if linesplit[1] == "Fall 2016":
            semester1.append(eval(linesplit[2].replace('\n', "")))
        else:
            semester2.append(eval(linesplit[2].replace('\n', "")))
    # this print statement avoids unnecessary storage, but calls  the function stats() 3 times
    print(f"Fall 2016   -  Mean: {stats(semester1)[0]}, Median: {stats(semester1)[1]}, STD: {stats(semester1)[2]}")
    # alternative method calls stats() once, but involves storage - depends upon application which is most important
    stats2 = stats(semester2)
    print(f"Spring 2016 -  Mean: {stats2[0]}, Median: {stats2[1]}, STD: {stats2[2]}")


def main():
    semester_sort("day14ActivitySample_grades.csv")


main()
