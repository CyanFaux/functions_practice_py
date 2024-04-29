def hello():
    print("Greetings, user")

def pack(a, b, c):
    return [a, b, c]

my_list = pack("apple", "banana", "carrot")

def eat_lunch(my_list):
    print("First I eat " + my_list[0])
    print("Next I eat " + my_list[1])
    print("Next I eat " + my_list[2])
    print("My lunchbox is empty!")

# after some research with chatGPT...
def eat_lunch2(my_list):
    if len(my_list) > 0:
        print("First, I eat " + my_list[0])
        for i, item in enumerate(my_list[1:], start=1):
            print("Next, I eat " + item)
        print("My lunchbox is empty!")
    else:
        print("My lunchbox is empty!")

hello()
print(my_list)
eat_lunch(my_list)
eat_lunch2(my_list)