from api import fetch_weather
# import pandas
# import openpyxl
from excel import append_to_excel, append_to_csv
from database import add_record
import time
data = fetch_weather()

append_to_excel(data)
append_to_csv(data)

while True:
    data = fetch_weather()

    append_to_excel(data)
    append_to_csv(data)

    add_record(data)
    time.sleep(10)
    print("Pobrano nowe dane")
#CRON