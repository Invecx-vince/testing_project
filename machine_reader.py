from machine import Machine
from card import Card

class MachineReader:

  def __init__(self, machine: Machine, card: Card) -> None:  
    self.machine = machine
    self.card = card
    self.play = self.is_machine_available() and self.is_card_valid() and self.is_credits_sufficient()

  def is_machine_available(self):
    return self.machine.is_available()

  def is_card_valid(self):
    return self.card.is_valid()

  def is_credits_sufficient(self):
    if self.card.credits is not None and self.machine.cost is not None:
      return self.card.credits >= self.machine.cost
    return False

  def notify_request_viable(self):
    if self.play:
      print('Green Light: You can play this game.')
      return True
    else:
      print('Red Light: You cannot play this game.')
      return False

  def deduct_credits(self):
    if self.play:
      self.card.deduct_credits(self.machine.cost)
      print('Amount %.2f is deducted. Current balance is %.2f' % (self.machine.cost, self.card.credits))
      return True
    else:
      print('No credits were deducted.')
      return False

  def allow_play(self):
    if self.play:
      print('Enjoy playing %s!' % self.machine.name)
      return self.machine.play()
    else:
      print('Swipe your card to play.')
      return False

  def is_machine_card_valid(self):
    return self.machine.is_valid() and self.card.is_valid()