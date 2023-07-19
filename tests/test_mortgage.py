from parameterized_mortgage import Mortgage

value = 100000
rate = 8
term = 30
repayment = 733.76
total_interest = 164155.25
mean_interest = round(total_interest / term / 12, 2)

loan = Mortgage(value, rate, 30)


def test_loan_periodic_repayment():
    assert round(loan.periodic_repayment, 2) == repayment

def test_loan_total_interest():
    assert round(loan.total_interest, 2) == total_interest

def test_loan_mean_interest():
    assert round(loan.mean_interest_per_payment_period, 2) == mean_interest