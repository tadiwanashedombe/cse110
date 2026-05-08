with open("python/web_traffic.csv") as web_file:
    total_time = 0
    for line in web_file:

        parts = line.split(",")

        page = parts[0].strip()
        time = float(parts[1].strip())
        referring_page = parts[2].strip()

        total_time += time

        print(f"Page '{page}' referred by '{referring_page}' was visited for {time} seconds")

        print(f"The total time was {total_time}")