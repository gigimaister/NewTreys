class WpfGreenHouse:
    def __init__(self, Hamama=0, TotalNumOfMagash=0):
        self.Hamama = Hamama
        self.TotalNumOfMagash = TotalNumOfMagash

    @staticmethod
    def get_list_of_green_occupancy(WpfPassports=[], greenNumber=None):
        total_magash = 0
        for i in WpfPassports:
            try:
                if int(i.Ham) == int(greenNumber):
                    total_magash += i.Mag
            except:
                continue

        return WpfGreenHouse(greenNumber, total_magash)


def get_list_ofwpfgreen(wpf_passports):
    list_wpfGreen = []
    Green1 = WpfGreenHouse.get_list_of_green_occupancy(wpf_passports, 1)
    list_wpfGreen.append(Green1)
    Green2 = WpfGreenHouse.get_list_of_green_occupancy(wpf_passports, 2)
    list_wpfGreen.append(Green2)
    Green3 = WpfGreenHouse.get_list_of_green_occupancy(wpf_passports, 3)
    list_wpfGreen.append(Green3)
    Green4 = WpfGreenHouse.get_list_of_green_occupancy(wpf_passports, 4)
    list_wpfGreen.append(Green4)
    Green5 = WpfGreenHouse.get_list_of_green_occupancy(wpf_passports, 5)
    list_wpfGreen.append(Green5)
    Green6 = WpfGreenHouse.get_list_of_green_occupancy(wpf_passports, 6)
    list_wpfGreen.append(Green6)
    Green7 = WpfGreenHouse.get_list_of_green_occupancy(wpf_passports, 7)
    list_wpfGreen.append(Green7)
    return list_wpfGreen
