import os
import csv
import random
import pytz
import datetime
from datetime import timezone
from pathlib import Path
import pandas as pd

from .constants import REPORT_COLUMN

def get_rand(min_range=0, max_range=0):
    """
    This function used to generate random data.
    """
    return random.randint(min_range, max_range)

def timestamp_gen(start_dtime = None):
    """
    This function used to Generate timestamp.
    """
    if start_dtime is not None:
        utc_timestamp = start_dtime
        while True:
            yield utc_timestamp
            utc_timestamp = utc_timestamp + datetime.timedelta(0,1)
    else:
        raise Exception("unsupported time and date")

def tounixdt(inpt_datetime = None):
    """
    This function used to handle unix datetime.
    """
    return int(inpt_datetime.replace(tzinfo=timezone.utc).timestamp())

def update_json(data = None, r_hour = None, path = None):
    if data is not None and r_hour is not None:
        filename_path = os.path.join(path,'.'.join((str(r_hour),'json')))
        with open(filename_path, 'a') as jfile:
            jfile.write(data.to_json(orient="records"))
        print("Json successfully updated path: {}".format(filename_path))

def save_report(reportname = None, data = None, r_hour = None, c_df = None):
    """
    This function used to save reports.
    """
    if reportname is not None and data is not None:
        today = datetime.datetime.now()
        path = os.path.join('reports',today.strftime('%Y%m%d'), str(r_hour))
        if not os.path.isdir(path):
            Path(path).mkdir(parents=True, exist_ok=True)
        filename_path = os.path.join(path,reportname)
        with open(filename_path, 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)

            # writing the fields
            csvwriter.writerow(REPORT_COLUMN)

            # writing the data rows
            csvwriter.writerows([data])
        print("Report successfully generated path: {}".format(filename_path))
        update_json(c_df, r_hour, path)

def r_hourly(path = None, s_path = None):
    if path is not None:
        data, min_hr, avg_hr, max_hr = (list(), list(), list(), list())
        for file in os.listdir(path):
            if file.endswith(".csv"):
                csv_file = os.path.join(path, file)
                df = pd.read_csv(csv_file)
                if df.get('avg_hr').size:
                    avg_hr.append( df.get('avg_hr').iat[0] )
                if df.get('min_hr').size:
                    min_hr.append( df.get('min_hr').iat[0] )
                if df.get('max_hr').size:
                    max_hr.append( df.get('max_hr').iat[0] )

        data.append(int(sum(avg_hr)/len(avg_hr)))
        data.append(min(min_hr))
        data.append(max(max_hr))
        filename_path = os.path.join('hourlyreports', ".".join((s_path,'csv')))
        with open(filename_path, 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)

            # writing the fields
            csvwriter.writerow(['avg_hr','min_hr', 'max_hr'])

            # writing the data rows
            csvwriter.writerows([data])
        print("Report successfully generated path: {}".format(filename_path))


def cal_hourly_report():
    report_path = 'reports'
    for d in os.listdir(report_path):
        s_rpath = os.path.join(report_path,d)
        for sdir in os.listdir(s_rpath):
            sb_rpath = os.path.join(s_rpath, sdir)
            r_hourly(sb_rpath, sdir)

def report_by_localdt(start_t = None, end_t = None):
    start_t = datetime.datetime.strptime(start_t, '%d-%m-%Y-%H:%M')
    end_t = datetime.datetime.strptime(end_t, '%d-%m-%Y-%H:%M')
    local = pytz.timezone ("Asia/Kolkata")
    local_dt = local.localize(start_t, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)
    hour = str(utc_dt.hour)
    year = str(utc_dt.year)
    month = str(utc_dt.month)
    month = ('0' + month ) if len(month) == 1 else month
    day = str(utc_dt.day)
    day = ('0' + day ) if len(day) == 1 else day
    dir_name =  year + month + day
    sb_rpath = os.path.join('reports',dir_name,hour)
    if os.path.exists(sb_rpath):
        r_hourly(sb_rpath, hour)
    else:
        print("Data not for this query.")
