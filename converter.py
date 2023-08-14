def number_to_words(number):
    if number == 0:
        return "Zero"

    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    if 1 <= number <= 9:
        return ones[number]
    elif 11 <= number <= 19:
        return teens[number - 10]
    elif 10 <= number <= 99:
        return tens[number // 10] + (" " + ones[number % 10] if number % 10 != 0 else "")
    elif 100 <= number <= 999:
        return ones[number // 100] + " Hundred" + (" and " + number_to_words(number % 100) if number % 100 != 0 else "")

# Read integer from file


with open("input.txt", "r") as file:
    integer = int(file.read().strip())
    if integer > 999:
        print("enter 3 digit no")
        exit()

# Convert integer to words
words = number_to_words(integer)

# Write result back to file
with open("input.txt", "a") as file:
    file.write("  ")
    file.write(words)


print("Conversion and writing to file successful.")
