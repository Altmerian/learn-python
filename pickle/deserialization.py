import pickle
# from Student import Student

with open("./pickle/students.pkl", "rb") as f:
    while True:
        try:
            student = pickle.load(f)
            print(student)
        except EOFError:
            break
