import time

class MyProfiler:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.time_delta = None

    def _get_current_time(self):
        return time.time()

    def __enter__(self):
        self.start_time = self._get_current_time()
        print(f"START {self.start_time}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = self._get_current_time()
        print(f"END {self.end_time}")
        self.time_delta = self.end_time - self.start_time
        print(f"TIME SPEND {self.time_delta}")


def my_shit_code():
    time.sleep(1.3213)


with MyProfiler():
    my_shit_code()
    my_shit_code()
    my_shit_code()



class ReadBigFile:
    def __init__(self):
        self.filename = "lesson26/convertcsv.csv"

    def __iter__(self):
        with open(self.filename) as file:
            yield from file
        

for line in ReadBigFile():
    print(line)