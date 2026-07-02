FIELDS = {
    "RESET":     (7, 1),
    "SLEEP":     (6, 1),
    "CLKSEL":    (3, 3),
    "TEMP_EN":   (2, 1),
    "SMPLRT":    (0, 2),
}

def read_field(reg: int, name: str):
    pass
def write_field(reg: int, name: str, value: int):
    pass
def print_reg(reg: int):
    print(f"reg = {reg:#04x} | bin = {reg:08b}")
    for name in FIELDS:
        print(f" {name:8s} = {read_field(reg, name)}")
if __name__ == "__main__":
    pass
reg = 0x00
print(f"{reg:#04x} -- {reg:08b}")

reg = write_field(reg, "SLEEP", 1)
reg = write_field(reg, "TEMP_EN", 1)

reg = write_field(reg, "CLKSEL", 5)
reg = write_field(reg, "SMPLRT", 3)

