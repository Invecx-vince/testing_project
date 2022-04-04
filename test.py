from card import Card
import unittest

class TestStringMethods(unittest.TestCase):
	'''
	TTT
	+Scenario 1: Card is swiped properly, read correctly, and in credit+.
	'''
	def test_scenario_1(self):
		card = Card("Juan", 1000.00)
		machine_cost = 18.00
		#c1: Given the card is swiped in the right direction
		c1 = card.is_swipe_proper('Left-Right')
		self.assertEqual(c1, True)
		#c2: And the card details are read correctly
		c2 = card.is_read_correct()
		self.assertEqual(c2, True)
		#c3: When the card contains sufficient credits
		c3 = card.is_in_credit(machine_cost)
		self.assertEqual(c3, True)

		if c1 and c2 and c3:
			#a1: Then notify that the card is read successfully
			a1 = card.do_card_status(c1 and c2)
			self.assertEqual(a1, True)
			#a2: And deduct credits from the card
			a2 = card.deduct_funds(a1, machine_cost)
			self.assertEqual(a2, True)
			#a3: And allow the user to play the machine once
			a3 = card.allow_play(a1 and a2)
			self.assertEqual(a3, True)
	
	'''
	TTF
	+Scenario 2: Card is swiped properly, read correctly, and not in credit+.
	'''
	def test_scenario_2(self):
		card = Card("Juan", 1000.00)
		machine_cost = 1001.00
		#c1: Given the card is swiped in the right direction
		c1 = card.is_swipe_proper('Left-Right')
		self.assertEqual(c1, True)
		#c2: And the card details are read correctly
		c2 = card.is_read_correct()
		self.assertEqual(c2, True)
		#c3: When the card contains insufficient credits
		c3 = card.is_in_credit(machine_cost)
		self.assertEqual(c3, False)

		if c1 and c2 and not c3:
			#a1: Then notify that the card is read successfully
			a1 = card.do_card_status(c1 and c2)
			self.assertEqual(a1, True)
			#a2: And do not deduct credits from the card
			a2 = card.deduct_funds(a1, machine_cost)
			self.assertEqual(a2, False)
			#a3: And do not allow the user to play the machine
			a3 = card.allow_play(a1 and a2)
			self.assertEqual(a3, False)
	
	'''
	TFT
	+Scenario 3: Card is swiped properly, read incorrectly, and in credit+.
	'''
	def test_scenario_3(self):
		card = Card(None, 1000.00)
		machine_cost = 18.00
		#c1: Given the card is swiped in the right direction
		c1 = card.is_swipe_proper('Left-Right')
		self.assertEqual(c1, True)
		#c2: And the card details are read incorrectly
		c2 = card.is_read_correct()
		self.assertEqual(c2, False)
		#c3: When the card contains sufficient credits
		c3 = card.is_in_credit(machine_cost)
		self.assertEqual(c3, True)

		if c1 and not c2 and c3:
			#a1: Then notify that the card is read unsuccessfully
			a1 = card.do_card_status(c1 and c2)
			self.assertEqual(a1, False)
			#a2: And do not deduct credits from the card
			a2 = card.deduct_funds(a1, machine_cost)
			self.assertEqual(a2, False)
			#a3: And do not allow the user to play the machine
			a3 = card.allow_play(a1 and a2)
			self.assertEqual(a3, False)

	'''
	TFF
	+Scenario 4: Card is swiped properly, read incorrectly, and not in credit+.
	'''
	def test_scenario_4(self):
		card = Card(None, 1000.00)
		machine_cost = 1001.00
		#c1: Given the card is swiped in the right direction
		c1 = card.is_swipe_proper('Left-Right')
		self.assertEqual(c1, True)
		#c2: And the card details are read incorrectly
		c2 = card.is_read_correct()
		self.assertEqual(c2, False)
		#c3: When the card contains sufficient credits
		c3 = card.is_in_credit(machine_cost)
		self.assertEqual(c3, False)

		if c1 and not c2 and not c3:
			#a1: Then notify that the card is read unsuccessfully
			a1 = card.do_card_status(c1 and c2)
			self.assertEqual(a1, False)
			#a2: And do not deduct credits from the card
			a2 = card.deduct_funds(a1, machine_cost)
			self.assertEqual(a2, False)
			#a3: And do not allow the user to play the machine
			a3 = card.allow_play(a1 and a2)
			self.assertEqual(a3, False)

	'''
	FTT
	+Scenario 5: Card is swiped improperly, read correctly, and in credit+.
	'''
	def test_scenario_5(self):
		card = Card('Juan', 1000.00)
		machine_cost = 18.00
		#c1: Given the card is swiped in the wrong direction
		c1 = card.is_swipe_proper('Right-Left')
		self.assertEqual(c1, False)
		#c2: And the card details are read correctly
		c2 = card.is_read_correct()
		self.assertEqual(c2, True)
		#c3: When the card contains sufficient credits
		c3 = card.is_in_credit(machine_cost)
		self.assertEqual(c3, True)

		if not c1 and c2 and c3:
			#a1: Then notify that the card is swiped improperly
			a1 = card.do_card_status(c1 and c2)
			self.assertEqual(a1, False)
			#a2: And do not deduct credits from the card
			a2 = card.deduct_funds(a1, machine_cost)
			self.assertEqual(a2, False)
			#a3: And do not allow the user to play the machine
			a3 = card.allow_play(a1 and a2)
			self.assertEqual(a3, False)
	
	'''
	FTF
	+Scenario 6: Card is swiped improperly, read correctly, and not in credit+.
	'''
	def test_scenario_6(self):
		card = Card('Juan', 1000.00)
		machine_cost = 1001.00
		#c1: Given the card is swiped in the wrong direction
		c1 = card.is_swipe_proper('Right-Left')
		self.assertEqual(c1, False)
		#c2: And the card details are read correctly
		c2 = card.is_read_correct()
		self.assertEqual(c2, True)
		#c3: When the card contains sufficient credits
		c3 = card.is_in_credit(machine_cost)
		self.assertEqual(c3, False)

		if not c1 and c2 and not c3:
			#a1: Then notify that the card is swiped improperly
			a1 = card.do_card_status(c1 and c2)
			self.assertEqual(a1, False)
			#a2: And do not deduct credits from the card
			a2 = card.deduct_funds(a1, machine_cost)
			self.assertEqual(a2, False)
			#a3: And do not allow the user to play the machine
			a3 = card.allow_play(a1 and a2)
			self.assertEqual(a3, False)

	'''
	FFT
	+Scenario 7: Card is swiped improperly, read incorrectly, and in credit+.
	'''
	def test_scenario_7(self):
		card = Card(None, 1000.00)
		machine_cost = 18.00
		#c1: Given the card is swiped in the wrong direction
		c1 = card.is_swipe_proper('Right-Left')
		self.assertEqual(c1, False)
		#c2: And the card details are read correctly
		c2 = card.is_read_correct()
		self.assertEqual(c2, False)
		#c3: When the card contains sufficient credits
		c3 = card.is_in_credit(machine_cost)
		self.assertEqual(c3, True)

		if not c1 and not c2 and c3:
			#a1: Then notify that the card is swiped improperly
			a1 = card.do_card_status(c1 and c2)
			self.assertEqual(a1, False)
			#a2: And do not deduct credits from the card
			a2 = card.deduct_funds(a1, machine_cost)
			self.assertEqual(a2, False)
			#a3: And do not allow the user to play the machine
			a3 = card.allow_play(a1 and a2)
			self.assertEqual(a3, False)

	'''
	FFF
	+Scenario 8: Card is swiped improperly, read incorrectly, and not in credit+.
	'''
	def test_scenario_8(self):
		card = Card(None, None)
		machine_cost = 1001.00
		#c1: Given the card is swiped in the wrong direction
		c1 = card.is_swipe_proper('Right-Left')
		self.assertEqual(c1, False)
		#c2: And the card details are read correctly
		c2 = card.is_read_correct()
		self.assertEqual(c2, False)
		#c3: When the card contains sufficient credits
		c3 = card.is_in_credit(machine_cost)
		self.assertEqual(c3, False)

		if not c1 and not c2 and not c3:
			#a1: Then notify that the card is swiped improperly
			a1 = card.do_card_status(c1 and c2)
			self.assertEqual(a1, False)
			#a2: And do not deduct credits from the card
			a2 = card.deduct_funds(a1, machine_cost)
			self.assertEqual(a2, False)
			#a3: And do not allow the user to play the machine
			a3 = card.allow_play(a1 and a2)
			self.assertEqual(a3, False)

if __name__ == '__main__':
	unittest.main()