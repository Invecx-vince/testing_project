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
    return self.card.credits >= self.machine.cost if self.is_machine_card_valid() else False

  def notify_request_viable(self):
    if not self.is_machine_card_valid():
      print('Red Light: Something went wrong.')
      return False
    if self.is_credits_sufficient():
      print('Green Light: You can play this game.')
      return True
    else:
      print('Red Light: Insufficient balance to play.')
      return False

  def deduct_credits(self):
    return self.card.deduct_credits(self.machine.cost)

  def allow_play(self):
    if self.play:
      print('Enjoy playing %s!' % self.machine.name)
      return self.machine.play()
    else:
      print('Swipe your card to play.')
      return False

  def is_machine_card_valid(self):
    return self.machine.is_valid() and self.card.is_valid()