import time

def timeit(function):
    def inner(a,b):
        start_time = time.time()
        try:
         res = function(a, b)
        except ZeroDivisionError as e:
         print ("Error" , e)
        except TypeError as e:
            print(e)
        except:
            print("Something went wrong")
        else :
            print("else")
        finally:
            print ("finally")
            end_time = time.time()
        print(f"Time taken: {(end_time - start_time)*1000}")
        return res
    return inner
@timeit
def division(a, b):
    time.sleep(2)  # Simulating a delay
    return a / b

result = division(5,3)
print(f"{result}")