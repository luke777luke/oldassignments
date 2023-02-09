#Lukasz Grzybek
class TransitCard:
	maxTrans = 100.00

	def __init__(self,amount = 5.00):
		#initializes balance to a default value of $5.00
		if amount > TransitCard.maxTrans:
			raise ValueError('Amount is >100.00')
		elif amount <= TransitCard.maxTrans:
			self.b = amount

	def ride(self,fare):
		#Finds the difference bewteen the card's current balance and the fare amount after a transit ride
		
		if self.b <= 0.00:
			raise ValueError('Card balance is 0 or negative; ride is denied')
		elif self.b > 0.00 and self.b < fare:
			self.b -= fare
		elif self.b > 0.00 and self.b > fare:
			self.b -= fare

	def addValue(self, amount):
		#Adds additional amount to current balance
		total = self.b + amount
		maxBalance = 350.00
		if amount > 100.00:
			raise ValueError('Amount is >100.00')
		elif amount <= TransitCard.maxTrans and total > maxBalance:
			raise ValueError('Card balance will be greater than 350.00; request is denied')
		elif amount <= TransitCard.maxTrans and total <= maxBalance:
			self.b += amount

	def balance(self):
		#Displays current balance on the card
		return '${:6.2f}'.format(self.b)

	def __repr__(self):
		# returns a canonical string representation of the balance
		return 'The card balance is ${:6.2f}'.format(self.b)





