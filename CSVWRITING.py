import pycountry
import csv
import sys


class CSVReportProcessing:
    # Constructor a  CSVReportProcessing class
    # Field contains row's need to make a raport and will be save to the output csv file.
    def __init__(self):
        self.list = []

    # This method round number of clicks in each field list element's.
    def round_number_of_clicks(self):
        for i in self.list:
            i[3] = int(round((i[3]), 0))

    # This method sort a field list to the given way.
    def list_sort(self):
        self.list.sort()

    # This method write field list element's to the output file,
    # (taken the file name from sys.argv list in command-line arguments way, sys.argv[2] for output file name),
    #  each element to the separate line in output file.
    # You can change this method to ask user about output file name after running script.
    def write_list_to_the_output_csv_file(self, file):
        # The typical way to write a csv file,taken from python manual.
            with open(file, 'w', newline='\n', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for i in self.list:
                    writer.writerow('{0},{1},{2},{3}'.format(i[0], i[1], i[2], i[3]))

    # This method read a csv file,
    # (taken the file name from sys.argv list in command-line arguments way, sys.argv[1] for input file name),
    # and put changed data to the field list.
    # You can change this method to ask user about input file name after running script.
    def read_csv_file(self, file):
        try:
            with open(file, encoding='utf-8', newline='') as csvfile:
                # Csv reader return each row from file as list of strings.
                csv_lines_keeper = csv.reader(csvfile, delimiter=' ', quotechar=',')
                for row in csv_lines_keeper:
                    if len(row) == 0:
                        continue
                    try:
                        # I split here row to the string array using ',' separator .
                        # row_after_splitting[0] is a date.
                        # row_after_splitting[1] is name of subdivision.
                        # row_after_splitting[2] is a number of impressions.
                        # row_after_splitting[3] is a CTR percentage.
                        row_after_splitting = row.__getitem__(0).split(',')
                        if len(row_after_splitting) < 4:
                            raise sys.stderr.write(
                                'Row \'{0}\' don\'t have all elements!!\n'.format(row.__getitem__(0)))
                            continue
                        if len(row_after_splitting) > 4:
                            raise sys.stderr.write(
                                'Row \'{0}\' have to many elements!!\n'.format(row.__getitem__(0)))
                            continue
                        date = row_after_splitting[0].split('/')
                        # Here I change date format.
                        output_date_format = date[2] + '-' + date[0] + '-' + date[1]

                        # Here i declare variable need in next part of method.
                        # alpha_3 variable keep three letter country code
                        alpha_3 = None
                        # was_not_in_list is a Boolean variable if stay True after checked method,
                        #  add new element to the list
                        was_not_in_list = True
                        # was_not_in_subdivisions_list is a Boolean variable,
                        #  if stay True after checked variable alpha_3="XXX"
                        was_not_in_subdivisions_list = True
                        subdivisions = list(pycountry.subdivisions)
                        # In this place method checked that this subdivision exist in subdivisions list.
                        # If not alpha_3="XXX"
                        for i in subdivisions:
                            if i.name == row_after_splitting[1]:
                                alpha_3 = i.country.alpha_3
                                was_not_in_subdivisions_list = False
                        if was_not_in_subdivisions_list:
                            alpha_3 = "XXX"
                        # number_of_impressions variable keep value read from csv input file.
                        number_of_impressions = int(row_after_splitting[2])
                        # number_of_clicks variable
                        number_of_clicks = (float(number_of_impressions) * float(row_after_splitting[3].split('%')[0])) / 100
                        # Method checked that it is the same country in alpha_3 variable and in object field list,
                        # and that in object field list the same date like in date variable.
                        for i in self.list:
                            date1 = i[0].split('-')
                            # If all 'and conditions' are true, method overload,
                            #  third and fourth element in 'i' element of object field list.
                            if (i[1] == alpha_3) and (date1[0] == date[2]) and (date1[1] == date[0]) and (date1[2] == date[1]):
                                i[2] = i[2] + number_of_impressions
                                i[3] = i[3] + number_of_clicks
                                was_not_in_list = False
                            # If the last if conditions was not true, method add new element to the object field list.
                        if was_not_in_list:
                            self.list.append([output_date_format, alpha_3, number_of_impressions, number_of_clicks])

                    except IndexError:
                        sys.stderr.write("Bad formating date in row '{0}' in csv file for {1}!!\n"
                                         .format(row.__getitem__(0), row_after_splitting[0]))
                    except ValueError:
                        sys.stderr.write("Bad number value in row '{0}' in csv file for '{1}' or for '{2}'!!\n"
                                         .format(row.__getitem__(0), row_after_splitting[2], row_after_splitting[3]))
                    except:
                        sys.stderr.write("")

        except FileNotFoundError:
            sys.stderr.write("File not found!!! Report didn't make. Please check input file name,and run script again.")


report = CSVReportProcessing()
report.read_csv_file(sys.argv[1])
report.round_number_of_clicks()
report.list_sort()
report.write_list_to_the_output_csv_file(sys.argv[2])


