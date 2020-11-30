            
def calculateOddSum(array):
    sum = 0
    for number in array:
        if number % 2 != 0:
            sum += number
    return sum

def main():
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
   
    odds_sum = calculateOddSum(numbers)
    print(odds_sum)
    
if __name__ == "__main__":
    main()



