import multiprocessing
import time
import user

TIMEOUT = 0.5

def userFunc():
    user.main()

def hanging_function():
    print("main()))))))")
    time.sleep(5)
    print("okokokko")

process = multiprocessing.Process(target=userFunc)
process.daemon = True
process.start()

process.join(TIMEOUT)
if process.is_alive():
    print("Function is hanging!")
    process.terminate()
    print("Kidding, just terminated!")