#-------------------------------------------------------------------------
#                     read, write, parse csv files
#-------------------------------------------------------------------------

'''Python Tutorial: CSV Module - How to Read, Parse, and Write CSV Files'''

'''
                                Notes 
                                
csv = comma seperated files, allows us to put into a plaintext file some 
data, and to use a delimiter to seperate to fields.

both files need to be in the same folder for it to work?

were trying to see if we can leave the heading fields first, middle, last
out, and see how it may affect the program     

also trying to use a file without the .txt extension.

possible to use the split(string method ?!?!                 

review context managers again  

can i create a csv file from plain txt by naming it with .csv or .txt       
    YES!                          
    
find out if there is a way to use read a xlsx file type
'''



# csvtext did not work
# csvtext.txt did
# I also created a new csvextension.csv file, and it worked also
# would not run csvextensionexcel.xlsx file
'''
C:Users\darre\Documents\csvfolder\venv\Scripts\python.exe C:/Users/darre/Documents/csvfolder/csvextract.py
Traceback (most recent call last):
  File "C:/Users/darre/Documents/csvfolder/csvextract.py", line 36, in <module>
    for line in csv_reader:
  File "C:Users\darre\Documents\csvfolder\venv\lib\encodings\cp1252.py", line 23, in decode
    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 16: character maps to <undefined>

Process finished with exit code 1
'''
#
# import csv
#
# with open('csvextension.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#   next(csv_reader)  will skip the line of values
#     for line in csv_reader:
#         print(line[0], end='')
#       if you add, end='' they will all be on one line
#           ['darren', 'james', 'gibson']['melissa', 'anne', 'gibson']['tyler', 'james', 'gibson']['patrick', 'joel', 'gibson']
#       we can also look at specific index's [0]
#           darren
#           melissa
#           tyler
#           patrick
#       i wrote print(line[0], end='') here and it worked
#           darrenmelissatylerpatrick
'''
['darren', 'james', 'gibson']
['melissa', 'anne', 'gibson']
['tyler', 'james', 'gibson']
['patrick', 'joel', 'gibson']
['jason', 'michael', 'curley']
['erin', 'curley', 'mundt']
'''




import csv
# if you do not provide the import csv, the error is:
# C:\Users\darre\Documents\csvfolder\venv\Scripts\python.exe C:/Users/darre/Documents/csvfolder/csvextract.py
# Traceback (most recent call last):
#   File "C:/Users/darre/Documents/csvfolder/csvextract.py", line 79, in <module>
#     csv_reader = csv.reader(csv_file)
# NameError: name 'csv' is not defined
#
# Process finished with exit code 1
# with open('csvextension.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     with open('createcsv.csv', 'w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='-')
# #       we can add in delimiter='-' to seperate with -
#         for line in csv_reader:
#             csv_writer.writerow(line)
# This produced a new file called create.csv with the contents of
# the original csvextension.csv data, and placed it in the new file
# with - delimiters in stead of the commas.

# you can open csv files with either excel or notepad




''' Heres a little creation I made that asks you for the name you want 
    the file to be called.
'''



with open('csvextension.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    youname = input('Please enter the new file name: ')

    with open(youname, 'w') as new_file:
        csv_writer = csv.writer(new_file)
#       if we left out the delimeter the file is
#       we can use several delimiters here \t   ' '   '-'
        for line in csv_reader:
            csv_writer.writerow(line)
# this created a file, but with no extension.  because the file did not
# an extension declared, I open it with both notepad and excel










