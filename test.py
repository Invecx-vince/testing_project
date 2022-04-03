from card import Card
import unittest

class TestStringMethods(unittest.TestCase):
	def test_scenario1(self): #TTT
		card = Card("Juan",1000.00)
		#c1. Given the card of the user is swiped in the right direction
		c1 = card.swipeDirection('Left-Right')
		self.assertEqual(c1, True)
		#c2. Card details were read properly
		c2 = card.isReadable()
		self.assertEqual(c2, True)
		#c3. Card contains sufficient funds to play the machine
		c3 = card.sufficientFunds(18.00)
		self.assertEqual(c3, True)

		if c1 and c2 and c3:
			#a1. notify that the reading of the card was successful
				a1 = card.read_status(c1)
				self.assertEqual(a1, True)
			#a2. funds within the card are deducted
				a2 = card.deductFunds(a1, 18.00)
				self.assertEqual(a2, True)
			#a3. the user is given 1 credit to play the machine
				a3 = card.grantCredit(a1 and a2)
				self.assertEqual(a3, True)
	def test_scenario2(self): #TTF
		card = Card("Juan",1000.00)
		#c1. Given the card of the user is swiped in the right direction
		c1 = card.swipeDirection('Left-Right')
		self.assertEqual(c1, True)
		#c2. Card details were read properly
		c2 = card.isReadable()
		self.assertEqual(c2, True)
		#c3. Card contains insufficient funds to play the machine
		c3 = card.sufficientFunds(1001.00)
		self.assertEqual(c3, False)

		if c1 and c2 and (not c3):
			#a1. notify that the reading of the card was successful
				a1 = card.read_status(c1)
				self.assertEqual(a1, True)
			#a2. funds within the card are not deducted
				a2 = card.deductFunds(a1, 1001.00)
				self.assertEqual(a2, False)
			#a3. the user is given 1 credit to play the machine
				a3 = card.grantCredit(a1 and a2)
				self.assertEqual(a3, False)
	def test_scenario3(self): #TFT
		card = Card(None ,1000.00)
		#c1. Given the card of the user is swiped in the right direction
		c1 = card.swipeDirection('Left-Right')
		self.assertEqual(c1, True)
		#c2. Card details were not read properly
		c2 = card.isReadable()
		self.assertEqual(c2, False)
		#c3. Card contains sufficient funds to play the machine
		c3 = card.sufficientFunds(18.00)
		self.assertEqual(c3, True)

		if c1 and (not c2) and c3:
			#a1. notify that the reading of the card was unsuccessful
				a1 = card.read_status(c1)
				self.assertEqual(a1, False)
			#a2. funds within the card are not deducted
				a2 = card.deductFunds(a1, 18.00)
				self.assertEqual(a2, False)
			#a3. the user is not given 1 credit to play the machine
				a3 = card.grantCredit(a1 and a2)
				self.assertEqual(a3, False)

	def test_scenario4(self): #TFF
	def test_scenario5(self): #FTT
	def test_scenario6(self): #FTF
	def test_scenario7(self): #FFT

	def test_scenario8(self): #FFF
		card = Card(None ,None)
		#c1. Given the card of the user is swiped in the wrong direction
		c1 = card.swipeDirection('Right-Left')
		self.assertEqual(c1, False)
		#c2. Card details were not read properly
		c2 = card.isReadable()
		self.assertEqual(c2, False)
		#c3. Card contains insufficient funds to play the machine
		c3 = card.sufficientFunds(1001.00)
		self.assertEqual(c3, False)

		if (not c1) and (not c2) and (not c3):
			#a1. notify that the reading of the card was unsuccessful
				a1 = card.read_status(c1)
				self.assertEqual(a1, False)
			#a2. funds within the card are not deducted
				a2 = card.deductFunds(a1, 1001.00)
				self.assertEqual(a2, False)
			#a3. the user is not given 1 credit to play the machine
				a3 = card.grantCredit(a1 and a2)
				self.assertEqual(a3, False)


if __name__ == '__main__':
	unittest.main()
