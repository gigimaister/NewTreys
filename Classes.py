# import datetime
# from dataclasses import dataclass
#
#
# @dataclass
# class Passport:
#     hamama: int
#     gamlon: int
#     gidul: str
#     zan: str
#     sow_date: datetime.datetime
#     out_date: datetime.datetime
#     growing_days: int
#     passpor_age: int
#     passport_num: int
#     cx: str
#     treys: int
#     total_plants_order: int
#     cx_plants_order: int
#     trey_type: int
#     remarks: str
#
#
# @dataclass
# class Job:
#     job_date: int
#     driver: int
#     job_cx: str
#     job_gidul: str
#     job_zan: datetime.datetime
#     job_plants: datetime.datetime
#     job_magash: int
#     job_passport: str
#     job_avg: int
#     job_passports_dict: {}
#
#     def __init__(self):
#         """
#         Split String Of More Than One Passport From Job
#         && Return Dict In The Format Of '{72345:15, 72457:89, ...}'
#         """
#         # Split To Format Of '72345-15, 72457-89, ...'
#         self.split_list_of_passport = self.job_passport.replace(",", " ").split(" ")
#         # Split To The Format Of '{72345:15, 72457:89, ...}'
#         for pair in self.split_list_of_passport:
#             self.job_passports_dict[pair.split("-")[0]] = pair.split("-")[1]
#
#     def num_of_passports(self):
#         """
#         Set The Num Of Passports With Their Magash Amount
#         """
#         pass
