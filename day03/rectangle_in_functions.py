def display(data):
    print(f"The area is {data}")

def get_input():
    received_length = input("Length: ")
    received_width = input("Width: ")

    return (received_length, received_width)

def main():
    (length, width) = get_input()

    area = int(length) * int(width)
    display(area)

main()