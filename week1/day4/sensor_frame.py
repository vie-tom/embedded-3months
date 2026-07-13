class SensorFrame:
    #Frame protocol don gian: STX-LEN-PAYLOAD-CHK-ETX.
    
    STX = 0xAA
    ETX = 0x55
    
    def __init__(self, cmd: init, payload: bytes = b''):
        self.cmd = cmd
        self.payload = bytes(payload)
    def build(self) -> bytes:
        #Dong goi thanh frame hoan chinh.
        
    @classmethod
    def parse(cls, data: bytes) -> "SensorFrame":
        #Giai ma frame, kiem tra STX/ETX/CHK, tra ve instance moi.
        pass

    def __repr__(self) -> str:
        return f"<SensorFrame cmd=0x(self.cmd:02x)payload=(self.payload.hex())>"

if __name__ == "__main__":
    SensorFrame(0x01, b'').build()
    
