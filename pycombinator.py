from functools import partial

def cond(*args):
    for tup in args:
        if tup[0]:
            return tup[1]

def tail(l):
    return l[1:]

def eternity(x):
    None
    
def add1(n):
    return 1+n
    
def null(l):
    return len(l) == 0
    
length_0 = \
    (lambda x: \
        (cond
            ((null(x), 1)) \
            or (add1 (eternity (tail(x))))))

length_1 = \
    (lambda x: \
        (cond
            ((null(x), 1)) \
            or (add1 (
                (lambda x: \
                    (cond
                        ((null(x), 1)) \
                        or (add1 (eternity (tail(x))))))
                (tail(x))))))


mlength_0 = \
    ((lambda length: \
        (lambda x: \
            (cond
                ((null(x), 1)) \
                or (add1 (length (tail(x)))))))
    (eternity))

mlength_1 = \
    ((lambda length: \
        (lambda x: \
            (cond
                ((null(x), 1)) \
                or (add1 (length (tail(x)))))))
    ((lambda length: \
        (lambda x: \
            (cond
                ((null(x), 1)) \
                or (add1 (length (tail(x)))))))
    (eternity)))

mlength_2 = \
    ((lambda length: \
        (lambda x: \
            (cond
                ((null(x), 1)) \
                or (add1 (length (tail(x)))))))
    ((lambda length: \
        (lambda x: \
            (cond
                ((null(x), 1)) \
                or (add1 (length (tail(x)))))))
    ((lambda length: \
        (lambda x: \
            (cond
                ((null(x), 1)) \
                or (add1 (length (tail(x)))))))
    (eternity))))


