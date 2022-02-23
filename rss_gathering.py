import rss_gathering_helper as rss
from datetime import timedelta

# starts_at = input("Time RSS Gathering starts: ").lower().replace(" ", "")
# temp = input("Starts the next day? (t or f): ").lower().replace(" ", "")
# biome = int(input("Biome?: "))

starts_at = "2pm"
temp = "f"
biome = 1

raw_time = rss.get_raw_time(starts_at)  # e.g 2 for 2am; 14 for 2pm, etc

rss_gathering_date = rss.starts_date(rss.get_starts_tomorrow(temp), raw_time) # get the date and time rss gathering starts
rss_gathering_date_str = rss_gathering_date.strftime("%a %I:%M %p")
print(f"Resource Gathering starts: {rss_gathering_date_str}")

starts_in = rss_gathering_date - rss.get_raw_current_time() # time left for rss gathering to start
print(f"Resource gathering starts in: {rss.format_timedelta(starts_in)}")

location = rss.get_biome_location(biome) # get biome to check for times

lines = rss.get_lines(location)  # get drag stats into a string

times = []
result, times = rss.get_send_times(lines, rss_gathering_date)
print(result)



times.sort()

for time in times:
    # time_str = time.strftime("%a %I:%M %p")
    # print(time_str)
    # print(time)
    pass

