chip_a=[1,1]
chip_b=[1,-1]

def encode(bit,chips):
    value=1 if bit==1 else -1
    return [value*chip for chip in chips]

def combine(signal_a,signal_b):
    return [a+b for a,b in zip(signal_a,signal_b)]

def decode(signal,chips):
    correlation=sum(x*chip for x,chip in zip(signal,chips))/len(chips)
    return 1 if correlation>0 else 0
a_data=int(input("Enter the data of channel a: "))
b_data=int(input("Enter the data of channel b: "))

a_signal=encode(a_data,chip_a)
b_signal=encode(b_data,chip_b)

channel_signal=combine(a_signal,b_signal)

a_decode=decode(channel_signal,chip_a)
b_decode=decode(channel_signal,chip_b)

print("Channel a data: ",a_data)
print("Channel b data: ",b_data)

print("Channel a signal: ",a_signal)
print("Channel b signal: ",b_signal)

print("Combined signal: ",channel_signal)

print("Decoded channel a data: ",a_decode)
print("Decoded channel b data: ",b_decode)