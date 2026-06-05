def details(*args, **kwargs):
    print("The non keyword values or positioned values : " )#collects data in tuples
    for arg in args:
        print(arg)
    print("The keyword values : ")
    for key, value in kwargs.items():
        print(f"{key}=={value}")
obj=details(23, "bhavs", )