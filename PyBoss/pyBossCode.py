
import os

import csv

import sys




us_filepath=os.path.join("Library")

sys.path.append(us_filepath)

import us_state_abbrev



import datetime



employee_data_files=['1','2']



outputfilename=os.path.join("Output","output.csv")



with open(outputfilename, 'w', newline='') as csvfile:

	csvwriter = csv.writer(csvfile, delimiter=',')

	

	csvwriter.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])



	for filenumber in employee_data_files:

		


		csvpath=os.path.join('Resources', 'employee_data'+filenumber+'.csv')

		

		with open(csvpath) as csvfile:

			csvreader=csv.reader(csvfile,delimiter=',')

			

			next(csvreader,None)

			

			for row in csvreader:

				


				FirstName,LastName=row[1].split(" ")

				

				DOB=datetime.datetime.strptime(row[2], "%Y-%m-%d").strftime("%d/%m/%Y")

				

				last4SSN=row[3][-4:]

				newSSN="***-**-"+str(last4SSN)

				



				csvwriter.writerow([row[0],FirstName,LastName,DOB,newSSN,us_state_abbrev.us_state_abbrev[row[4]]])



print("\nFormatting data completed successfully!!\n")
