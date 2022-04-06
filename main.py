import random


def main():
    option = " "
    
    while (option[0].lower() != "q"):
        print("Bubble sort algorithm\n"\
            + "n    - manually input an array\n"\
            + "r    - generate radnom array with random size in 50-100 range\n"\
            + "r n  - generate random n-sized array\n"\
            + "q    - quit\n\n"\
            + "Choose option: ", end='')
        option = input()
        
        if (len(option) > 0):
            if (option[0].lower() == "q"):
                return
                
            elif (option[0].lower() == "n"):
                print("Enter an array, separate with 'space': ", end='')

                try:
                    array = list(map(int, input().split()))

                    print("\nUnsorted", array, sep='\n', end='\n\n')
                    bubbleSort(array)
                    print("Sorted", array, sep='\n', end='\n\n')
                except ValueError:
                    print("Only numbers allowed. Please, try again.\n")
            elif (len(option) == 1 and option.lower() == "r"):
                array = []
                for i in range(random.randrange(50, 101)):
                    array.append(random.randrange(100000))

                print("\nUnsorted", array, sep='\n', end='\n\n')
                bubbleSort(array)
                print("Sorted", array, sep='\n', end='\n\n')
            elif (len(option) > 1 and option[0] == "r"):
                try:
                    size = int(option.split()[1])
                    array = []
                    for i in range(size):
                        array.append(random.randrange(100000))

                    print("\nUnsorted", array, sep='\n', end='\n\n')
                    bubbleSort(array)
                    print("Sorted", array, sep='\n', end='\n\n')
                except:
                    print("Unable to cast to integer. Please, try again.")
            else:
                print("Unable to handle input. Please, try again.\n")
        else:
            option = " "
            print()


def bubbleSort(array):
    size = len(array)
    while (True):
        isSorted = True
        for i in range(size - 1):
            if (array[i] > array[i + 1]):
                isSorted = False
                array[i], array[i + 1] = array[i + 1], array[i]
        size = size - 1
        if (isSorted == True):
            break


if __name__ == '__main__':
    main()
