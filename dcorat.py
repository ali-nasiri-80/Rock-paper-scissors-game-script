from datetime import datetime


def log_time(func):
    def wrap_function(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        total = end_time - start_time
        hours = total.seconds // 3600
        minutes = total.seconds // 60
        seconds = total.seconds % 60
        print(f"total{hours}:{minutes}:{seconds}")

        return result

    return wrap_function
