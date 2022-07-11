from datetime import datetime, timedelta

import Config
from Helpers import ExcelHelper, XLMapping


class Passport:
    def __init__(self, hamama=None, gamlon=None, gidul="", zan="", sow_date=datetime.today(), out_date=datetime.today(),
                 growing_days=0, passport_num=0, cx="", treys=0, total_plants_order=0, cx_order=0,
                 trey_type=0, remarks=None, avg=0, job_num_of_magash=0):
        self.hamama = hamama
        self.gamlon = gamlon
        self.gidul = gidul
        self.zan = zan
        self.sow_date = sow_date
        self.out_date = out_date
        self.growing_days = growing_days
        self.passport_num = passport_num
        self.cx = cx
        self.treys = treys
        self.total_plants_order = total_plants_order
        self.cx_order = cx_order
        self.trey_type = trey_type
        self.remarks = remarks
        self.avg = avg
        self._passpor_Age = datetime.today() - timedelta(days=self.sow_date.day)
        self.job_num_of_magash = job_num_of_magash

    def set_hamama_and_gamlon(self, sheet):
        # metzay = ExcelHelper.get_excel_sheet_as_table_new(Config.Files.METZAY)
        for row in sheet.iter_rows(min_row=3, values_only=True):
            try:
                if int(row[XLMapping.PASSPORT]) == int(self.passport_num):
                    self.hamama = int(row[XLMapping.HAMAMA])
                    self.gamlon = int(row[XLMapping.GAMLON])
            except Exception:
                continue
