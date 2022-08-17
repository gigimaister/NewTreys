from rich.table import Table
import Config
import ConsoleGreet.Greeter


class VersionSettings:
    @staticmethod
    def app_promt_details():
        table = Table(title=ConsoleGreet.Greeter.rev("הדפסת מדבקות אוטומטית"), style=Config.Styles.Green)
        table.add_column("Created By", style="cyan", no_wrap=True)
        table.add_column("Version", style="magenta")
        table.add_row(CREATED_BY, APP_VERSION)

        return table


# Files
class Files:
    TEST_XLS = "J:\\קובי\\קובי\\TEST\\test1.xlsx"
    FILE_TO_CREATE = "C:\\Users\\hamama2\\Desktop\\העתקת עבודות מטבלת הוצאות.xlsx"
    EXCEL_TO_BARTENDER = "J:\\קובי\\קובי\\DONOTTOUCH\\JOBSFORBARTENDER.xlsx"
    METZAY = "J:\\מצאי חממות חדש\\מצאי חממות חדש.xlsx"
    EXCEL_TO_WPF = "J:\\קובי\\קובי\\DONOTTOUCH\\DONOTTOUCHWPF.xlsx"


# Styles
class Styles:
    WhiteOnBlue = "white on blue"
    BoldWhiteOnBlue = "bold white on blue"
    Blue = "blue"
    Green = "green"
    GreenOnWhite = "green on white"
    BoldRed = "bold red"
    RedOnWhite = "bold red on white"
    PurpleOnWhite = "bold purple on white"
    BlueOnWhite = "bold blue on white"


# App Settings
CREATED_BY = "Kobi Gigi"
APP_VERSION = "3.0"

# Hebrew Strings
Heb_Searching = "מחפש"
Heb_No_Xl = "לא נמצא קובץ אקסל!"
Heb_Make_New_Xl = "מייצר קובץ אקסל בשולחן העבודה"
Heb_Are_U_Sure = "האם להמשיך?"
Heb_Start_Working = "התחלת עבודה"
Heb_Finish_Working = "סיום עבודה"
Heb_Loading_Data = "טוען נתונים..."
Heb_Ok = "אחלה סיימתי...אפשר להמשיך ):"
Heb_Reading_Data = "קורא נתונים..."
Heb_Confirm_Choice = "להדפסה נא ללחוץ על אינטר."
Heb_Promt_Job_Not_Print_Alert = "שימו לב! עבודות ללא תאריך, לקוח או כמות מגשים לא יודפסו!"
Heb_No_Jobs_Found = "לא נמצאו עבודות."
Heb_Print_Instructions = " נא להדביק עבודות בקובץ אקסל, לשמור ולהפעיל את התוכנה שוב."
Heb_Promt_Stand_By = "לתחילת עבודה, נא ללחוץ על אינטר."
Heb_Wrong_Value = "ערך לא נכון הוכנס!"
Heb_Job_Finished = "פעולה הסתיימה בהצלחה. ניתן להדפיס מדבקות בקובץ ברטנדר"
Heb_magash = "מגש"

# Small Cage Cx
Meshek_Habibyan = "חביביאן"
Mapan = "ים שיווק"
Israel_Mapan = "מפן"
Eran_Porat = "ערן פורת"


def Promt_Found_Num_Of_Pass(string):
    return f" מצאתי {string[::-1]} עבודות. \n "


def user_confirm():
    user_input = input(f"{ConsoleGreet.Greeter.rev(Heb_Confirm_Choice)}\n>>>")
    if user_input == "":
        return 0
    elif user_input == "1":
        return 1
    else:
        return 2
