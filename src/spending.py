def get_total(costs: dict, items: list, tax: float) -> float:
    total = 0.0

    for item in items:
        if item in costs:
            total += costs[item]

    total += total * tax
    return round(total, 2)
