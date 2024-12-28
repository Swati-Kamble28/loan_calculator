import pytest
from src.loan_calculator import LoanCalculator

# Test Case 1: Test valid loan interest calculation
def test_calculate_interest():
    calculator = LoanCalculator(principal=1000, rate=5, time=3)
    assert calculator.calculate_interest() == 150  # (1000 * 5 * 3) / 100

# Test Case 2: Test total amount (principal + interest)
def test_calculate_total_amount():
    calculator = LoanCalculator(principal=1000, rate=5, time=3)
    assert calculator.calculate_total_amount() == 1150  # 1000 + 150

# Test Case 3: Test monthly payment for a valid number of months
def test_calculate_monthly_payment():
    calculator = LoanCalculator(principal=1000, rate=5, time=3)
    assert round(calculator.calculate_monthly_payment(12), 2) == 95.83  # 1150 / 12

# Test Case 4: Test ValueError for negative principal
def test_negative_principal():
    with pytest.raises(ValueError):
        LoanCalculator(principal=-1000, rate=5, time=3)

# Test Case 5: Test ValueError for negative rate
def test_negative_rate():
    with pytest.raises(ValueError):
        LoanCalculator(principal=1000, rate=-5, time=3)

# Test Case 6: Test ValueError for negative time
def test_negative_time():
    with pytest.raises(ValueError):
        LoanCalculator(principal=1000, rate=5, time=-3)

# Test Case 7: Test ValueError for zero months in monthly payment calculation
def test_zero_months():
    calculator = LoanCalculator(principal=1000, rate=5, time=3)
    with pytest.raises(ValueError):
        calculator.calculate_monthly_payment(0)

# Test Case 8: Test monthly payment for edge case (1 month)
def test_one_month_payment():
    calculator = LoanCalculator(principal=1000, rate=5, time=3)
    assert calculator.calculate_monthly_payment(1) == 1150  # 1150 / 1