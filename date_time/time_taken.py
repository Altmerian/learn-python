import datetime


start_time = datetime.datetime.now()

for i in range(100_000_000):
    pass

end_time = datetime.datetime.now()
execution_time = (end_time - start_time)

print("Execution time:", execution_time)
