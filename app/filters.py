from datetime import datetime

from app import app


@app.template_filter("timestamp_to_date")
def timestamp_to_date(timestamp):
    date = datetime.fromtimestamp(int(timestamp))
    return date.strftime("%m/%d/%y")


@app.template_filter("timestamp_to_time")
def timestamp_to_time(timestamp):
    date = datetime.fromtimestamp(int(timestamp))
    return date.strftime("%I:%M:%S %p")

