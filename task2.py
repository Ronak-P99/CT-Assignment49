class HistoryStack:
    def __init__(self):
        self.pages = []
    
    def push(self, page):
        """Add an history to the top of the stack."""
        self.pages.append(page)

    def pop(self):
        """Remove and return the top history from the stack."""
        if not self.is_empty():
            return self.pages.pop()
        
    def peek(self):
        """Return the top history from the stack without removing it."""
        if not self.is_empty():
            return self.pages[-1]
        
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.pages) == 0
    
    def size(self):
        """Return the number of pages in the stack."""
        return len(self.pages)