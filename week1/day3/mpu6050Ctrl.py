class Mpu6050Ctrl:
    FIELDS = {
        "RESET": (7, 1),
        "SLEEP": (6, 1),
        "CLKSEL": (3, 3),
        "TEMP_EN": (2, 1),
        "SMPLRT": (0, 2),
    }
    
    def __init__(self, i2c_address: int = 0x68):
        self.i2c_address = i2c_address
        self.reg = 0x00
    
    def set_field(self, name: str, value: int):
        if name in self.FIELDS:
            start_bit, length = self.FIELDS[name]
            mask = ((1 << length) - 1) << start_bit
            self.reg &= ~mask  
            self.reg |= (value & ((1 << length) - 1)) << start_bit
            if name == "RESET" and value == 1:
                sensor_A.reg = 0
        return
    
    def get_field(self, name: str):
        pass
    
    def dump(self):
        print(f"reg = {self.reg:#04x} | bin = {self.reg:08b}")
        for name in self.FIELDS:
            print(f" {name:8s} = {self.get_field(name)}")
            
    def __repr__(self):
        return f"<Mpu6050Ctrl @0x{self.i2c_address:02x} reg = 0x{self.reg:02x}>"
if __name__ == "__main__":
    sensor_A = Mpu6050Ctrl(0x68)
    print(sensor_A)
    sensor_A.set_field("SLEEP", 1)
    sensor_A.set_field("TEMP_EN", 1)
    print(f"sensor_A.reg = {sensor_A.reg:#04x}")
    sensor_A.set_field("CLKSEL", 5)
    sensor_A.set_field("RESET", 1)
    print(f"sensor_A.reg = {sensor_A.reg:#04x}")
    sensor_B = Mpu6050Ctrl(0x68)
    print(sensor_B)
    sensor_B.set_field("SMPLRT", 3)
    print(f"sensor_A.reg = {sensor_A.reg:#04x}")
    print(f"sensor_B.reg = {sensor_B.reg:#04x}")
    
    
    
    

        
        