class Card:
	def __init__(self, name: str, amount: float):
		self.name = name
		self.funds = amount
	
	def is_swipe_proper(self, direction: str):
		return direction == 'Left-Right'
	
	def is_read_correct(self):
		return self.name != None and self.funds != None
	
	def is_in_credit(self, price: float):
		return self.funds is not None and self.funds >= price
	
	def do_card_status(self, flag: bool):
		if flag:
			print('\nCard is read successfully.')
			print('Welcome, %s!' % self.name)
			print('Current balance: %.2f' % self.funds)
		else:
			print('\nSomething went wrong. Please swipe again properly.')
		return flag
	
	def deduct_funds(self, flag: bool, price: float):
		if flag == True:
			if self.funds >= price:
				self.funds = self.funds - price
				print('Amount %.2f is deducted.' % price)
				print('Current balance: %.2f' % self.funds)
				flag = True
			else:
				print("Unable to deduct %.2f due to insufficient funds." % price)
				flag = False
		else:
			print("No credits were deducted.")
			flag = False
		return flag
	
	def allow_play(self, flag: bool):
		if flag:
			print("Enjoy your game!")
		else:
			print("Unable to play game.")
		return flag