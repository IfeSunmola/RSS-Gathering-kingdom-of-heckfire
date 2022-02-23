import rss_gathering_helper as rss

# starts_at = input("Time RSS Gathering starts: ").lower().replace(" ", "")
# starts_tomorrow = input("Starts the next day? (t or f): ").lower().replace(" ", "")
# biome = int(input("Biome?: ")) # 1 for grass, # 2 for badlands, 3 for swamp

# uncomment the code above and comment the code below to get the input at run time
starts_at = "2pm"
starts_tomorrow = "f"
biome = 1

raw_time = rss.get_raw_time(starts_at)  # e.g 2 for 2am; 14 for 2pm, etc

rss_gathering_date = rss.starts_date(rss.get_starts_tomorrow(starts_tomorrow), raw_time)  # get the date and time rss gathering starts
rss_gathering_date_str = rss_gathering_date.strftime("%a %I:%M %p")
print(f"Resource Gathering starts: {rss_gathering_date_str}")

starts_in = rss_gathering_date - rss.get_raw_current_time()  # time left for rss gathering to start
print(f"Resource gathering starts in: {rss.format_timedelta(starts_in)}")

location = rss.get_biome_location(biome)  # get biome to check for times

lines = rss.get_lines(location)  # get drag stats into a string

times = []  # not using this yet
result, times = rss.get_send_times(lines, rss_gathering_date)
print(result)
