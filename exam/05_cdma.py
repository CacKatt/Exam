# CDMA demonstration using two orthogonal 4-chip sequences.
# Bit 1 maps to +1; bit 0 maps to -1.

CHIPS = {
    "Client A": [1, 1, 1, 1],
    "Client B": [1, -1, 1, -1],
}


def encode(bit, chips):
    value = 1 if bit == "1" else -1
    return [value * chip for chip in chips]


def decode(signal, chips):
    correlation = sum(x * chip for x, chip in zip(signal, chips)) / len(chips)
    return "1" if correlation > 0 else "0"


bit_a = input("Client A bit (0 or 1): ").strip()
bit_b = input("Client B bit (0 or 1): ").strip()

if bit_a not in ("0", "1") or bit_b not in ("0", "1"):
    print("Each client must enter 0 or 1.")
else:
    signal_a = encode(bit_a, CHIPS["Client A"])
    signal_b = encode(bit_b, CHIPS["Client B"])
    combined = [a + b for a, b in zip(signal_a, signal_b)]

    print("Client A chips :", CHIPS["Client A"])
    print("Client A signal:", signal_a)
    print("Client B chips :", CHIPS["Client B"])
    print("Client B signal:", signal_b)
    print("Combined signal:", combined)
    print("A extracts bit :", decode(combined, CHIPS["Client A"]))
    print("B extracts bit :", decode(combined, CHIPS["Client B"]))
