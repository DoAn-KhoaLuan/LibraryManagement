class CreateScheduleReq():
    def __init__(self, req):
        self.employee_id = req['employee_id']
        self.date = req['date']
        self.time_from = req['time_from']
        self.time_to = req['time_to']
        self.note = req['note']
        self.actual_hours = req['actual_hours']
        self.expected_hours = req['expected_hours']
        self.salary = req['salary']
        self.delete_at = req['delete_at']


class UpdateScheduleReq():
    def __init__(self, req):
        self.schedule_id = req['schedule_id']
        self.employee_id = req['employee_id']
        self.date = req['date']
        self.time_from = req['time_from']
        self.time_to = req['time_to']
        self.note = req['note']
        self.actual_hours = req['actual_hours']
        self.expected_hours = req['expected_hours']
        self.salary = req['salary']
        self.delete_at = req['delete_at']


class SearchSchedulesReq():
    def __init__(self, req):
        self.keyword = req['keyword'] if 'keyword' in req else None
