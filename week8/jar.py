import sys

class Jar:
    #__init__ should initialize a cookie jar with the given capacity, which represents the maximum number of cookies that can fit in the cookie jar.
    #If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    #__str__ should return a str with  🍪, where  is the number of cookies in the cookie jar.
    def __str__(self):
        return f"🍪"*self.size

    #deposit should add n cookies to the cookie jar. 
    #If adding that many would exceed the cookie jar’s capacity, though, deposit should instead raise a ValueError.
    def deposit(self, n):
        if self.size + n <= self.capacity:
            return (self.size + n)
        else:
            raise ValueError

    #withdraw should remove n cookies from the cookie jar. Nom nom nom. 
    #If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
    def withdraw(self, n):
        if self.size - n >=0:
            return (self.size - n)
        else:
            raise ValueError
        
    #capacity should return the cookie jar’s capacity.
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if capacity <= 0:
            raise ValueError
        self._capacity = capacity

    #size should return the number of cookies actually in the cookie jar, initially 0.
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if 0 > size > self.capacity:
            raise ValueError
        else:
            self._size = size

def main():
    try:
        limit = int(input("Capacity: "))
        action=input("Depost or Withdraw?: ").lower()
        amount = int(input("Amount? "))
        if limit >0 and amount >0:
            jar=Jar(limit, 5)
        else:
            raise ValueError                
    except ValueError:
        if limit <= 0:
            sys.exit("Invalid capacity")
        else:
            sys.exit("Invalid amount")

    if action == "deposit":
        try:
            jar.size = jar.deposit(amount)
            print(jar)
        except ValueError:
            sys.exit("Not enough capacity")
    elif action == "withdraw":
        try:
            jar.size = jar.withdraw(amount)
            print(jar)
        except ValueError:
            sys.exit("Not enough cookies")

if __name__ == "__main__":
    main()