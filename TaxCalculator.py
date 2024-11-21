def calculate_irpf(income):
    brackets = [
        (12450, 0.19),
        (20200, 0.24),
        (35200, 0.30),
        (60000, 0.37),
        (float('inf'), 0.45)
    ]
    tax = 0
    previous_limit = 0

    for limit, rate in brackets:
        if income > previous_limit:
            taxable_income = min(income, limit) - previous_limit
            tax += taxable_income * rate
            previous_limit = limit
        else:
            break

    return tax
