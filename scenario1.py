from machine import Machine
from card import Card
from machine_reader import MachineReader
import unittest

class TestScenario1(unittest.TestCase):
	'''
	TTT
	+Scenario 1: Machine is available, card is valid and in credit+.
	c1: Given the arcade machine is available
	c2: And the card details are valid
	c3: When the card contains sufficient credits
	a1: Then notify that the request is viable
	a2: And deduct credits from the card
	a3: And allow the user to play
	'''
	def setUp(self) -> None:
		self.machine = Machine(name = 'Air Hockey', cost = 20.00, available = True)
		self.card = Card('Juan', 500.00)
		self.machine_reader = MachineReader(self.machine, self.card)
		return super().setUp()

	def test1_machine_available(self):
		c1 = self.machine_reader.is_machine_available()
		self.assertEqual(c1, True)

	def test2_card_valid(self):
		c2 = self.machine_reader.is_card_valid()
		self.assertEqual(c2, True)

	def test3_credits_sufficient(self):
		c3 = self.machine_reader.is_credits_sufficient()
		self.assertEqual(c3, True)

	def test4_notify_request_viable(self):
		a1 = self.machine_reader.notify_request_viable()
		self.assertEqual(a1, True)

	def test5_deduct_credits(self):
		a2 = self.machine_reader.deduct_credits()
		self.assertEqual(a2, True)

	def test6_allow_play(self):
		a3 = self.machine_reader.allow_play()
		self.assertEqual(a3, True)

if __name__ == '__main__':
	unittest.main()