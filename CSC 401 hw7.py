#Lukasz Grzybek
def  startUp(fname):
	lined = {}
	try:
		infile = open(fname, 'r')
		lines = infile.readlines()
		
		for line in lines:
			(pin,first,last,balance) = line.split(',')
			account = []
			account.append(first)
			account.append(last)
			balance = float(balance)
			account.append(balance)
			lined[pin] = account
		infile.close()
		return lined
	except IOError:
		print('{} not found'.format(fname))
		return None

def verifyPin(d):
	pin = input('Enter pin number: ')

	for key in d.keys():
		if pin == key:
			return key, d[key][0]
		if pin != key:
			for i in range(2):
				invalid_pin = input('Invalid pin, try again: ')
			msg = 'Please call customer support at 800-000-0000'
			return (None, msg)
	

def displayMenu(name):
	print(name)
	print('1. Deposit')
	print('2. Withdrawal')
	print('3. Balance')
	print('4. Quit')
	menu_choice = verifyMenuChoice()
	return menu_choice

def verifyMenuChoice():
	while True:
		try:
			choice = input('Enter a menu number: ')
			choice = int(choice)
			choice_list = [1,2,3,4]
			if choice in choice_list:
				return choice
			else:
				print('Enter 1 or 2 or 3 or 4, try again')
				
		except ValueError:
			print('{} invalid choice, non-numeric characters not allowed, try again'.format(choice))
			

def verifyAmount():
	while True:
		amount = input('Enter amount to be deposited or withdrawn: ')
		if amount[0] == '-':
			print('Negative amount. Try again')
			amount = input('Enter amount to be deposited or withdrawn: ')
		else:
			try:
				amount = float(amount)
				return amount
			except:
				print('Invalid amount. Use digits only')


def deposit(pin,d):
	for key in d.keys():
		if pin == key:
			d[key][2] += verifyAmount()
			#print(d)
		else:
			return None

def withdraw(pin, d):
	while True:
		for key in d.keys():
			if pin == key:
				if d[key][2] < verifyAmount():
					print('Insufficient funds to complete the transaction')

				else:
					d[key][2] -= verifyAmount()
					
					return None
			else:
				return None

def balance(pin, d):
	for key in d.keys():
		if pin == key:
			return d[key][2]
		else:
			return None

def quit(pin, d):
	for key in d.keys():
		if pin == key:
			x = input('Would you like to leave the transaction? y or n? ')
			if x == 'y':
				print('{} {}, thanks for using the ABC Banking system'.format(d[key][0],d[key][1]))
				return x
			elif x == 'n':
				return x

def tester(fname):
	dict = startUp(fname)
	if dict == None:
		return
	pin,msg = verifyPin(dict)
	if pin == None:
		print(msg)
		return 'Goodbye'
	name = msg

	while True:
		print()
		choice = displayMenu(name)
		if choice == 1:
			deposit(pin,dict)
		elif choice == 2:
			withdraw(pin,dict)
		elif choice == 3:
			b = balance(pin,dict)
			msg = 'Current balance is ${:,.2f}'
			print('\n',msg.format(b))
		elif choice == 4:
			reply = quit(pin,dict)
			if reply == 'n':
				pass
			else:
				break
	return 'Goodbye'