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
  def add_item(self, item, price, quantity=0):
    # Adds price to the 'total'
    self.total += price
      
    # Adds 'item' to the items list
    self.items.append(item)
    
    # Adds details about the transaction to the 'previous_transactions' list
    transaction = {
      'item': item,
      'price': price,
      'quantity': quantity
    }
    self.previous_transactions.append(transaction)
    
  def apply_discount(self):
    if not self.previous_transactions:
      print("There is no discount to apply.")
      return 
    else:
      discount = self.total * self._discount/100
      last_item = self.previous_transactions[-1]
    
      self.total -= discount 
      self.previous_transactions.pop()
      self.total -= last_item['price']
      self.items.pop()
    
    
