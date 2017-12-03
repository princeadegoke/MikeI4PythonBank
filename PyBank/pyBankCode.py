
import os

import csv



budget_files=['1','2']


filename=os.path.join("Output","output.txt")


with open(filename, 'w') as fileobject:


	for filenumber in budget_files:



		no_of_months=0

		total_revenue=0

		previous_change=0

		greatest_Inc_revenue=0

		greatest_Dec_revenue=0

		Average_revenue_change=0



		months=[]

		change_revenue=[]



		csvpath=os.path.join('Resources', 'budget_data_'+filenumber+'.csv')



		with open(csvpath) as csvfile:

			csvreader=csv.reader(csvfile,delimiter=',')

			

			next(csvreader,None)



			for row in csvreader:

				
				date=row[0]



				months.append(date)



				total_revenue=total_revenue+int(row[1])



				
				index=months.index(date)

				
				revenue_change=int(row[1])-previous_change

				change_revenue.insert(index,revenue_change)

				

				

				previous_change=int(row[1])



		
				change_revenue[0]=0


				no_of_months=len(months)





		print("\nFinancial Analysis for Budget File "+ str(filenumber))

		print("---------------------------------------------------------------------")

		print("Number of months: " + str(len(months)))

		print("Total Revenue: $" + str(total_revenue))



		Average_revenue_change=round(sum(change_revenue)/(len(change_revenue)-1),3)

		print("Average Revenue Change: $"+ str(Average_revenue_change))



		greatest_Inc_revenue=max(change_revenue)

		month_Greatest_Inc_revenue=months[change_revenue.index(greatest_Inc_revenue)]

		print("Greatest Increase in Revenue: " + month_Greatest_Inc_revenue + "($" + str(greatest_Inc_revenue)+")")


		greatest_Dec_revenue=min(change_revenue)

		month_Greatest_Dec_revenue=months[change_revenue.index(greatest_Dec_revenue)]

		print("Greatest Derease in Revenue: " + month_Greatest_Dec_revenue + "($" + str(greatest_Dec_revenue)+")")




		fileobject.write("\nFinancial Analysis for Budget File "+ str(filenumber) + "\n")

		fileobject.write("---------------------------------------------------------------------" + "\n")

		fileobject.write("Number of months: " + str(len(months)) + "\n")

		fileobject.write("Total Revenue: $" + str(total_revenue) + "\n")

		fileobject.write("Average Revenue Change: $"+ str(Average_revenue_change) + "\n")

		fileobject.write("Greatest Increase in Revenue: " + month_Greatest_Inc_revenue + "($" + str(greatest_Inc_revenue)+")" + "\n")

		fileobject.write("Greatest Derease in Revenue: " + month_Greatest_Dec_revenue + "($" + str(greatest_Dec_revenue)+")" + "\n")



 #End of project