from card import Card
from swipe import Swipe
import unittest

class TestScenario1(unittest.TestCase):
	'''
	TTT
	+Scenario 1: Card is swiped properly, read correctly, and in credit+.
	'''
	def test_scenario_1(self):
		card = Card("Juan", 1000.00)
		swipe = Swipe(direction = 'Left-Right',price = 18.00,card = card)
		#c1: Given the card is swiped in the right direction
		c1 = card.is_swipe_proper()
		self.assertEqual(c1, True)
		#c2: And the card details are read correctly
		c2 = card.is_read_correct()
		self.assertEqual(c2, True)
		#c3: When the card contains sufficient credits
		c3 = card.is_in_credit()
		self.assertEqual(c3, True)

		if c1 and c2 and c3:
			#a1: Then notify that the card is read successfully
			a1 = card.do_card_status()
			self.assertEqual(a1, True)
			#a2: And deduct credits from the card
			a2 = card.deduct_funds()
			self.assertEqual(a2, True)
			#a3: And allow the user to play the machine once
			a3 = card.allow_play()
			self.assertEqual(a3, True)

if __name__ == '__main__':
	unittest.main()