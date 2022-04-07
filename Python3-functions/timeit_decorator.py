from time import perf_counter


def timeit_decorator(func):
    @wraps(func)
    def timeit_wrapper(*args, **kw):
        ts = perf_counter()
        result = func(*args, **kw)
        te = perf_counter()

        time_diff_in_sec = te-ts
        if time_diff_in_sec > 3600:
            print(f'*script runtime: {round(time_diff_in_sec/3600,3)} Hours')
        elif time_diff_in_sec > 60:
            print(f'*script runtime: {round(time_diff_in_sec/60,3)} Minutes')
        else:
            print(f'*script runtime: {round(time_diff_in_sec,3)} Seconds')
        return result
    return timeit_wrapper
  
  # how to use?
  
  @timeit_decorator
  def some_function(a):
    pass
