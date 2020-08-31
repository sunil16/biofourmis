

from engine.core import Engine
from utils.utility import cal_hourly_report, report_by_localdt

def run():
    """
    This method start Engine
    including simulator, process, report generator.
    """
    Engine().start()

def get_hourly_report():
    """
    This method generate report for an hour by 15 mins dataframe.
    """
    cal_hourly_report()

def get_localdt_report(start_t = None, end_t = None):
    """
    This method generate report for an hour by 15 mins dataframe with local(IST) time filter.
    """
    report_by_localdt(start_t, end_t)

if __name__ == '__main__':
    get_hourly_report()
    get_localdt_report('31-08-2020-15:00', '31-08-2020-16:00')
