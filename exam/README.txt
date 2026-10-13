NETWORK LAB EXPERIMENTS — SIMPLE PYTHON IMPLEMENTATIONS

Requirements:
    python -m pip install simpy

Run each experiment separately.

1. Subnetting:
    python 01_subnetting.py

2. Bit stuffing / destuffing:
    python 02_bit_stuffing.py

3. RARP over TCP sockets:
    Terminal 1: python 03_rarp_server.py
    Terminal 2: python 03_rarp_client.py
    Test MAC: AA:BB:CC:DD:EE:01
    This uses a static MAC-to-IP table to demonstrate the lookup.
    It is a lab simulation, not a real LAN RARP service.

4. Stop-and-Wait ARQ using SimPy:
    python 04_stop_and_wait_simpy.py
    Frames and ACKs can be lost; the sender times out and retransmits.
    The random seed makes the demo repeatable.

5. CDMA:
    python 05_cdma.py
    Enter 0 or 1 for each client. The receiver separates the two
    users by correlating the combined signal with each user's chips.

6. DNS using UDP sockets — start each server in a separate terminal:
    Terminal 1: python 06_dns_root_server.py
    Terminal 2: python 06_dns_tld_server.py
    Terminal 3: python 06_dns_authoritative_server.py
    Terminal 4: python 06_dns_recursive_server.py
    Terminal 5: python 06_dns_client.py

    Try:
        www.example.com  -> 93.184.216.34
        mail.example.com -> 192.0.2.25
        unknown.example.com -> NOT_FOUND

DNS demo flow:
    Client -> Recursive resolver -> Root -> TLD -> Authoritative
    Authoritative -> Recursive resolver -> Client

Important:
- These DNS servers use localhost and UDP ports 5300–5303, so they do
  not query the public Internet and do not conflict with normal DNS port 53.
- The root and TLD servers return referrals (next-server addresses);
  the recursive resolver follows those referrals and returns the final IP.
- The IP addresses are demonstration records.
