import re
from datetime import datetime, timedelta
import pytz

utcRegex = "\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2]\d|3[0-1])T(?:[0-1]\d|2[0-3]):[0-5]\d:[0-5]\dZ"


def convertUTCDateTime(inputDateTime, timezone="US/Eastern"):
    dest_timezone= pytz.timezone(timezone)

    utc_time = datetime.fromisoformat(inputDateTime)
    dest_time = utc_time.astimezone(dest_timezone)
    dest_time_after24hrs = dest_time + timedelta(hours=24)

    utc_time_string = utc_time.strftime("%Y/%m/%d %H:%M:%S")
    dest_time_string = dest_time.strftime("%Y/%m/%d %H:%M:%S")
    dest_time_after24hrs_string = dest_time_after24hrs.strftime("%Y/%m/%d %H:%M:%S")
    print(f"The current date you entered in UTC is {utc_time_string}.")
    print(f"Input date in US Eastern Timezone: {dest_time_string}.")
    print(f"US Eastern Time after 24 hours will be: {dest_time_after24hrs_string}")



while True:
    utcInput = input("Please enter a valid UTC date (format: YYYY-MM-DDThh:mm:ssZ):")
    if not re.match(utcRegex, utcInput):
        print("Error! Invalid UTC input!")
    else:
        convertUTCDateTime(utcInput)
        break

        

        


