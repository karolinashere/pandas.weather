from api import fetch_weather
# import pandas
# import openpyxl
from excel import append_to_excel
data = fetch_weather()

append_to_excel(data)