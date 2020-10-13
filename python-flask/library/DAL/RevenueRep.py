from datetime import datetime, date, timedelta
from sqlalchemy import or_, func
from dateutil.relativedelta import relativedelta
from library import db
from library.Common.Rsp.SingleRsp import ErrorRsp
from library.Common.util import ConvertModelListToDictList
from library.DAL import models
import pytz
from flask import jsonify, json


def OrderCountToday():
    order_count_today = models.Orders.query.filter(models.Orders.order_id,
                                                   func.DATE(
                                                       models.Orders.order_date) == datetime.now(
                                                       tz=pytz.timezone("Asia/Ho_Chi_Minh")).date()).all()
    return order_count_today


def RevenueToday():
    revenue_today = models.Orders.query.filter(models.Orders.total,
                                               func.DATE(models.Orders.order_date) == datetime.utcnow().date()).all()
    return revenue_today


def RevenueCurrentMonth():
    revenue_month = models.Orders.query.filter(models.Orders.total,
                                               func.MONTH(models.Orders.order_date) == datetime.now(tz=pytz.timezone("Asia/Ho_Chi_Minh")).month).all()
    return revenue_month


def PercentageWithPrevDay():
    percentage = models.Orders.query.filter(models.Orders.total,
                                            func.DATE(models.Orders.order_date) == date.today() - timedelta(
                                                days=1)).all()

    return percentage


def PercentageWithPrevMonth():
    percentage = models.Orders.query.filter(models.Orders.total, func.MONTH(models.Orders.order_date) ==
                                            date.today().month - 1).all()

    return percentage


def TotalRevenue():
    total_revenue = models.Orders.query.filter(models.Orders.total).all()

    return total_revenue
