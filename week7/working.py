import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s:str)->str:
    if time := re.search(r"^([0-9][0-2]*):* ?([0-5][0-9])* ?([ap]\.?m\.?)? ?to? ?([0-9][0-2]*):* ?([0-5][0-9])* ?([ap]\.?m\.?)?", s.lower(), re.IGNORECASE):
        start_hour=time.group(1)
        start_minute=time.group(2)
        end_hour=time.group(4)
        end_minute=time.group(5)
        if time.group(3) != None:
            if int(start_hour) != 12 and "a" in time.group(3):
                start_hour="0"+start_hour
            elif int(start_hour) == 12 and "a" in time.group(3):
                start_hour="00"
            elif int(start_hour) != 12 and "p" in time.group(3):
                start_hour=int(start_hour)+12
            if start_minute == None:
                start_minute="00"
        if time.group(6) != None:
            if int(end_hour) != 12 and "a" in time.group(6):
                end_hour="0"+end_hour
            elif int(end_hour) ==12 and "a" in time.group(6):
                end_hour="00"
            elif int(end_hour) != 12 and "p" in time.group(6):
                end_hour=int(end_hour)+12
            if end_minute == None:
                end_minute="00"
        if time.group(3) == None and int(start_hour)<10:
            start_hour="0"+start_hour
        if time.group(6) == None and int(end_hour)<10:
            end_hour="0"+end_hour
        return f"{start_hour}{start_minute} to {end_hour}{end_minute}"
    else:
        raise ValueError


def bug_convert(s:str)->str:
    if time := re.search(r"^([0-9][0-2]*):* ?([0-5][0-9])* ?([ap]\.?m\.?)? ?to? ?([0-9][0-2]*):* ?([0-5][0-9])* ?([ap]\.?m\.?)?", s.lower(), re.IGNORECASE):
        start_hour=time.group(1)
        start_minute=time.group(2)
        end_hour=time.group(4)
        end_minute=time.group(5)
        if time.group(3) != None:
            if int(start_hour) != 12 and "a" in time.group(3):
                start_hour="0"+start_hour
            elif int(start_hour) == 12 and "a" in time.group(3):
                start_hour="00"
            elif int(start_hour) != 12 and "p" in time.group(3):
                start_hour=int(start_hour)+12
            if start_minute == None:
                start_minute="00"
        if time.group(6) != None:
            if int(end_hour) != 12 and "a" in time.group(6):
                end_hour="0"+end_hour
            elif int(end_hour) ==12 and "a" in time.group(6):
                end_hour="00"
            elif int(end_hour) != 12 and "p" in time.group(6):
                end_hour=int(end_hour)+12
            if end_minute == None:
                end_minute="00"
        if time.group(3) == None and int(start_hour)<10:
            start_hour="0"+start_hour
        if time.group(6) == None and int(end_hour)<10:
            end_hour="0"+end_hour
        return f"{start_hour}{start_minute} to {end_hour}{end_minute}"
    else:
        return


if __name__ == "__main__":
    main()