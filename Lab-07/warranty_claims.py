import math

def parse_claim(text):
    """
    Parses claim string formatted as 'plan:months'.
    Returns a tuple of (plan_title, months_float) or None if invalid.
    """
    if not isinstance(text, str):
        return None
    parts = text.split(':')
    if len(parts) != 2:
        return None
    plan = parts[0].strip()
    months_str = parts[1].strip()
    if not plan:
        return None
    try:
        months = float(months_str)
    except (ValueError, TypeError):
        return None
    if math.isnan(months) or math.isinf(months) or months < 0:
        return None
    return plan.title(), months

def age_average(ages_csv):
    """
    Computes floor average of product ages given as comma-separated values.
    Returns integer average or None if invalid.
    """
    if not isinstance(ages_csv, str) or not ages_csv.strip():
        return None
    parts = ages_csv.split(',')
    values = []
    for r in parts:
        item = r.strip()
        if not item:
            return None
        try:
            val = int(item)
            if val < 0:
                return None
            values.append(val)
        except (ValueError, TypeError):
            return None
    if not values:
        return None
    return sum(values) // len(values)

def payable_charge(text):
    """
    Computes payable repair charge with 18% tax minus discount given 'charge|discount'.
    Returns non-negative total charge or None if invalid.
    """
    if not isinstance(text, str):
        return None
    parts = text.split('|')
    if len(parts) != 2:
        return None
    try:
        charge = float(parts[0].strip())
        discount = float(parts[1].strip())
    except (ValueError, TypeError):
        return None
    if math.isnan(charge) or math.isinf(charge) or math.isnan(discount) or math.isinf(discount):
        return None
    if charge < 0 or discount < 0:
        return None
    total = charge * 1.18 - discount
    return max(round(total, 2), 0.0)

def main():
    print("==== Running parse_claim ====")
    user_input = input("Enter plan:age in months (e.g. standard:30): ")
    result = parse_claim(user_input)
    print("Plan and Age:", result)

    print("\n==== Running age_average ====")
    user_input = input("Enter product ages as CSV (e.g. 12,24,36): ")
    result = age_average(user_input)
    print("Average Age:", result)

    print("\n==== Running payable_charge ====")
    user_input = input("Enter charge|discount (e.g. 1500|200): ")
    result = payable_charge(user_input)
    print("Payable Charge:", result)

if __name__ == "__main__":
    main()
