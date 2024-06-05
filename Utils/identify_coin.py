def identify_coin(area):
    if abs(area - 61504) < 5000:
        return "50 Cents"
    elif abs(area - 71022) < 4000:
        return "Two Dollars"
    elif abs(area - 46870) < 3000:
        return "20 Cents"
    elif abs(area - 52212) < 3000:
        return "One Dollar"
    elif abs(area - 42642) < 3000:
        return "10 Cents"
    else:
        return "Unknown coin"