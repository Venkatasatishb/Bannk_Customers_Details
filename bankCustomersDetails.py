# Bank Customers Details

customersRecords = []
fileName = "bankCustomersDetails.dat"
with open(fileName, 'r') as fpDetails:
	customersRecords = eval(fpDetails.read())

def saveCustomerRecord():
	customerRecord = []
	customerRecord.append(input("Enter Customer Account Number: "))
	customerRecord.append(input("Enter Customer Name: "))
	customerRecord.append(input("Enter Customer Balance: "))
	customerRecord.append('A')
	customersRecords.append(customerRecord)
	saveCustomersRecords()
def showAllActiveCustomersRecords():
	for customerRecord in customersRecords:
		if customerRecord[3] == 'A':
			print("\nAccount Number: " + customerRecord[0] + "\nCustomer Name: " + customerRecord[1] + "\nCurrent Balance: " + customerRecord[2])
		
def showAllClosedCustomersRecords():
	for customerRecord in customersRecords:
		if customerRecord[3] == 'C':
			print("\nAccount Number: " + customerRecord[0] + "\nCustomer Name: " + customerRecord[1] + "\nCurrent Balance: " + customerRecord[2])

def showAllCustomerRecords():
	for customerRecord in customersRecords:
		print("\nAccount Number: " + customerRecord[0] + "\nCustomer Name: " + customerRecord[1] + "\nCurrent Balance: " + customerRecord[2])
		if customerRecord[3] == 'A':
			print("Account Status: Active")
		elif customerRecord[3] == 'C':
			print("Account Status: Closed")

def searchRecord():
	accountNumberToBeSearched = input("Enter Account Number To Search: ")
	for customerRecord in customersRecords:
		if accountNumberToBeSearched == customerRecord[0]:
			print("\nAccount Number: " + customerRecord[0] + "\nCustomer Name: " + customerRecord[1] + "\nCurrent Balance: " + customerRecord[2])
			if customerRecord[3] == 'A':
				print("Account Status: Active")
			elif customerRecord[3] == 'C':
				print("Account Status: Closed")
			break

def updateRecord():
	accountNumberToBeUpdated = input("Enter Account Number To Update: ")
	for customerRecord in customersRecords:
		if accountNumberToBeUpdated == customerRecord[0]:
			print("\nAccount Number: " + customerRecord[0] + "\nCustomer Name: " + customerRecord[1] + "\nCurrent Balance: " + customerRecord[2])
			if customerRecord[3] == 'A':
				print("Account Status: Active")
			elif customerRecord[3] == 'C':
				print("Account Status: Closed")
			option = int(input("\n What Do You Want To Update: \n1. Customer Name\n2. Current Balance"))
			if option == 1:
				customerRecord[1] = input("Enter New Name: ")
			elif option == 2:
				customerRecord[2] = input("Enter New Balance: ")
			else:
				print("\nEnter Correct Option.\n")
			saveCustomersRecords()
			break

def closeRecord():
	accountNumberToBeClosed = input("Enter Account Number To close: ")
	for customerRecord in customersRecords:
		if accountNumberToBeClosed == customerRecord[0]:
			customerRecord[3] = 'C'
			saveCustomersRecords()
			break

def exit():
	quit()

def saveCustomersRecords():
	with open(fileName, 'w') as fpDetails:
		fpDetails.write(str(customersRecords))
	

while (1):
	functions = [saveCustomerRecord, showAllCustomerRecords,showAllActiveCustomersRecords, showAllClosedCustomersRecords, searchRecord, updateRecord, closeRecord, exit]
	functions[int(input("\n1. Save Customer Record\n2. Show All Customer Records\n3. Show All Active Customers Records\n4. Show All Closed Customers Records\n5. Search Record\n6. Update Record\n7. Close Record\n8. Exit\n----------------------\nEnter Your Choice: ")) - 1]()