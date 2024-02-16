import csv  #module is used for read write and investiagete csv 
"""
Read and print rows from csv file

for argument it takes the name of the csv file.
"""

def read_csv(filename): #giving name of the func and argument name
    try:
        with open(filename, 'r', newline='') as file: #with is an statement it access resources likes files
            """open is and function that pen files, and it takes atleast one argument 'filename' which will be
            the csv file i want to open . the 'r' tells us that csv file will me open and will be in read mode.
            the newline paramater will understand when we go to a newline in the csv file.
            """
            csv_reader = csv.reader() # assigning the rading function of csv to csv_reader variable.
            next(csv_reader) #skips the first line
            for row in csv_reader:  #this for loop prints out the rows one by one
                print(', '.join(row)) #join each rows words with a comma in between
    except:
        print("Something wrong with the code")  #if code wrong this will print


if __name__ == "__main__": 
    '''if I running code here, the if statment will run or else the if statement
    won't run as I will be suing it as an helper from another program.
    '''
    csv_filename = "names.csv" # saving the name of the csv file in a variable
    read_csv(csv_filename) #read_csv takes the argument and reads the CSV file