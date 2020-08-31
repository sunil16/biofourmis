import multiprocessing

class DataPipe(object):
    """
    This is DataPipe(Queue) Class, used to handle
    all queue related funtion. Simulator push data
    one by one and process funtion will pop data
    one by one from queue without lost any data.
    """
    def __init__(self):
        self.data_queue = multiprocessing.Queue()

    def enqueue(self, data = None):
        self.data_queue.put(data)

    def dequeue(self):
        return self.data_queue.get()

    def size(self):
        return self.data_queue.qsize()

    def isempty(self):
        return self.data_queue.empty()

if '__name__' == '__main__':
    print(DataPipe().size())
