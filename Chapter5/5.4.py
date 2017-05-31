import sys

def printNextNumbers(num):
    m = 1
    smallIndex = 0
    largeIndex = 0
    first = True
    for iterator in range(0, 32):
        n = m << iterator
        if(first):
            prev = (num & n) > 0
            first = False
            continue
        else:
            curr =  (num & n) > 0
            if not prev and curr and smallIndex == 0:
                smallIndex = iterator
            elif prev and not curr and largeIndex == 0:
                largeIndex = iterator
            elif (smallIndex > 0 and largeIndex > 0) or (num < (1 << iterator)):
                break
            prev = curr
    if smallIndex == 0:
        print("This number contains all one's. So smaller number with same number of 1's is not possible")
    else:
        print("The immediate smallest number than " + str(num) + " is: " + str(num - (1 << (smallIndex - 1))))
    if largeIndex == 0:
        print("This number is -1. So larger number is 0")
    else:
        print("The immediate largest number than " + str(num) + " is: " + str(num + (1 << (largeIndex - 1))))

def main():
    arguments = sys.argv
    if len(arguments) != 2:
        print("More or less arguments are passed than required arguments")
        exit(-2)
    printNextNumbers(int(arguments[1]))
    return 0

if __name__ == "__main__":
    main()
    sys.exit()