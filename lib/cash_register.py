#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self._discount = discount
    self.total = 0
    self.items = []
    self.previous_transactions = []

  # Getter function for 'discount'
  @property
  def discount(self):
    return self._discount
  
  # Setter function for 'discount'
  @discount.setter
  def discount(self, discount):
    if isinstance(discount, int) and 0 <= discount <= 100:
      self._discount = discount
    else:
      print("Not valid discount")
      
  # Function to add items
  def add_item(self, item, price, quantity=None):
    # Adds price to the 'total'
    if isinstance(quantity, int):
      self.total = self.total + (price * quantity)
      x = 0
      while x < quantity:
        self.items.append(item)
        x += 1
    else:
      self.total += price
    
      # Adds 'item' to the items list
      self.items.append(item)
    # Adds details about the transaction to the 'previous_transactions' list
    self.previous_transactions.append({
      'item': item,
      'price': price,
      'quantity': quantity
    })
    
  def apply_discount(self):
    if self._discount > 0:
      discount = self.total * self._discount/100
      self.total -= discount
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
      return
    
  def void_last_transaction(self):
    if not self.previous_transactions:
      print("There is no transaction to void.")
      return
    
    # Handles subtracting the price of the removed item from the 'total'
    last_item = self.previous_transactions[-1]
    if type(last_item['quantity']) == int:
      self.total = self.total - (last_item['price'] * last_item['quantity'])

    # Removes the last item in the 'previous_transactions' list
    self.previous_transactions.pop()
    
    # Removes the last item in the 'items' list to match 'previous_transactions' list
    self.items.pop()
    
    
c1 = CashRegister()
c1.add_item('tomato', 1.76)
print(c1.items)
print(c1.previous_transactions)
print(c1.total) 


c1.void_last_transaction()
print(c1.items)
print(c1.previous_transactions)
print(c1.total) 