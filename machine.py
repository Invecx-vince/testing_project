class Machine:

  def __init__(self, name: str, cost: float, available: bool) -> None:
    self.name = name
    self.cost = cost
    self.available = available

  def is_valid(self):
    return self.name is not None and self.cost is not None and self.available is not None

  def is_available(self):
    return self.available if self.is_valid() else False

  def play(self):
    return True if self.is_valid() else False