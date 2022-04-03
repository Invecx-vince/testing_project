class Card:
	name = ""
	funds = 0.0
	def _init_(self, name: str, amount: float):
		self.name = name
		self.funds = amount

	def swipeDirection(self, direction: str):
		return direction == 'Left-Right'
	def isReadable(self)
		return self.name != None and self.funds != None
	def sufficientFunds(self, price: float):
		return (funds is not None) and funds>=price
		
	def read_status(self, flag: bool):
		if flag:
			print("Card read Successful!\n Welcome, {}".format(self.name))
		else:
			print("Card read Unsuccessful. Please swipe again.")
		return flag
	def deductFunds(self, flag: bool, price: float):
		if flag == True:
			if funds >= price:
				funds = funds - price
				print("Current balance: {}".format(self.funds))
				flag = True
			else:
				print("Unable to deduct due to insufficient funds")
				flag = False
		else:
			print("Unable to deduct due to unreadable funds")
			flag = False

		return flag
	def grantCredit(self, flag: bool):
		if flag:
			print("Enjoy your game!")
		else:
			print("Unable to play game.")
		return flag