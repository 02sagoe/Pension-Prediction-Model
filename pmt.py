def calculate_pmt(present_value, payment_term, payment_cycle='annual', interest_rate=0.01, future_value=None, type=0):    
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

    number_of_payment_period_minus = number_of_payment_periods - (2 * number_of_payment_periods) #converts value into a negative

    pmt_value_numerator = present_value * payment_rate # numerator calculation
    pmt_value_denominator = (1 - ((1 + payment_rate) ** number_of_payment_period_minus)) # denominator calculation
    pmt_value = pmt_value_numerator / pmt_value_denominator #final caulculation

    return pmt_value