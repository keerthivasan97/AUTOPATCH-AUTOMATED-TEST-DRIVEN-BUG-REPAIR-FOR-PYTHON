from calculator import divide
import pytest
def test_divide():
    assert divide(10,2) ==5
    with pytest.raises(ValueError,match="cannot divide by zero"):
        divide(10,0)