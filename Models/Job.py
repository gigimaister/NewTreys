import datetime
from math import ceil
import Config
from Helpers import ExcelHelper, XLMapping
from Models.Passport import Passport

BIG_MAGASH_IN_CAGE = 33
SMALL_MAGASH_IN_CAGE = 44
BIG_MAGASH_SMALL_CAGE = 15
SMALL_MAGASH_SMALL_CAGE = 20


class MainJob:
    @property
    def metzay(self):
        return ExcelHelper.get_excel_sheet_as_table_new(Config.Files.METZAY)

    def __init__(self, job_date=datetime.datetime, driver="", job_cx="", job_gidul="", job_zan="", job_plants=0,
                 job_magash=0, job_passport="", job_avg=0):
        self.list_of_passports_objects = []
        self.job_date = job_date
        self.driver = driver
        self.job_cx = job_cx
        self.job_gidul = job_gidul
        self.job_zan = job_zan
        self.job_plants = job_plants
        self.job_magash = job_magash
        self.job_passport = job_passport
        self.job_avg = job_avg
        self.num_of_bartender_stickers = 0
        self.is_page2 = False
        self.is_page3 = False
        self.is_small_cage = False
        self.is_job_need_to_return = False
        self.id = 0

        # Replace If Input Was Like "73125=5"
        # self.split_list_of_passport = str(self.job_passport).replace("=", "-")
        # print(f"after = replace = : { self.split_list_of_passport}")
        # Split To Format Of '72345-15, 72457-89, ...'
        self.split_list_of_passport = str(self.job_passport).replace(",", " ").split(" ")
        # Split To The Format Of '{72345:15, 72457:89, ...}'
        for pair in self.split_list_of_passport:
            try:
                self.list_of_passports_objects.append(Passport(passport_num=pair.split("-")[0]
                                                               , job_num_of_magash=pair.split("-")[1]
                                                               ))
            except IndexError:
                self.list_of_passports_objects.append(Passport(passport_num=pair.split("-")[0]
                                                               , job_num_of_magash=self.job_magash
                                                               ))

        # Matched Metzay To Passports
        self.get_passports_to_job()
        # If Small Cage
        self._is_small_cage()
        # Num Of Bartender Sticker To Print
        self.get_num_of_stickers_to_print()
        # Set If We Have More Than One Passports Page(4-9 Passports)
        if len(self.list_of_passports_objects) > 3 < 7:
            self.is_page2 = True
        if len(self.list_of_passports_objects) > 6:
            self.is_page3 = True

    def get_passports_to_job(self):
        """
        For Each Job Passport Find Passport Obj From The Metzay
        """
        try:
            # metzay = ExcelHelper.get_excel_sheet_as_table_new(Config.Files.METZAY)
            for passport in self.list_of_passports_objects:
                for row in self.metzay.iter_rows(min_row=3, values_only=True):
                    if int(row[XLMapping.PASSPORT]) == int(passport.passport_num):
                        passport.hamama = int(row[XLMapping.HAMAMA])
                        passport.gamlon = int(row[XLMapping.GAMLON])
                        passport.gidul = str(row[XLMapping.GIDUL])
                        passport.zan = str(row[XLMapping.ZAN])
                        passport.sow_date = datetime.datetime.strptime(str(row[XLMapping.SOW_DATE]),
                                                                       "%Y-%m-%d %H:%M:%S")
                        passport.out_date = datetime.datetime.strptime(str(row[XLMapping.OUT_DATE]),
                                                                       "%Y-%m-%d %H:%M:%S")
                        passport.growing_days = int(row[XLMapping.GROW_DAYS])
                        passport.treys = int(row[XLMapping.TREYS])
                        passport.total_plants_order = int(row[XLMapping.ORIGINAL_AMOUNT_PLANTS] * 1_000)
                        passport.trey_type = int(row[XLMapping.TREY_TYPE])
                        passport.remarks = str(row[XLMapping.REMARKS])
                        passport.avg = int(row[XLMapping.AVG])
                        break
        except Exception:
            pass

    def get_num_of_stickers_to_print(self):
        """
        Set Num Of Stickers To Max Of 48
        """
        max_stick = 40
        max_stick_for_return = 15
        try:
            if self.is_job_need_to_return:
                self.num_of_bartender_stickers = min(max(round(self.job_magash / BIG_MAGASH_IN_CAGE * 3 + 1), 5),
                                                     max_stick_for_return)
                return

            elif self._get_sticker():
                self.num_of_bartender_stickers = min(max(round(self.job_magash/BIG_MAGASH_IN_CAGE*3+1), 5), max_stick)

            elif self._get_sticker() is None:
                self.num_of_bartender_stickers = min(max(ceil(self.job_magash / BIG_MAGASH_SMALL_CAGE) * 3 + 1, 5),
                                                     max_stick)
            else:
                self.num_of_bartender_stickers = min(max(round(self.job_magash/SMALL_MAGASH_IN_CAGE*3 + 1), 5),
                                                     max_stick)
        except Exception:
            pass

    def _get_sticker(self):
        passport = self.list_of_passports_objects[0]
        try:
            if int(passport.trey_type) == 442 or int(passport.trey_type) == 187:
                return True
            elif int(passport.trey_type) == 308 or int(passport.trey_type) ==180 or int(passport.trey_type) == 250:
                return False
            elif self.is_small_cage:
                return None
            else:
                return True
        except Exception:
            return True

    def _is_small_cage(self):
        try:
            if Config.Mapan in self.job_cx or Config.Meshek_Habibyan in self.job_cx or Config.Israel_Mapan in self.job_cx \
                    or Config.Eran_Porat in self.job_cx:
                self.is_small_cage = True
        except Exception:
            return False



