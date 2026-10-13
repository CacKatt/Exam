import random
import simpy

random.seed(7)  # Repeatable demonstration; change/remove for different results

FRAME_LOSS_PROBABILITY = 0.25
ACK_LOSS_PROBABILITY = 0.20
TIMEOUT = 4
PROPAGATION_DELAY = 1


class StopAndWait:
    def __init__(self, env, frames):
        self.env = env
        self.frames = frames
        self.expected_frame = 0
        self.process = env.process(self.sender())

    def deliver(self, frame_id, seq, ack_event):
        # Simulate a lost data frame.
        if random.random() < FRAME_LOSS_PROBABILITY:
            print(f"{self.env.now}: Frame {frame_id} (seq={seq}) LOST")
            return

        yield self.env.timeout(PROPAGATION_DELAY)

        if frame_id == self.expected_frame:
            print(f"{self.env.now}: Receiver accepts frame {frame_id} (seq={seq})")
            self.expected_frame += 1
        else:
            print(f"{self.env.now}: Receiver detects duplicate frame {frame_id}")

        # Receiver sends an ACK; it may be lost.
        if random.random() < ACK_LOSS_PROBABILITY:
            print(f"{self.env.now}: ACK for frame {frame_id} LOST")
            return

        if not ack_event.triggered:
            ack_event.succeed()

    def sender(self):
        for frame_id, data in enumerate(self.frames):
            seq = frame_id % 2  # Stop-and-Wait uses alternating 0/1 sequence numbers.
            acknowledged = False

            while not acknowledged:
                print(f"{self.env.now}: Sender sends frame {frame_id}, seq={seq}, data={data}")
                ack_event = self.env.event()
                self.env.process(self.deliver(frame_id, seq, ack_event))

                result = yield ack_event | self.env.timeout(TIMEOUT)
                if ack_event in result:
                    print(f"{self.env.now}: Sender receives ACK for frame {frame_id}")
                    acknowledged = True
                else:
                    print(f"{self.env.now}: Timeout; retransmitting frame {frame_id}")

        print(f"{self.env.now}: All frames delivered.")


env = simpy.Environment()
protocol = StopAndWait(env, ["A", "B", "C", "D"])
env.run(until=protocol.process)
