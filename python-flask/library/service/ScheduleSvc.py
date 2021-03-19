# from library.repository import ScheduleRep, EmployeeRep
#
#
# def GetScheduleByPage(req):
#     hasNext, hasPrev, schedules = ScheduleRep.GetScheduleByPage(req)
#     result = {
#         "hasNext": hasNext,
#         "hasPrev": hasPrev,
#         "schedules": schedules
#     }
#     return result
#
#
# def CreateSchedule(req):
#     create_schedule = ScheduleRep.CreateSchedule(req)
#     return create_schedule
#
# def UpdateSchedule(req):
#     update_schedule = ScheduleRep.UpdateSchedule(req)
#     return update_schedule
#
#
# def SearchSchedules(req):
#     search_schedules = ScheduleRep.SearchSchedules(req)
#     return search_schedules
