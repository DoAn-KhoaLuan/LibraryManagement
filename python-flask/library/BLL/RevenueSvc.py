from datetime import date

from library.DAL import RevenueRep
from calendar import monthrange


def Revenue():
    count = 0
    today_total = 0
    prev_total = 0
    total = 0
    prev_month_total = 0
    month_total = 0
    result_every_month = []
    result_every_day = []
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

    # phan tram hom nay so với hom qua
    if prev_total == 0:
        percentage = 100
    else:
        percentage = (today_total / prev_total) * 100

    # phan tram thang này so với tháng trước
    if prev_month_total == 0:
        percentage_month = 100
    else:
        percentage_month = (month_total / prev_month_total) * 100

    # phan tram hom nay tăng hay giam so với hôm qua : âm - giảm, dương - tăng
    if prev_total == 0:
        percentage_compare_with_prev_day = 100
    else:
        percentage_compare_with_prev_day = (today_total / prev_total) * 100 - 100

    # phan tram tháng này tăng hay giảm so với tháng trước: âm - giảm, dương - tăng
    if prev_total == 0:
        percentage_compare_with_prev_month = 100
    else:
        percentage_compare_with_prev_month = (month_total / prev_month_total) * 100 - 100

    # Tổng doanh thu từng tháng
    for month in range(1, 13):
        everymonth_total = 0
        revenue_every_month = RevenueRep.RevenueEveryMonth(month)
        if revenue_every_month:
            for every_month_price in revenue_every_month:
                if every_month_price:
                    everymonth_total += every_month_price.total
                else:
                    everymonth_total = everymonth_total
            result_every_month.append({"tháng": month, "tổng doanh thu": everymonth_total})
        else:
            result_every_month.append({"tháng": month, "tổng doanh thu": 0})

    # Tổng doanh thu từng ngày trong tháng của năm hiện tại
    for month in range(1, 13):
        for day in range(1, monthrange(date.today().year, month)[1]):
            every_day_total = 0
            revenue_every_day = RevenueRep.RevenueEveryDayInMonth(month, day)
            if revenue_every_day:
                for every_day_price in revenue_every_day:
                    if every_day_price:
                        every_day_total += every_day_price.total
                    else:
                        every_day_total = every_day_total
                result_every_day.append({"ngày": day, "tổng doanh thu": every_day_total})
            else:
                result_every_day.append({"Tháng": month, "ngày": day, "tổng doanh thu": 0})

    # kết quả
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
    result_curent_month_total = {
        "labels": "Tổng doanh thu tháng hiện tại",
        "current_month_total": month_total
    }

    result_compare_with_prev_day = {
        "labels": "Tăng hay giảm so với hôm qua",
        "compare_with_prev_day": round(percentage_compare_with_prev_day, 2)
    }

    result_compare_with_prev_month = {
        "labels": "Tăng hay giảm so với tháng trước",
        "compare_with_prev_month": round(percentage_compare_with_prev_month, 2)
    }

    result_everymonth = {
        "labels": "Tổng doanh thu từng tháng",
        "revenue_every_month": result_every_month
    }

    result_everyday = {
        "labels": "Tổng doanh thu từng ngày trong tháng của năm hiện tại",
        "Năm": date.today().year,
        "revenue_every_day": result_every_day
    }

    return result_order_count, result_today_total, result_percentage, result_percentage_month, \
           result_curent_month_total, result_compare_with_prev_month, result_compare_with_prev_day, result_everymonth, result_everyday
