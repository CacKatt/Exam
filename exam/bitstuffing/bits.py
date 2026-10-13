def stuff(bits):
    res=""
    ones=0
    for bit in bits:
        res+=bit
        if bit=='1':
            ones+=1
            if ones>=5:
                res+='0'
                ones=0
    return res

def destuff(bits):

    res=""
    ones=0

    for bit in bits:
        if ones==5:
            ones=0
            continue
        else:
            res+=bit
            if bit =='1':
                ones+=1
    return res


bits=input("Enter the bits ").strip()

print(f"original {bits}")

stuffed=stuff(bits)
print(f"stuffed {stuffed}")

destuffed=destuff(stuffed)
print(f"destuffed {destuffed}")