# Function for partitioning the data
def partition(m, lb, ub):
    pivot = m[lb]
    s = lb + 1
    e = ub
    while s <= e:
        while s <= ub and m[s] <= pivot:
            s += 1
        while m[e] > pivot:
            e -= 1
        if s < e:
            m[s], m[e] = m[e], m[s]
    m[e], m[lb] = m[lb], m[e]
    return e

# Function for performing Quick Sort on the data
def quick_sort(m, lb, ub):
    if lb < ub:
        loc = partition(m, lb, ub)
        quick_sort(m, lb, loc - 1)
        quick_sort(m, loc + 1, ub)

# Function for displaying sorted percentages
def display(m):
    print("\nSorted student percentages:")
    for i, perc in enumerate(m, 1):
        print(f"Student {i}: {perc:.2f}%")

# Main function
def main():
    l = int(input("Enter the number of students: "))
    arr = [float(input(f"Enter percentage for Student {i+1}: ")) for i in range(l)]
    print("\nStudents' percentages before sorting:")
    for i, perc in enumerate(arr, 1):
        print(f"Student {i}: {perc:.2f}%")

    while True:
        print("\nMenu:")
        print("1. Sort percentages")
        print("2. Show Top 5 students")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            quick_sort(arr, 0, l - 1)
            display(arr)
        elif choice == 2:
            top = min(l, 5)
            print("\nTop students:")
            for i in range(top):
                print(f"Student {i+1}: {arr[l-i-1]:.2f}%")
        elif choice == 3:
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
