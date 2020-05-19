from datetime import datetime

class Timer:
    def __enter__(self):
        self._start = datetime.utcnow()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(datetime.utcnow() - self._start)


if __name__ == "__main__":
    with(Timer()):
        for i in range(1000):
            pass

