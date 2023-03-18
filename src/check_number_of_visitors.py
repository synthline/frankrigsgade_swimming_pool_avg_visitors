from datetime import datetime

now = datetime.now()

dt_string = str(now.strftime("%d-%m-%Y %H:%M:%S"))
date = dt_string[:10]
time_now = dt_string[11:]