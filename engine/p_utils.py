from utils.utility import save_report
from datetime import datetime

def prepare_data(data = None, current_data = None):
    """
    This function used to prepare data for pandas dataframe.
    """
    if data is not None and current_data is not None:
        if 'activity' in data:
            act = data.get('activity')
            act.append(current_data.get('activity'))
            data['activity'] = act

        if 'respiration_rate' in data:
            rep = data.get('respiration_rate')
            rep.append(current_data.get('respiration_rate'))
            data['respiration_rate'] = rep

        if 'timestamp' in data:
            tt = data.get('timestamp')
            tt.append(current_data.get('timestamp'))
            data['timestamp'] = tt

        if 'user_id' in data:
            data['user_id'] = current_data.get('user_id')

        if 'heart_rate' in data:
            hr = data.get('heart_rate')
            hr.append(current_data.get('heart_rate'))
            data['heart_rate'] = hr

def prepare_report(c_df = None):
    """
    This function used to prepare data for CSV file.
    """
    if c_df is not None:
        report_data = list()
        filename = ''
        if 'user_id' in c_df.columns and c_df.user_id.size:
            report_data.append(c_df.user_id.iat[0])
        if 'timestamp' in c_df.columns and c_df.timestamp.size:
            start_t = c_df.timestamp.iat[0]
            end_t = c_df.timestamp.iat[-1]
            report_data.append(start_t)
            report_data.append(end_t)
            r_hour = datetime.utcfromtimestamp(float(start_t)).time().hour
            r_minute = datetime.utcfromtimestamp(float(end_t)).time().minute
            filename = '.'.join(('_'.join((str(r_hour), str(r_minute))),'csv'))
        if 'heart_rate' in c_df.columns:
            report_data.append(int(c_df.get('heart_rate').mean()))
            report_data.append(int(c_df.get('heart_rate').min()))
            report_data.append(int(c_df.get('heart_rate').max()))
        if 'respiration_rate' in c_df.columns:
            report_data.append(int(c_df.get('respiration_rate').mean()))
        save_report(filename, report_data, r_hour, c_df)
