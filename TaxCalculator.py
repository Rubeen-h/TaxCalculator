def calculate_irpf(people):
    brackets = [
        (12450, 0.19),
        (20200, 0.24),
        (35200, 0.30),
        (60000, 0.37),
        (float('inf'), 0.45)
    ]

    age_discounts = {range(16, 31): 0.85, range(60, 150): 0.95}
    disability_discounts = {
        range(33, 66): 0.90,  
        range(66, 101): 0.85   
    }

    results = []

    for name, income, age, disability_percentage, children_count in people:
        tax = 0
        previous_limit = 0

        for limit, rate in brackets:
            if income > previous_limit:
                taxable_income = min(income, limit) - previous_limit
                tax += taxable_income * rate
                previous_limit = limit
            else:
                break

        for age_range, discount in age_discounts.items():
            if age in age_range:
                tax *= discount
                break

        for disability_range, discount in disability_discounts.items():
            if disability_percentage in disability_range:
                tax *= discount
                break

        children_discount = min(children_count * 0.10, 1.0)
        tax *= (1 - children_discount)

        tax = max(tax, 0) 

        results.append((name, tax))

    return results


# Example Test Input
dataset = [
    ("Alice", 50000, 25, 40, 2),  # 15% age discount, 10% disability discount, 2 children (20% total discount)
    ("Bob", 30000, 45, 70, 1),    # No age discount, 15% disability discount, 1 child (10% total discount)
    ("Charlie", 70000, 62, 60, 0),  # 5% age discount, 10% disability discount, no children discount
    ("Diana", 12000, 28, 50, 3)   # 15% age discount, 10% disability discount, 3 children (30% total discount)
]


result = calculate_irpf(dataset)
print(result)
