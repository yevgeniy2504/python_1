from sys import argv


def check_date(date):
    try:
        day_, month_, year_ = date.split(".")
        if 0 < int(day_) <= 31 and 0 < int(month_) <= 12 and 1800 < int(year_) <= 3000:
            return True
        return False

    except ValueError:
        return False


if __name__ == "__main__":
    print(check_date(argv[1]))


