def stuff(bits):
    result = ""
    ones = 0

    for bit in bits:
        result += bit
        if bit == "1":
            ones += 1
            if ones == 5:
                result += "0"  # Insert a 0 after five consecutive 1s
                ones = 0
        else:
            ones = 0
    return result


def destuff(bits):
    result = ""
    ones = 0
    i = 0

    while i < len(bits):
        bit = bits[i]
        result += bit
        i += 1

        if bit == "1":
            ones += 1
            if ones == 5:
                # A stuffed 0 must follow five consecutive 1s.
                if i < len(bits) and bits[i] == "0":
                    i += 1
                ones = 0
        else:
            ones = 0
    return result


data = input("Enter data bits (0s and 1s only): ").strip()
if not data or any(bit not in "01" for bit in data):
    print("Enter a non-empty string containing only 0 and 1.")
else:
    stuffed = stuff(data)
    received = destuff(stuffed)
    print("Original data :", data)
    print("Stuffed frame :", stuffed)
    print("After destuff :", received)
