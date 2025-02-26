import array as a

# Function for performing insertion sort
def insertion_sort(m, n):
    for i in range(1, n):
        key = m[i]
        j = i - 1
        while j >= 0 and key < m[j]:
            m[j + 1] = m[j]
            j -= 1
        m[j + 1] = key
    print("Marks of students after performing insertion sort on the list:")
    for i in range(len(m)):
        print("%.2f" % m[i])

# Function for performing shell sort
def shell_sort(a, n):
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = temp
        gap //= 2
    print("Marks after shell sort:")
    for n in range(0, n):
        print("%.2f" % a[n])

# Main function
def main():
    arr = a.array('f', [])
    l = int(input("Enter number of students: "))
    print("Enter marks of students:")
    for i in range(0, l):
        print("Student ", i + 1)
        e = float(input())
        arr.append(e)
    print("Student marks before sorting:")
    for n in range(0, l):
        print("%.2f" % arr[n])

    while True:
        print("\nMenu:")
        print("1. Insertion sort of the marks")
        print("2. Shell sort of the marks")
        print("3. Top 5 students")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            insertion_sort(arr, l)
        elif choice == 2:
            shell_sort(arr, l)
        elif choice == 3:
            if l < 5:
                print(l, "topper(s) are:")
                for t in range(l-1, -1, -1):
                    print("%.2f" % arr[t])
            else:
                print("Top students:")
                for k in range(l-1, l-6, -1):
                    print("%.2f" % arr[k])
        elif choice == 4:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
