# Python-Intern-Task---CSV-Report-Processing
Python Intern Task - CSV Report Processing
To run this script  

a)using PyCharm and other python IDE, add input csv file eg. 'input.csv' and add output csv file eg. 'output.csv' to the field Parameters in file Running configurations, click apply and ok.Now You can run the script. The input file should be in the same folder with  python scripts. If dont, You must put full path to the file. If the output file don't exist, script create a new csv file, with name You put as parameter.

b) using windows command line, go to folder with script, press shift key and use right mouse button click open command window here. write python or python3 'name of file' 'name of csv input file' 'name of csv output file' click enter. The input file should be in the same folder with  python scripts. If dont, You must put full path to the file. If the output file don't exist, script create a new csv file, with name You put as parameter.
In this script i made a class CSVReportProcessing with one field 'list'. It is a list that keep all good row read from input csv file, prepared to be saved. 

Class CSVReportProcessing have 4 method to help with this exercise. 

    #This method round number of clicks in each field list element's.
    
    round_number_of_clicks(self)
    
    # This method sort a field list to the given way.
    
    list_sort(self)

    # This method write field list element's to the output file,
    # (taken the file name from sys.argv list in command-line arguments way, sys.argv[2] for output file name),
    #  each element to the separate line in output file.
    
    write_list_to_the_output_csv_file(self, file):

    # This method read a csv file,
    # (taken the file name from sys.argv list in command-line arguments way, sys.argv[1] for input file name),
    # and put changed data to the field list
    
    read_csv_file(self, file):
