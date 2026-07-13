class SensorFrame:
    STX = 0xAA
    ETX = 0x55

    def __init__(self, cmd: int, payload: bytes = b''):
        self.cmd = cmd
        self.payload = bytes(payload)

    def build(self) -> bytes:
        length = len(self.payload)
        body = bytes([length, self.cmd]) + self.payload   
        chk = 0
        for b in body:
            chk ^= b                                       
        return bytes([self.STX]) + body + bytes([chk, self.ETX])

    @classmethod
    def parse(cls, data: bytes) -> "SensorFrame":
        if len(data) < 5:
            raise ValueError("frame too short")
        if data[0] != cls.STX:
            raise ValueError("bad STX")
        if data[-1] != cls.ETX:
            raise ValueError("bad ETX")
        length = data[1]
        cmd = data[2]
        payload = data[3:3 + length]
        chk_received = data[3 + length]
        chk_calc = 0
        for b in data[1:3 + length]:
            chk_calc ^= b
        if chk_calc != chk_received:
            raise ValueError(f"checksum mismatch: got {chk_received:02x}, expected {chk_calc:02x}")
        return cls(cmd, payload)

    def __repr__(self) -> str:
        return f"<SensorFrame cmd=0x{self.cmd:02x} payload={self.payload.hex()}>"


def selftest():
    cases = [
        (0x01, b'',           'aa 00 01 01 55'),
        (0x02, b'\x10\x20',   'aa 02 02 10 20 30 55'),
    ]
    for cmd, payload, expected in cases:
        got = SensorFrame(cmd, payload).build().hex(' ')
        status = "OK" if got == expected else "FAIL"
        print(f"[{status}] cmd={cmd:#04x} payload={payload.hex()} -> {got}  (expected {expected})")


def roundtrip_test():
    samples = [
        (0x01, b''),
        (0x02, b'\x10\x20'),
        (0x7F, b'\x00\x01\x02\x03\x04'),
        (0xFF, bytes(range(20))),
    ]
    for cmd, payload in samples:
        orig = SensorFrame(cmd, payload)
        parsed = SensorFrame.parse(orig.build())
        ok = (orig.cmd == parsed.cmd) and (orig.payload == parsed.payload)
        print(f"[{'OK' if ok else 'FAIL'}] cmd={cmd:#04x} payload_len={len(payload)}")


def run_5_scenarios():
    print("Buoc 1: SensorFrame(0x01, b'').build()")
    out1 = SensorFrame(0x01, b'').build()
    expect1 = bytes.fromhex('aa0001 0155'.replace(' ', ''))
    print(f"  got:      {out1.hex(' ')}")
    print(f"  expected: aa 00 01 01 55")
    print(f"  {'OK' if out1 == expect1 else 'FAIL'}")

    print()
    print("Buoc 2: SensorFrame(0x02, b'\\x10\\x20').build()")
    out2 = SensorFrame(0x02, b'\x10\x20').build()
    expect2 = bytes.fromhex('aa020210203055'.replace(' ', ''))
    print(f"  got:      {out2.hex(' ')}")
    print(f"  expected: aa 02 02 10 20 30 55")
    print(f"  {'OK' if out2 == expect2 else 'FAIL'}")

    print()
    print("Buoc 3: SensorFrame.parse(build_bytes) - buoc 1 va 2")
    orig1 = SensorFrame(0x01, b'')
    p1 = SensorFrame.parse(orig1.build())
    ok1 = (orig1.cmd == p1.cmd) and (orig1.payload == p1.payload)
    print(f"  buoc1 -> cmd/payload khop instance goc: {'OK' if ok1 else 'FAIL'}")

    orig2 = SensorFrame(0x02, b'\x10\x20')
    p2 = SensorFrame.parse(orig2.build())
    ok2 = (orig2.cmd == p2.cmd) and (orig2.payload == p2.payload)
    print(f"  buoc2 -> cmd/payload khop instance goc: {'OK' if ok2 else 'FAIL'}")

    print()
    print("Buoc 4: parse(b'\\xaa\\x02\\x02\\x10\\x20\\xff\\x55')  # CHK sai")
    try:
        SensorFrame.parse(b'\xaa\x02\x02\x10\x20\xff\x55')
        print("  FAIL: khong raise ValueError")
    except ValueError as e:
        print(f"  OK, raise ValueError: {e}")

    print()
    print("Buoc 5: parse(b'\\xbb\\x00\\x01\\x01\\x55')  # STX sai")
    try:
        SensorFrame.parse(b'\xbb\x00\x01\x01\x55')
        print("  FAIL: khong raise ValueError")
    except ValueError as e:
        print(f"  OK, raise ValueError: {e}")


if __name__ == "__main__":
    run_5_scenarios()

    print()
    print("--- selftest() va roundtrip_test() (tham khao them) ---")
    selftest()
    print()
    roundtrip_test()

