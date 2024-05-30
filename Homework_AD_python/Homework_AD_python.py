import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    random.seed()
    choice = int(input("Choose an option:\n1. Manual input of book sizes\n2. Randomly generate book sizes\n"))

    if choice == 1:
        # Manual input
        num_employees = int(input("Enter the number of employees: "))
        total_books = int(input("Insert the amount of books you want: "))
        books = []
        print("Now for the number of pages for each book.")
        for i in range(total_books):
            book_pages = int(input(f"Pages for Book[{i + 1}]: "))
            books.append(book_pages)
    elif choice == 2:
        # Randomly generate book sizes
        num_employees = random.randint(1, 10000)
        print(f"\nNumber employees: {num_employees}")

        total_books = random.randint(1, 20000)
        while total_books <= num_employees / 2:
            total_books = random.randint(1, 20000)

        print(f"\nNumber Books: {total_books}\n\n")
        books = [random.randint(100, 10099) for _ in range(total_books)]
    else:
        print("Invalid choice. Please choose 1 or 2.")
        return

    insertion_sort(books)

    total_pages = sum(books)
    avg_pages = total_pages // num_employees

    current_sum = 0
    sections = 1
    print("Employee 1: ", end="")
    for book in books:
        current_sum += book
        if current_sum > avg_pages * sections:
            print(f"\nEmployee {sections + 1}: ", end="")
            sections += 1
        print(book, end=" ")

    print(f"\nAverage pages per employee: {avg_pages}")

if __name__ == "__main__":
    main()