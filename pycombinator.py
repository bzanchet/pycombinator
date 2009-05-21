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

mmlength_0 = \
    ((lambda mklength: \
        mklength(eternity))
    ((lambda length: \
        (lambda x: \
            (cond
                ((null(x), 1)) \
                or (add1 (length (tail(x)))))))))

mmlength_1 = \
    ((lambda mklength: \
        mklength(mklength(eternity)))
    ((lambda length: \
        (lambda x: \
            (cond
                ((null(x), 1)) \
                or (add1 (length (tail(x)))))))))

mmlength_2 = \
    ((lambda mklength: \
        mklength(mklength(mklength(eternity))))
    ((lambda length: \
        (lambda x: \
            (cond
                ((null(x), 1)) \
                or (add1 (length (tail(x)))))))))

mmmlength_1 = \
    ((lambda mklength: \
        mklength(mklength))
    ((lambda mklength: \
        (lambda x: \
            (cond
                ((null(x), 1)) \
                or (add1 (mklength(eternity)
                    (tail(x)))))))))

mmmlength = \
    ((lambda mklength: \
        mklength(mklength))
    ((lambda mklength: \
        (lambda l: \
            (cond
                ((null(l), 1)) \
                or (add1 (mklength(mklength)
                    (tail(l)))))))))

# error_mmmlength = \
#     ((lambda mklength: \
#         mklength(mklength))
#     ((lambda mklength: \
#         (( lambda length: \
#             (lambda x: \
#                 (cond
#                     ((null(x), 1)) \
#                     or (add1 (length (tail(x)))))))
#         (mklength(mklength))))))
        
mmmlength = \
    ((lambda mklength: \
        mklength(mklength))
    ((lambda mklength: \
        (lambda l: \
            (cond
                ((null(l), 1)) \
                or (add1
                    ((lambda x: \
                        mklength(mklength)(x))
                    (tail(l)))))))))

# extract and abstract 
# (lambda x: \
#     mklength(mklength)(x))
mmmlength = \
    ((lambda mklength: \
        mklength(mklength))
    ((lambda mklength: \
        (lambda length: \
            (lambda l: \
                (cond
                    ((null(l), 1)) \
                    or (add1
                        (length((tail(l))))))))
        (lambda x: \
            mklength(mklength)(x)))))
            
# extract length
mmmlength = \
    ((lambda le: 
        ((lambda mklength: \
            mklength(mklength))
         (lambda mklength: \
             le(lambda x: \
                 (mklength(mklength))(x)))))
    (lambda length: \
        (lambda l: \
            (cond
                ((null(l), 1)) \
                or (add1
                    (length((tail(l)))))))))

# renaming mklength to l
mmmlength = \
    ((lambda le: 
        ((lambda f: f(f))
         (lambda f: \
             le(lambda x: \
                 (f(f))(x)))))
    (lambda length: \
        (lambda l: \
            (cond
                ((null(l), 1)) \
                or (add1
                    (length((tail(l)))))))))
           
           
# "now that we understand recursion, we can use 'def' again"  
def Y(le):
    return(
        (lambda f: f(f))
        (lambda f: \
             le(lambda x: (f(f))(x)))
    )

length_y = Y(
    lambda length: \
        (lambda l: \
            (cond
                ((null(l), 1)) \
                or (add1
                    (length((tail(l))))))))
                            