class OrderQueue:
    def __init__(self):
        self.orders = []
    
    def take_order(self, order):
        """Adds a order to the end of the queue."""
        self.orders.append(order)
    
    def order_fullfilled(self):
        """Removes and returns the first order from the queue."""
        if not self.is_empty():
            return self.orders.pop(0)
        
    def is_empty(self):
        """Checks if the queue is empty."""
        return len(self.orders) == 0
    
order_queue = OrderQueue()

order_queue.take_order({"Order_Number": 1, "Appetizer": "Nachos", "Entree": "Steak", "Drink": "Lemonade"})