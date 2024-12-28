"""
This module provides a class for calculating loan details such as interest,
total amount, and monthly payments.
"""
class LoanCalculator:
    """
    A class to calculate loan-related financial details.
    Attributes:
        principal (float): The principal amount of the loan.
        rate (float): The annual interest rate (as a percentage).
        time (float): The loan duration in years.
    """
    def __init__(self, principal, rate, time):
        """
        Initialize the LoanCalculator with principal, rate, and time.
        Args:
            principal (float): The principal amount of the loan (non-negative).
            rate (float): The annual interest rate as a percentage (non-negative).
            time (float): The loan duration in years (non-negative).
        Raises:
            ValueError: If any of the arguments are negative.
        """
        if principal < 0 or rate < 0 or time < 0:
            raise ValueError("Principal, rate, and time must be non-negative")
        self.principal = principal
        self.rate = rate
        self.time = time
    def calculate_interest(self):
        """
        Calculate the simple interest on the loan.
        Returns:
            float: The calculated interest.
        """
        return (self.principal * self.rate * self.time) / 100
    def calculate_total_amount(self):
        """
        Calculate the total amount to be paid after the loan duration.
        Returns:
            float: The total amount including the principal and interest.
        """
        return self.principal + self.calculate_interest()
    def calculate_monthly_payment(self, months):
        """
        Calculate the monthly payment for the loan.
        Args:
            months (int): The number of months to pay off the loan.
        Returns:
            float: The monthly payment amount, rounded to 2 decimal places.
        Raises:
            ValueError: If the number of months is non-positive.
        """
        if months <= 0:
            raise ValueError("Months must be positive")
        total = self.calculate_total_amount()
        return round(total / months, 2)  # Round to 2 decimal places
# Fix trailing blank lines and ensure exactly one newline at the end
FILE_PATH = "src/loan_calculator.py"
with open(FILE_PATH, "r", encoding="utf-8") as file:
    lines = file.readlines()
with open(FILE_PATH, "w", encoding="utf-8") as file:
    file.writelines([
        line.rstrip() + "\n"
        for line in lines
        if line.strip() or not lines[-1].strip()
    ])
