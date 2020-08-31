
import datetime

from utils.utility import get_rand, timestamp_gen, tounixdt
from config import START_TIME

class Generator:
    """
    This is Generator Class, used to handle
    all data generation operation.
    """
    def __init__(self):
        self.start_dtime =  datetime.datetime.strptime(START_TIME, '%Y-%m-%d %H:%M:%S')
        self.timestamp_itr = None

    def _heart_rate(self):
        return get_rand(30, 100)

    def _respiration_rate(self):
        return get_rand(30, 100)

    def _activity(self):
        return get_rand(1, 20)

    def _timestamp(self):
        if not self.timestamp_itr:
            self.timestamp_itr = timestamp_gen(self.start_dtime)
        return self.timestamp_itr

    def _timestamp_nxt(self):
        try:
            return tounixdt(next(self._timestamp()))
        except StopIteration as e:
            return None

    def current_generator_data(self):
        censor_data = dict()
        censor_data['user_id'] = 'abc'
        censor_data['timestamp'] = str(self._timestamp_nxt())
        censor_data['heart_rate'] = self._heart_rate()
        censor_data['respiration_rate'] = self._respiration_rate()
        censor_data['activity'] = self._activity()
        return censor_data

if '__name__' == '__main__':
    obj = Generator()
    for i in range(10):
        print(obj.current_generator_data())
