from calculator import divide
import pytest
def test_divide():
    assert divide(10,3) == pytest.approx(3.33333, abs=3.4e-06)
    assert divide(0,2) == 0,"0/2= 0"
    with pytest.raises(ValueError,match="cannot divide by zero"):
        divide(10,0)