
def calculate_savings_plan(budget, extra_config):
    saving_rate = extra_config.get("saving_rate", 0.2)
    months = extra_config.get("months", 6)
    monthly_saving = budget * saving_rate
    total_saved = monthly_saving * months
    return {"monthly_saving": monthly_saving, "total_saved": total_saved, "months": months}

def calculate_investment_plan(budget, extra_config):
    monthly_contribution = extra_config.get("monthly_contribution", budget * 0.2)
    months = extra_config.get("months", 12)
    monthly_return = extra_config.get("monthly_return", 0.0)
    
    total = 0
    for _ in range(months):
        total = (total + monthly_contribution) * (1 + monthly_return)
    
    return {"monthly_contribution": monthly_contribution, "total_value": round(total, 2), "months": months}

def calculate_hybrid_plan(budget, extra_config):
    saving_rate = extra_config.get("saving_rate", 0.2)
    debt_rate = extra_config.get("debt_rate", 0.1)
    months = extra_config.get("months", 12)
    
    monthly_saving = budget * saving_rate
    monthly_debt = budget * debt_rate
    return {
        "monthly_saving": monthly_saving,
        "monthly_debt": monthly_debt,
        "total_saving": monthly_saving * months,
        "total_debt": monthly_debt * months,
        "months": months
    }