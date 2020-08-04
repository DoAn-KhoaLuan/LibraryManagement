from library.app import db

class Schedules(db.Model):
    schedule_id
    employee_id
    date
    time_from
    time_to
    actual_hours
    expected_hours
    salary
