from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.size = jar.deposit(1)
    assert str(jar) == "🍪"
    jar.size = jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar=Jar(10, 0)
    jar.size = jar.deposit(5)
    assert jar.size ==  5
    jar1 = Jar(10, 0)
    jar1.size = jar1.deposit(-5)
    assert pytest.raises(ValueError)


def test_withdraw():
    jar=Jar(10, 10)
    jar.size = jar.withdraw(6)
    assert jar.size ==  4
    jar1 = Jar(10, 10)
    jar1.deposit(-5)
    assert pytest.raises(ValueError)

"""Open your test_jar.py file and import your Jar class with from jar import Jar. 
Create a function called test_init, wherein you create a new instance of Jar with jar = Jar(). 
assert that this jar has the capacity it should, then run your tests with pytest test_jar.py.

Add another function to your test_jar.py file called test_str. In test_str, create a new instance of your Jar class and deposit a few cookies. 
assert that str(jar) prints out as many cookies as have been deposited, then run your tests with pytest test_jar.py.

Add another function to your test_jar.py file called test_deposit. 
In test_deposit, create a new instance of your Jar class and deposit a few cookies. 
assert that the jar’s size attribute is as large as the number of cookies that have been deposited. 
Also assert that, if you deposit more than the jar’s capacity, deposit should raise a ValueError. Run your tests with pytest test_jar.py.

Add another function to your test_jar.py file called test_withdraw. 
In test_withdraw, create a new instance of your Jar class and first deposit a few cookies. 
assert that withdrawing from the jar leaves the appropriate number of cookies in the jar’s size attribute. 
Also assert that, if you withdraw more than the jar’s size, withdraw should raise a ValueError. Run your tests with pytest test_jar.py."""