def main():
    time = input("What time is it?: ")
    try:
        if 7.0 <= convert(time) <= 8.0:
            print("Breakfast Time")
        elif 12.0 <= convert(time) <= 13.0:
            print("Lunch Time")
        elif 18.0 <= convert(time) <= 19.0:
            print("Dinner Time")
    except TypeError:
        print("Not a valid time")


def convert(time: str) -> float:
    if ":" in time:
        new: str = letters(time)
        hour, minute = new.split(":")
        hour = float(hour)
        minute=float(minute)  
    elif len(time) == 4:
        hour = float(time[:2])
        minute = float(time[2:])
    elif len(time) == 3:
        hour = float(time[0])
        minute = float(time[1:])
    else:
        return f"Not a valid time"
    fraction: float = float(hour) + float(minute/60)
    return fraction

def letters(user_input: str) -> str:
    clock=user_input.lower()
    if clock.endswith("am"):
        hour, minute = clock.removesuffix("am").rstrip().split(":")
        if hour == "12":
            hour = int(hour)+12
            hour = str(hour)
        time = hour + ":" + minute
        return time
    elif clock.endswith("a.m."):
        hour, minute = clock.removesuffix("a.m.").rstrip().split(":")
        if hour == "12":
            hour = int(hour)+12
            hour = str(hour)
        time = hour + ":" + minute
        return time
    elif clock.endswith("pm"):
        hour, minute = clock.removesuffix("pm").rstrip().split(":")
        hour = int(hour)
        if hour < 12:
            hour = hour + 12
        hour = str(hour)
        time: str = hour + ":" + minute
        return time
    elif clock.endswith("p.m."):
        hour, minute = clock.removesuffix("p.m.").rstrip().split(":")
        hour = int(hour)
        if hour < 12:
            hour = hour + 12
        hour = str(hour)
        time = hour + ":" + minute
        return time
    else:
        return clock
    

if __name__ == "__main__":
    main()