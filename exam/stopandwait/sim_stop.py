import simpy
import random

def sender(env, data, ack):
    seq = 0

    for i in range(5):
        while True:
            print(f"\nSender: Sending Frame {seq}")
            yield data.put(seq)

            # Wait for ACK or timeout
            result = yield ack.get() | env.timeout(2)

            if ack in result:
                if result[ack] == seq:
                    print(f"Sender: ACK {seq} received")
                    seq = 1 - seq
                    break
                else:
                    print("Wrong ACK received")
            else:
                print("Timeout! Resending frame")


def receiver(env, data, ack):
    expected = 0

    while True:
        seq = yield data.get()

        # Simulate data frame loss
        if random.random() < 0.2:
            print(f"Receiver: Frame {seq} lost")
            continue

        if seq == expected:
            print(f"Receiver: Frame {seq} received")
            expected = 1 - expected
        else:
            print(f"Receiver: Duplicate Frame {seq} discarded")

        # Simulate ACK loss
        if random.random() < 0.2:
            print(f"Receiver: ACK {seq} lost")
        else:
            print(f"Receiver: Sending ACK {seq}")
            yield ack.put(seq)


env = simpy.Environment()
data = simpy.Store(env)
ack = simpy.Store(env)

env.process(sender(env, data, ack))
env.process(receiver(env, data, ack))

env.run(until=30)