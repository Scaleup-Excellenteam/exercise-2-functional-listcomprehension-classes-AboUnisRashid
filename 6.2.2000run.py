
import time

def timer(f, *args, **kwargs):
    """
    :param f: The function to be timed.
    :param args:
    :param kwargs:
    :return: time taken by a function to execute.
    """
    start = time.time()
    f(*args, **kwargs)
    end_time = time.time()
    run_time = end_time - start
    real_time = f"{run_time:.6f}"
    return real_time


def main():
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print(timer("Hi {name}".format, name="Bug"))
    return 0


if __name__ == '__main__':
    main()
