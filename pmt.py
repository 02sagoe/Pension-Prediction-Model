def pmt(present_value, payment_term, payment_cycle='annual', interest_rate=0.01, future_value=None, type=0):    
    payment_cycle.lower()
    payment_cycle_dictionary = {
        'annual': 1,
        'bi-annual': 2,
        'thirdly': 3,
        'quaterly': 4,
        'monthly': 12,
    }
    number_of_payment_periods = payment_term * payment_cycle_dictionary[payment_cycle]
    payment_rate = interest_rate / payment_cycle_dictionary[payment_cycle]

    pmt_value_numerator = present_value * payment_rate * ((1 + interest_rate)** number_of_payment_periods)
    pmt_value_denominator = (((1 + interest_rate)** number_of_payment_periods) - 1)
    pmt_value = pmt_value_numerator/pmt_value_denominator

    return pmt_value

def car_loan_scenario(loan_amount, annual_interest_rate, loan_term, payment_cycle):
    return f"You have decided to take out a car loan of ${loan_amount} with an annual interest rate", 
    f"of {annual_interest_rate*100}% and a loan term of {loan_term} years with {payment_cycle} payments.", 
    f"\nYour {payment_cycle} payment amount would be stated below:"

#loan_amount = input('What amount ($) of a loan do you want take?: ')
#loan_amount = round(float(loan_amount), 2)
loan_amount = 20000

annual_interest_rate = 0.05

payment_cycle = 'monthly'
payment_cycle = payment_cycle.lower()

#loan_term  = input('How long (years) will you need to pay back the full amount plus the required interest?')
#loan_term = int(loan_term)
loan_term = 4

loan_scenario = car_loan_scenario(loan_amount, annual_interest_rate, loan_term, payment_cycle)
loan_scenario
payment = pmt(loan_amount, loan_term, payment_cycle, annual_interest_rate)
print(payment)