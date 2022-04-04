class Card:
	name = ''
	funds = 0.00

	def __init__(self, name: str, amount: float):
		self.name = name
		self.funds = amount
	