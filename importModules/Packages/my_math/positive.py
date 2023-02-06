# if you are using an absolute path, you can't execute this module from
# another point as the "root" of your project


# from my_math.abs import my_abs

from abs import my_abs

def is_positive(n):
    return my_abs(n) == n
