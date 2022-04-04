from card import Card

class Swipe:
	direction: str = ''
	funds: float = 0.00
	flag: bool = False
	card = None
	def __init__(self, direction: str, price: float, card: Card):
		self.direction = direction
		self.funds = fund
		self.card = card

	def is_swipe_proper(self):
		return self.direction == 'Left-Right'
	
	def is_read_correct(self):
		return self.card.name != None and self.card.funds != None
	
	def is_in_credit(self):
		self.flag = self.card.funds is not None and self.card.funds >= price
		return flag
	
	def do_card_status(self):
		if self.flag:
			print('\nCard is read successfully.')
			print('Welcome, %s!' % self.card.name)
			print('Current balance: %.2f' % self.card.funds)
		else:
			print('\nSomething went wrong. Please swipe again properly.')
		return self.flag
	
	def deduct_funds(self):
		if self.flag == True:
			if self.card.funds >= self.price:
				self.card.funds = self.funds - self.price
				print('Amount %.2f is deducted.' % self.price)
				print('Current balance: %.2f' % self.card.funds)
				self.flag = True
			else:
				print("Unable to deduct %.2f due to insufficient funds." % self.price)
				self.flag = False
		else:
			print("No credits were deducted.")
			self.flag = False
		return self.flag
	
	def allow_play(self):
		if self.flag:
			print("Enjoy your game!")
		else:
			print("Unable to play game.")
		return self.flag