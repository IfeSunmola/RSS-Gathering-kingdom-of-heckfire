import datetime as dt
from datetime import datetime

raw_current_time = datetime.now()
str_current_time = raw_current_time.strftime("%a %X")


def get_raw_time(starts_at):
    raw_time = ""  # e.g 2 for 2am, 13 for 1pm
    index = 0
    while index < len(starts_at):
        if starts_at[index].isdigit():
            raw_time += starts_at[index]
        else:
            break
        index += 1

    if starts_at == "12am":
        raw_time = "00"
    if "pm" in starts_at:
        if int(raw_time) < 12:
            raw_time = int(raw_time)
            raw_time += 12
            raw_time = str(raw_time)
    return raw_time


def get_starts_tomorrow(temp):
    if temp == "t":
        starts_tomorrow = True
    elif temp == "f":
        starts_tomorrow = False
    else:
        starts_tomorrow = None
    return starts_tomorrow


def format_timedelta(time_):
    time_ = str(time_)
    new_time = ""
    index_ = 0
    while index_ < len(time_):
        if time_[index_] != ".":
            new_time += time_[index_]
        else:
            break
        index_ += 1
    return new_time


def starts_date(starts_tomorrow, time):
    if starts_tomorrow:
        rss_gathering_date = dt.datetime(raw_current_time.year, raw_current_time.month, raw_current_time.day + 1,
                                         hour=int(time))
    elif not starts_tomorrow:
        rss_gathering_date = dt.datetime(raw_current_time.year, raw_current_time.month, raw_current_time.day,
                                         hour=int(time))
    else:
        rss_gathering_date = None

    return rss_gathering_date


def get_raw_current_time():
    return raw_current_time


def get_biome_location(biome):
    if biome == 1:
        location = "rss_gathering/grass.txt"
    elif biome == 2:
        location = "rss_gathering/badlands.txt"
    elif biome == 3:
        location = "rss_gathering/swamp.txt"
    else:
        location = None
    return location


def get_lines(location):
    with open(location) as f:
        lines = f.readlines()
    return lines


def get_send_times(lines, rss_gathering_date):
    result = ""
    times = []
    for line in lines:
        if line.startswith("="):
            result += f"\n{line}"
        else:
            spliter = line.split(" = ")
            # get node type and drag names
            details = spliter[0]  # contains format: food_migo_nos
            details = details.split("_", 1)  # contains list format: "food", "migo_nos"
            node_name = details[0]
            drags_to_send = details[1]

            # get gathering time
            details = spliter[1]  # contains gathering time format: 4 8 OR 4 38
            details = details.split()  # contains list format "4" "8" OR "4" "38"
            hours = int(details[0])
            minutes = int(details[1])

            send_time = rss_gathering_date - dt.timedelta(hours=hours, minutes=minutes)
            times.append(send_time)
            send_time = send_time.strftime("%a %I:%M %p")
            result += f"Send {drags_to_send} to {node_name} at: {send_time}\n"
    return result, times
