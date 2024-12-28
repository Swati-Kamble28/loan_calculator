
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


class LoanCalculator:
    def xǁLoanCalculatorǁ__init____mutmut_orig(self, principal, rate, time):
        if principal < 0 or rate < 0 or time < 0:
            raise ValueError("Principal, rate, and time must be non-negative")
        self.principal = principal
        self.rate = rate
        self.time = time
    def xǁLoanCalculatorǁ__init____mutmut_1(self, principal, rate, time):
        if principal <= 0 or rate < 0 or time < 0:
            raise ValueError("Principal, rate, and time must be non-negative")
        self.principal = principal
        self.rate = rate
        self.time = time
    def xǁLoanCalculatorǁ__init____mutmut_2(self, principal, rate, time):
        if principal < 1 or rate < 0 or time < 0:
            raise ValueError("Principal, rate, and time must be non-negative")
        self.principal = principal
        self.rate = rate
        self.time = time
    def xǁLoanCalculatorǁ__init____mutmut_3(self, principal, rate, time):
        if principal < 0 or rate <= 0 or time < 0:
            raise ValueError("Principal, rate, and time must be non-negative")
        self.principal = principal
        self.rate = rate
        self.time = time
    def xǁLoanCalculatorǁ__init____mutmut_4(self, principal, rate, time):
        if principal < 0 or rate < 1 or time < 0:
            raise ValueError("Principal, rate, and time must be non-negative")
        self.principal = principal
        self.rate = rate
        self.time = time
    def xǁLoanCalculatorǁ__init____mutmut_5(self, principal, rate, time):
        if principal < 0 or rate < 0 or time <= 0:
            raise ValueError("Principal, rate, and time must be non-negative")
        self.principal = principal
        self.rate = rate
        self.time = time
    def xǁLoanCalculatorǁ__init____mutmut_6(self, principal, rate, time):
        if principal < 0 or rate < 0 or time < 1:
            raise ValueError("Principal, rate, and time must be non-negative")
        self.principal = principal
        self.rate = rate
        self.time = time
    def xǁLoanCalculatorǁ__init____mutmut_7(self, principal, rate, time):
        if principal < 0 and rate < 0 or time < 0:
            raise ValueError("Principal, rate, and time must be non-negative")
        self.principal = principal
        self.rate = rate
        self.time = time
    def xǁLoanCalculatorǁ__init____mutmut_8(self, principal, rate, time):
        if principal < 0 or rate < 0 or time < 0:
            raise ValueError("XXPrincipal, rate, and time must be non-negativeXX")
        self.principal = principal
        self.rate = rate
        self.time = time
    def xǁLoanCalculatorǁ__init____mutmut_9(self, principal, rate, time):
        if principal < 0 or rate < 0 or time < 0:
            raise ValueError("Principal, rate, and time must be non-negative")
        self.principal = None
        self.rate = rate
        self.time = time
    def xǁLoanCalculatorǁ__init____mutmut_10(self, principal, rate, time):
        if principal < 0 or rate < 0 or time < 0:
            raise ValueError("Principal, rate, and time must be non-negative")
        self.principal = principal
        self.rate = None
        self.time = time
    def xǁLoanCalculatorǁ__init____mutmut_11(self, principal, rate, time):
        if principal < 0 or rate < 0 or time < 0:
            raise ValueError("Principal, rate, and time must be non-negative")
        self.principal = principal
        self.rate = rate
        self.time = None

    xǁLoanCalculatorǁ__init____mutmut_mutants = {
    'xǁLoanCalculatorǁ__init____mutmut_1': xǁLoanCalculatorǁ__init____mutmut_1, 
        'xǁLoanCalculatorǁ__init____mutmut_2': xǁLoanCalculatorǁ__init____mutmut_2, 
        'xǁLoanCalculatorǁ__init____mutmut_3': xǁLoanCalculatorǁ__init____mutmut_3, 
        'xǁLoanCalculatorǁ__init____mutmut_4': xǁLoanCalculatorǁ__init____mutmut_4, 
        'xǁLoanCalculatorǁ__init____mutmut_5': xǁLoanCalculatorǁ__init____mutmut_5, 
        'xǁLoanCalculatorǁ__init____mutmut_6': xǁLoanCalculatorǁ__init____mutmut_6, 
        'xǁLoanCalculatorǁ__init____mutmut_7': xǁLoanCalculatorǁ__init____mutmut_7, 
        'xǁLoanCalculatorǁ__init____mutmut_8': xǁLoanCalculatorǁ__init____mutmut_8, 
        'xǁLoanCalculatorǁ__init____mutmut_9': xǁLoanCalculatorǁ__init____mutmut_9, 
        'xǁLoanCalculatorǁ__init____mutmut_10': xǁLoanCalculatorǁ__init____mutmut_10, 
        'xǁLoanCalculatorǁ__init____mutmut_11': xǁLoanCalculatorǁ__init____mutmut_11
    }

    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLoanCalculatorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁLoanCalculatorǁ__init____mutmut_mutants"), *args, **kwargs)
        return result 

    __init__.__signature__ = _mutmut_signature(xǁLoanCalculatorǁ__init____mutmut_orig)
    xǁLoanCalculatorǁ__init____mutmut_orig.__name__ = 'xǁLoanCalculatorǁ__init__'



    def xǁLoanCalculatorǁcalculate_interest__mutmut_orig(self):
        return (self.principal * self.rate * self.time) / 100

    def xǁLoanCalculatorǁcalculate_interest__mutmut_1(self):
        return (self.principal / self.rate * self.time) / 100

    def xǁLoanCalculatorǁcalculate_interest__mutmut_2(self):
        return (self.principal * self.rate / self.time) / 100

    def xǁLoanCalculatorǁcalculate_interest__mutmut_3(self):
        return (self.principal * self.rate * self.time) * 100

    def xǁLoanCalculatorǁcalculate_interest__mutmut_4(self):
        return (self.principal * self.rate * self.time) / 101

    xǁLoanCalculatorǁcalculate_interest__mutmut_mutants = {
    'xǁLoanCalculatorǁcalculate_interest__mutmut_1': xǁLoanCalculatorǁcalculate_interest__mutmut_1, 
        'xǁLoanCalculatorǁcalculate_interest__mutmut_2': xǁLoanCalculatorǁcalculate_interest__mutmut_2, 
        'xǁLoanCalculatorǁcalculate_interest__mutmut_3': xǁLoanCalculatorǁcalculate_interest__mutmut_3, 
        'xǁLoanCalculatorǁcalculate_interest__mutmut_4': xǁLoanCalculatorǁcalculate_interest__mutmut_4
    }

    def calculate_interest(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLoanCalculatorǁcalculate_interest__mutmut_orig"), object.__getattribute__(self, "xǁLoanCalculatorǁcalculate_interest__mutmut_mutants"), *args, **kwargs)
        return result 

    calculate_interest.__signature__ = _mutmut_signature(xǁLoanCalculatorǁcalculate_interest__mutmut_orig)
    xǁLoanCalculatorǁcalculate_interest__mutmut_orig.__name__ = 'xǁLoanCalculatorǁcalculate_interest'



    def xǁLoanCalculatorǁcalculate_total_amount__mutmut_orig(self):
        return self.principal + self.calculate_interest()

    def xǁLoanCalculatorǁcalculate_total_amount__mutmut_1(self):
        return self.principal - self.calculate_interest()

    xǁLoanCalculatorǁcalculate_total_amount__mutmut_mutants = {
    'xǁLoanCalculatorǁcalculate_total_amount__mutmut_1': xǁLoanCalculatorǁcalculate_total_amount__mutmut_1
    }

    def calculate_total_amount(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLoanCalculatorǁcalculate_total_amount__mutmut_orig"), object.__getattribute__(self, "xǁLoanCalculatorǁcalculate_total_amount__mutmut_mutants"), *args, **kwargs)
        return result 

    calculate_total_amount.__signature__ = _mutmut_signature(xǁLoanCalculatorǁcalculate_total_amount__mutmut_orig)
    xǁLoanCalculatorǁcalculate_total_amount__mutmut_orig.__name__ = 'xǁLoanCalculatorǁcalculate_total_amount'



    def xǁLoanCalculatorǁcalculate_monthly_payment__mutmut_orig(self, months):
        if months <= 0:
            raise ValueError("Months must be positive")
        total = self.calculate_total_amount()
        return round(total / months, 2)  # Round to 2 decimal places

    def xǁLoanCalculatorǁcalculate_monthly_payment__mutmut_1(self, months):
        if months < 0:
            raise ValueError("Months must be positive")
        total = self.calculate_total_amount()
        return round(total / months, 2)  # Round to 2 decimal places

    def xǁLoanCalculatorǁcalculate_monthly_payment__mutmut_2(self, months):
        if months <= 1:
            raise ValueError("Months must be positive")
        total = self.calculate_total_amount()
        return round(total / months, 2)  # Round to 2 decimal places

    def xǁLoanCalculatorǁcalculate_monthly_payment__mutmut_3(self, months):
        if months <= 0:
            raise ValueError("XXMonths must be positiveXX")
        total = self.calculate_total_amount()
        return round(total / months, 2)  # Round to 2 decimal places

    def xǁLoanCalculatorǁcalculate_monthly_payment__mutmut_4(self, months):
        if months <= 0:
            raise ValueError("Months must be positive")
        total = None
        return round(total / months, 2)  # Round to 2 decimal places

    def xǁLoanCalculatorǁcalculate_monthly_payment__mutmut_5(self, months):
        if months <= 0:
            raise ValueError("Months must be positive")
        total = self.calculate_total_amount()
        return round(total * months, 2)  # Round to 2 decimal places

    def xǁLoanCalculatorǁcalculate_monthly_payment__mutmut_6(self, months):
        if months <= 0:
            raise ValueError("Months must be positive")
        total = self.calculate_total_amount()
        return round(total / months, 3)  # Round to 2 decimal places

    xǁLoanCalculatorǁcalculate_monthly_payment__mutmut_mutants = {
    'xǁLoanCalculatorǁcalculate_monthly_payment__mutmut_1': xǁLoanCalculatorǁcalculate_monthly_payment__mutmut_1, 
        'xǁLoanCalculatorǁcalculate_monthly_payment__mutmut_2': xǁLoanCalculatorǁcalculate_monthly_payment__mutmut_2, 
        'xǁLoanCalculatorǁcalculate_monthly_payment__mutmut_3': xǁLoanCalculatorǁcalculate_monthly_payment__mutmut_3, 
        'xǁLoanCalculatorǁcalculate_monthly_payment__mutmut_4': xǁLoanCalculatorǁcalculate_monthly_payment__mutmut_4, 
        'xǁLoanCalculatorǁcalculate_monthly_payment__mutmut_5': xǁLoanCalculatorǁcalculate_monthly_payment__mutmut_5, 
        'xǁLoanCalculatorǁcalculate_monthly_payment__mutmut_6': xǁLoanCalculatorǁcalculate_monthly_payment__mutmut_6
    }

    def calculate_monthly_payment(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLoanCalculatorǁcalculate_monthly_payment__mutmut_orig"), object.__getattribute__(self, "xǁLoanCalculatorǁcalculate_monthly_payment__mutmut_mutants"), *args, **kwargs)
        return result 

    calculate_monthly_payment.__signature__ = _mutmut_signature(xǁLoanCalculatorǁcalculate_monthly_payment__mutmut_orig)
    xǁLoanCalculatorǁcalculate_monthly_payment__mutmut_orig.__name__ = 'xǁLoanCalculatorǁcalculate_monthly_payment'


