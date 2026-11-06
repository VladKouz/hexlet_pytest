from src.cart import make_cart
import pytest

# BEGIN (write your solution here)
@pytest.fixture()
def cart():
    return make_cart()

def test_cart_initial_state(cart):
    assert cart.get_items() == []
    assert cart.get_count() == 0
    assert cart.get_cost() == 0

def test_cart_add_item(cart):
    good = {'name': 'apple', 'price': 10}
    cart.add_item(good, 2)
    assert cart.get_items() == [{'good': good, 'count': 2}]
    assert cart.get_count() == 2
    assert cart.get_cost() == 20

def test_cart_add_multiple_items(cart):
    good1 = {'name': 'apple', 'price': 10}
    good2 = {'name': 'banana', 'price': 5}
    cart.add_item(good1, 2)
    cart.add_item(good2, 3)
    assert cart.get_items() == [{'good': good1, 'count': 2}, {'good': good2, 'count': 3}]
    assert cart.get_count() == 5
    assert cart.get_cost() == 35

def test_cart_get_items(cart):
    good = {'name': 'apple', 'price': 10}
    cart.add_item(good, 2)
    assert cart.get_items() == [{'good': good, 'count': 2}]

def test_cart_get_count(cart):
    good = {'name': 'apple', 'price': 10}
    cart.add_item(good, 2)
    assert cart.get_count() == 2

def test_cart_get_cost(cart):
    good = {'name': 'apple', 'price': 10}
    cart.add_item(good, 2)
    assert cart.get_cost() == 20

def test_cart_get_items_count_cost(cart):
    good = {'name': 'apple', 'price': 10}
    cart.add_item(good, 2)
    assert cart.get_items() == [{'good': good, 'count': 2}]
    assert cart.get_count() == 2
    assert cart.get_cost() == 20


# END
