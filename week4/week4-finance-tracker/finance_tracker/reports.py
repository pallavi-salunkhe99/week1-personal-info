from finance_tracker.utils import get_month_from_date

def monthly_report(expenses, month):
    total=0
    for e in expenses:
        if e.date.startswith(month):
            total += e.amount
    return total

def category_breakdown(expenses):
    data = {}
    for e in expenses:
        data[e.category] = data.get(e.category, 0) + e.amount
        return data

def statistics(expenses):
    
    if not expenses:
        return {"max": 0, "min": 0, "avg": 0}
    
    amounts = [e.amount for e in expenses]
    return {
        "max" : max(amounts),
        "min" : min(amounts),
        "avg" : sum(amounts) / len(amounts)

    }