class CustomException(Exception):
    pass


ce = CustomException()
help(ce.__str__())
print(ce)
