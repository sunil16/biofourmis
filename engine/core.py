import time
import multiprocessing
from multiprocessing import Process

from .generator import Generator
from datapipe.data_pipe import DataPipe
from datastore.pandas_core import DataStore
from utils.constants import PROCESS_REPORT_COLUMN
from .p_utils import prepare_data, prepare_report
from config import INTERVAL_M

class Engine(object):
    """
    This is Engine Class, used to handle
    all concurrent processes, Simulator,
    Processs function, Report Generation function, pandas_core.
    """
    def __init__(self):
        print("Engine started...")

    def _start_simulator(self, q_obj = None, gen_obj = None):
        print("Simulator Started...")
        while True:
            q_obj.enqueue(gen_obj.current_generator_data())
            time.sleep(1)

    def _start_processing(self, q_obj = None, pq_obj = None):
        print("Processing Engine Started...")
        data, secound, minute = (PROCESS_REPORT_COLUMN, 0, 1*int(INTERVAL_M))
        while True:
            if minute == secound:
                pq_obj.enqueue(DataStore.save(data))
                secound, data = (0, PROCESS_REPORT_COLUMN)
            prepare_data(data, q_obj.dequeue())
            time.sleep(1)
            secound += 1

    def _start_reportengine(self, pq_obj = None):
        print("Report Engine Started...")
        while True:
            if pq_obj.size():
                prepare_report(pq_obj.dequeue())

    def start(self):
        gen_obj, q_obj, pq_obj = (Generator(), DataPipe(), DataPipe())
        Process(target=self._start_simulator, args = (q_obj, gen_obj)).start()
        Process(target=self._start_processing, args = (q_obj, pq_obj)).start()
        Process(target=self._start_reportengine, args = (pq_obj,)).start()

if __name__ == '__main__':
    Engine().start()
