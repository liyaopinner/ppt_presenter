def Gen():
    try:
        try:
            yield 1
        except :
            pass
        finally:
            yield 10
    except :
        yield 1
    finally:
        yield 10

gen = Gen()
print(next(gen))