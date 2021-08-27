from dummy_basic.get import get_hello, get_hello_world


def test_get_hello():
    assert "hello" == get_hello()
    
def test_get_hello_world():
    assert "hello_world" == get_hello_world()