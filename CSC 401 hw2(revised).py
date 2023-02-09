#Lukasz Grzybek

#Resubmitting due to an output error stemming from line 38, which led to further errors in case #2.

x = input('Enter number of membership type, services, number of months: ')

if int(x[0]) == 1:
	member_description = 'Standard adult'
	member_fee = 40
if int(x[0]) == 2:
	member_description = 'Child (age 12 and under)'
	member_fee = 20
if int(x[0]) == 3:
	member_description = 'Student'
	member_fee = 25
if int(x[0]) == 4:
	member_description = 'Senior citizen (age 65 and over)'
	member_fee = 30

if int(x[1]) == 0:
	additional_fee = 0
	lesson_description = 'no additional lessons'
if int(x[1]) == 1:
	additional_fee = 10
	lesson_description = 'Yoga'
if int(x[1]) == 2:
	additional_fee = 50
	lesson_description = 'Personal Trainer'
if int(x[1]) == 3:
	additional_fee = 60
	lesson_description = 'Yoga and Personal Trainer'

if int(x[2]) in [1,2,3]:
	discount = 0
if int(x[2]) in [4,5,6]:
	discount = 0.05
if int(x[2]) in [7,8,9]:
	discount = 0.08
if int(x[2:]) >= 10:
	discount = 0.10

monthly_fee = (member_fee + additional_fee) - ((member_fee + additional_fee) * discount)

monthy_fee_rounded = str(round(monthly_fee, 2))
if monthy_fee_rounded[-2] == '.':
	monthy_fee_rounded = str(round(monthly_fee, 2)) + '0'

total_fee = float(monthy_fee_rounded) * int(x[2:])

total_fee_rounded = str(round(total_fee, 2))
if total_fee_rounded[-2] == '.':
	total_fee_rounded = str(round(total_fee, 2)) + '0'

print(member_description + ' ' + 'with' + ' ' + lesson_description + ' ' + 'for' + ' ' + x[2:] + ' ' + 'months')
print('Monthly fee =' + ' ' + '$'+ monthy_fee_rounded)
print('Total =' + ' ' + '$' + total_fee_rounded)

if x[1] != 0:
	print('Redeem your free drink at the juice bar using code:' + ' ' + x)

#Case 1 - When the input string is 137, the resulting message describes a 'Standard adult with Yoga and Personal Trainer for 7 months'. The monthly fee calculates to '$92.00' and the total fee results in '$644.00'. Due to the customer choosing optional lessons, the message 'Redeem your free drink at the juice bar using code 137' is displayed.

#Case 2 - When the input string is 2215, the resulting message describes a 'Student with Yoga for 15 months'. The monthly fee calculates to '$63.00' and the total fee results in '$945.00'. Due to the customer choosing optional lessons, the message 'Redeem your free drink at the juice bar using code 2215' is displayed.