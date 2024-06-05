def identify_coin(area):
    if abs(area - 64770) < 3000:
        return "50 Cents"
    elif abs(area - 73000) < 4000:
        return "Two Dollars"
    elif abs(area - 49283) < 3000:
        return "20 Cents"
    elif abs(area - 54990) < 3000:
        return "One Dollar"
    elif abs(area - 42420) < 3000:
        return "10 Cents"
    else:
        return "Unknown coin"