from datetime import datetime, date, timedelta
from sqlalchemy import or_, func
from dateutil.relativedelta import relativedelta
from library import db
from library.Common.Rsp.SingleRsp import ErrorRsp
from library.Common.util import ConvertModelListToDictList
from library.DAL import models
from calendar import monthrange
from flask import jsonify, json


def GetOrdersToday():
    orders = models.Orders.query.filter(models.Orders.order_id,
                                                   func.DATE(
                                                       models.Orders.order_date) == datetime.utcnow().date()).all()
    return orders

def GetOrdersPrevDay():
    prev_day_orders = models.Orders.query.filter(func.DATE(models.Orders.order_date) == date.today() - timedelta(days=1)).all()
    return prev_day_orders

def GetOrdersInMonth():
    month_orders = models.Orders.query.filter(func.MONTH(models.Orders.order_date) == datetime.utcnow().month()).all()
    return month_orders

def GetOrdersInPrevMonth():
    prev_month_orders = models.Orders.query.filter(func.MONTH(models.Orders.order_date) == date.today().month() - timedelta(months=1)).all()
    return prev_month_orders

def GetTotalRevenueToday():
    today_orders = models.Orders.query.filter(func.DATE(models.Orders.order_date) == datetime.utcnow().date()).all()
    total_revenue = 0
    for order in today_orders:
        total_revenue += order.total
    return total_revenue

def GetTotalRevenuePrevDay():
    today_prev_orders = models.Orders.query.filter(func.DATE(models.Orders.order_date) == date.today() - timedelta(days=1)).all()
    total_prev_revenue = 0
    for order in today_prev_orders:
        total_prev_revenue += order.total
    return total_prev_revenue

def RevenueCurrentMonth():
    revenue_month = models.Orders.query.filter(models.Orders.total,
                                               func.MONTH(models.Orders.order_date) == datetime.utcnow().month).all()
    return revenue_month




def PercentageWithPrevMonth():
    percentage = models.Orders.query.filter(models.Orders.total, func.MONTH(models.Orders.order_date) == date.today().month - 1).all()

    return percentage


def TotalRevenue():
    total_revenue = models.Orders.query.filter(models.Orders.total).all()

    return total_revenue


def RevenueEveryMonth(month):
    revenue_everymonth = models.Orders.query.filter(models.Orders.total,
                                                    func.MONTH(models.Orders.order_date) == month,
                                                    func.YEAR(models.Orders.order_date) == date.today().year).all()

    return revenue_everymonth


def RevenueEveryDayInMonth(month, _date):
    revenue_everyday = models.Orders.query.filter(models.Orders.total,
                                                  func.DAY(models.Orders.order_date) == _date,
                                                  func.MONTH(models.Orders.order_date) == month,
                                                  func.YEAR(models.Orders.order_date) == date.today().year).all()

    return revenue_everyday

