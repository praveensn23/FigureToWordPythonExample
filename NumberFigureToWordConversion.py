# List containing the literals to be substituted for each number depending on the position
words = [
    # units (1)
    ["one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine "],
    # tens (2)
    ["ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ",
     "nineteen "],
    ["twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "],
    ]

result = ""
concat = ""
figure = ""
decimal = ""

digit = 0
numLen = 0
decLen = 0
value = 0.0


# Function returns the word of the unit equivalent number
def units(num):
    if num > 0:
        return words[0][num-1]
    else:
        return ""


# Function returns the word of the tens equivalent number
def tens(num):
    if num > 0:
        if num < 20:
            major_index = num - 10
            return words[1][major_index]
        else:
            minor_index = num % 10
            major_index = int(num / 10)
            if minor_index == 0:
                return words[2][major_index - 2]
            else:
                return words[2][major_index - 2] + words[0][minor_index - 1]


# Function returns the word of the hundreds equivalent number
def hundreds(num):
    if num > 0:
        return units(num) + "hundred "
    else:
        return ""


# Function returns the word of the thousands equivalent number
def thousands(num):
    if num > 0 and num < 10:
        return units(num) + "thousand "
    elif num >= 10:
        return tens(num) + "thousand "
    else:
        return ""


# Function returns the word of the lakhs equivalent number
def lakhs(num):
    if num > 0 and num < 10:
        return units(num) + "lakh "
    elif num >= 10:
        return tens(num) + "lakh "
    else:
        return ""


# Function returns the word of the crores equivalent number
def crores(num):
    if num > 0 and num < 10:
        return units(num) + "crore "
    elif num >= 10:
        return tens(num) + "crore "
    else:
        return ""


def num_after_point(nos):
    s = str(nos)
    if not '.' in s:
        return 0
    return len(s) - s.index('.') - 1


# Take the input from the user
value = float(input("Enter the amount in figures (999999999.99 max) : Rs "))

# Check if the input exceeds the precribed no of digits
if value > 999999999.99:
    print("Error: exceeds maximum allowable amount !!!")
    exit()

decLen = num_after_point(value)
if decLen > 2:
    print("Error: decimal exceeds more then 2 !!!")
    exit()
else:
    decimal = str(int(value * 100 - int(value) * 100))

figure = str(int(value))
if int(value) > 100:
    concat = "and "

numLen = len(figure)
while numLen != 0:
    if numLen == 1:
        digit = int(figure[numLen - 1])
        if digit == 0:
            result += ""
        else:
            result += units(digit) + "rupees "
    elif numLen == 2:
        digit = int(figure[numLen - 2]) * 10 + int(figure[numLen - 1])
        if digit == 0:
            result += "rupees "
        elif digit > 0 and digit < 10:
            result += concat + units(digit) + "rupees "
        else:
            result += concat + tens(digit) + "rupees "
    elif numLen == 3:
        digit = int(figure[numLen - 3])
        result += hundreds(digit)
    elif numLen == 4:
        digit = int(figure[numLen - 4])
        result += thousands(digit)
    elif numLen == 5:
        digit = int(figure[numLen - 5]) * 10 + int(figure[numLen - 4])
        result += thousands(digit)
    elif numLen == 6:
        digit = int(figure[numLen - 6])
        result += lakhs(digit)
    elif numLen == 7:
        digit = int(figure[numLen - 7]) * 10 + int(figure[numLen - 6])
        result += lakhs(digit)
    elif numLen == 8:
        digit = int(figure[numLen - 8])
        result += crores(digit)
    elif numLen == 9:
        digit = int(figure[numLen - 9]) * 10 + int(figure[numLen - 8])
        result += crores(digit)

    if numLen >= 4:
        if numLen % 2:
            figure = figure[2:numLen]
            numLen = numLen - 2
        else:
            figure = figure[1:numLen]
            numLen = numLen - 1
    else:
        if numLen % 2:
            figure = figure[1:numLen]
            numLen = numLen - 1
        else:
            figure = figure[2:numLen]
            numLen = numLen - 2

if int(value) > 0:
    concat = "and "
else:
    concat = ""

numLen = len(decimal)
while numLen != 0:
    if numLen == 1:
        digit = int(decimal[numLen - 1])
        if digit == 0:
            result += " only"
        else:
            result += concat + units(digit) + "paise only"
        decimal = decimal[1:numLen]
        numLen = numLen - 1
    elif numLen == 2:
        digit = int(decimal[numLen - 2]) * 10 + int(decimal[numLen - 1])
        result += concat + tens(digit) + "paise only"
        decimal = decimal[2:numLen]
        numLen = numLen - 2

print("result : " + result)
