class Card:

	def __init__(self, name: str, credits: float):
		self.name = name
		self.credits = credits
	
	def is_valid(self):
		return self.name is not None and self.credits is not None

	def deduct_credits(self, amount: float):
		if self.is_valid() and amount is not None:
			if self.credits >= amount:
				self.credits = self.credits - amount
				return True
		return False