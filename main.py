import Config
from ConsoleGreet import Greeter
from rich.console import Console
import sys
from ConsoleGreet.Greeter import loading_bar
from Helpers import ExcelHelper
from playsound import playsound

from Models import WpfGreenHouse

console = Console()


def sub_main():
    excel_jobs = None
    jobs_objects = []

    # Promt Credits
    console.print(Config.VersionSettings.app_promt_details())
    print("\n")
    # Promt Ruler Line
    Greeter.ui_ruler(Config.Styles.BoldRed, Greeter.rev(Config.Heb_Start_Working))
    print("\n")
    console.print(Greeter.rev(Greeter.greet_user()), style=Config.Styles.BlueOnWhite)
    print("\n")
    console.print(Greeter.rev(Config.Heb_Promt_Job_Not_Print_Alert), style=Config.Styles.PurpleOnWhite)
    print("\n")
    console.print(f"[+] {Greeter.rev(Config.Heb_Loading_Data)}", style=Config.Styles.Green)
    # Get Metzay File For Data To Use Once
    metzay = ExcelHelper.get_excel_sheet_as_table_new(Config.Files.METZAY)
    # Get Jobs From Excel File On Desktop As Sheet
    excel_jobs = ExcelHelper.get_excel_sheet_as_table_new(Config.Files.FILE_TO_CREATE)

    # If No File Exist
    if not excel_jobs:
        console.print(Greeter.rev(Config.Heb_No_Xl) + "\n", style=Config.Styles.RedOnWhite)
        console.print(Greeter.rev(Config.Heb_Make_New_Xl) + "\n", style=Config.Styles.WhiteOnBlue)
        ExcelHelper.create_xl_file(Config.Files.FILE_TO_CREATE, A1="job_date", B1="driver", C1="job_cx"
                                   , D1="job_gidul", E1="job_zan", F1="job_plants"
                                   , G1="job_magash", H1="job_passport", I1="job_avg")
        console.print(Greeter.rev(Config.Heb_Ok) + "\n", style=Config.Styles.GreenOnWhite)
        console.print(Greeter.rev(Config.Heb_Print_Instructions), style=Config.Styles.RedOnWhite)
        main()

    # Populate Jobs From Excel Sheet
    jobs_objects = ExcelHelper.populate_jobs_from_xlsheet(excel_jobs)

    # If No Jobs In Excel File
    try:
        if len(jobs_objects) == 0:
            console.print(Greeter.rev(Config.Heb_No_Jobs_Found), style=Config.Styles.RedOnWhite)
            console.print(Greeter.rev(Config.Heb_Print_Instructions), style=Config.Styles.RedOnWhite)
            main()
    except Exception:
        console.print(Greeter.rev(Config.Heb_No_Jobs_Found), style=Config.Styles.RedOnWhite)
        console.print(Greeter.rev(Config.Heb_Print_Instructions), style=Config.Styles.RedOnWhite)
        main()

    # Promt Num Of Jobs For User To Confirm
    console.print(Greeter.rev(Config.Promt_Found_Num_Of_Pass(str(len(jobs_objects)))))

    # For Passports That Hamama && Gamlon are Null
    count = 1
    for job in jobs_objects:
        job.id = count
        if len(job.list_of_passports_objects) > 0:
            for passport in job.list_of_passports_objects:
                if passport.hamama is None:
                    passport.set_hamama_and_gamlon(metzay)
        count += 1

    # Clean Bartender Sheet Before Writing To It
    ExcelHelper.clean_sheet(Config.Files.EXCEL_TO_BARTENDER)
    if Config.user_confirm() == 0:
        # Write To Bartender Sheet For Normal Print
        ExcelHelper.write_jobs_to_bartender_file(Config.Files.EXCEL_TO_BARTENDER, jobs_objects)
    elif Config.user_confirm() == 1:
        # Write To Bartender Sheet For Job Return Page
        ExcelHelper.write_jobs_to_bartender_file(Config.Files.EXCEL_TO_BARTENDER, jobs_objects, True)
    else:
        main()
    # Write Passports To Xl File
    # ExcelHelper.write_jobs_for_bartender_Excel(Config.Files.EXCEL_TO_BARTENDER, jobs_to_print)

    # Progress Bar
    loading_bar(Greeter.rev(Config.Heb_Loading_Data), 0.001)
    # If We Got Here - Promt "You Can Print Now"
    console.print(Greeter.rev(Config.Heb_Job_Finished), style=Config.Styles.BoldWhiteOnBlue)
    # Promt Time
    console.print(Greeter.print_time(), style=Config.Styles.BoldWhiteOnBlue)
    # Play Sound
    playsound('levelup.mp3')
    print("\n")
    # Promt Ruler Line
    Greeter.ui_ruler(Config.Styles.BlueOnWhite, Greeter.rev(Config.Heb_Finish_Working))

    # !! WPF !!
    # Get Metzay For Wpf Data
    wpf_metzay = ExcelHelper.get_excel_sheet_as_table_new_for_wpf(Config.Files.METZAY)

    # Get WpfPassport Obj For Wpd Excel Data
    wpf_passports = ExcelHelper.get_wpf_passports(wpf_metzay)

    # Clean wpf Sheet Before Writing To It
    ExcelHelper.clean_sheet(Config.Files.EXCEL_TO_WPF)

    # Get List Of WpfGreenHouse
    wpf_green_list = WpfGreenHouse.get_list_ofwpfgreen(wpf_passports)

    # Writing Into Excel Sheet
    ExcelHelper.write_jobs_to_wpf_file(Config.Files.EXCEL_TO_WPF, wpf_green_list)
    main()


def main():
    # Promt Credits
    console.print(Config.VersionSettings.app_promt_details())
    print("\n")
    console.print(Greeter.rev(Config.Heb_Promt_Stand_By), style=Config.Styles.Green)
    user_input = input("\n>>>")
    if user_input == "":
        sub_main()
    else:
        console.print(Greeter.rev(Config.Heb_Wrong_Value), style=Config.Styles.RedOnWhite)
        main()


if __name__ == '__main__':
    main()
