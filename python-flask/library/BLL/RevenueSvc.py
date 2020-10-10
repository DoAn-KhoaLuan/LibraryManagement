from library.DAL import RevenueRep


def Revenue():
    count = 0
    today_total = 0
    prev_total = 0
    total = 0
    prev_month_total = 0
    month_total = 0
    order_count = RevenueRep.OrderCountToday()
    revenue_today = RevenueRep.RevenueToday()
    percentage_with_prev_day = RevenueRep.PercentageWithPrevDay()
    revenue_total = RevenueRep.TotalRevenue()
    percentage_with_prev_month = RevenueRep.PercentageWithPrevMonth()
    revenue_month = RevenueRep.RevenueCurrentMonth()

    for order_count_today in order_count:
        if order_count_today:
            count += 1
        else:
            count = count

    for today_price in revenue_today:
        if today_price:
            today_total += today_price.total
        else:
            today_total = today_total
    for current_month_price in revenue_month:
        if current_month_price:
            month_total += current_month_price.total
        else:
            month_total = revenue_month

    for prev_price in percentage_with_prev_day:
        if prev_price:
            prev_total += prev_price.total
        else:
            prev_total = prev_total
    for prev_price_month in percentage_with_prev_month:
        if prev_price_month:
            prev_month_total += prev_price_month.total
        else:
            prev_month_total = prev_month_total

    for total_price in revenue_total:
        if total_price:
            total += total_price.total
        else:
            total = total
    percentage = 100 - (prev_total / today_total) * 100
    percentage_month = 100 - (prev_month_total / month_total) * 100
    result_order_count = {
        "labels": "Tổng sô đơn hang trong ngay",
        "order_count": count
    }
    result_today_total = {
        "labels": "Tổng sô doanh thu trong ngay",
        "total_today": today_total,

    }
    result_percentage = {
        "labels": "So với hôm qua",
        "compare_pre_day": round(percentage, 2)
    }
    result_percentage_month = {
        "labels": "So với tháng trước",
        "compare_pre_month": round(percentage_month, 2),

    }
    return result_order_count, result_today_total, result_percentage, result_percentage_month
