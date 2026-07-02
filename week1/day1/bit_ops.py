def set_bit(reg: int, n: int): #set bit thu n cua reg len 1
    return reg | (1 << n)

def clear_bit(reg: int, n: int): #set bit thu n cua reg xuong 0
    return reg & ~(1 << n)

def toggle_bit(reg: int, n: int): #dao bit thu n cua reg,
    return reg ^ (1 << n)

def read_bit(reg: int, n: int): #doc bit thu n cua reg, tra ve 0 hoac 1
    return (reg >> n) & 1

def print_bin(v: int): #in so v duoi dang nhi phan 8 bit
    print(f"{v:08b}")
    
if __name__ == "__main__":
    reg = 0
    print_bin(reg)
    reg = set_bit(reg, 0)
    reg = set_bit(reg, 2)
    reg = set_bit(reg, 5)
    print_bin(reg)
    reg = clear_bit(reg, 2)
    print_bin(reg)
    reg = toggle_bit(reg, 7)
    print_bin(reg)
    bits = [] # list
    for i in range(8):
        b = read_bit(reg, i)
        bits.append(b)
        print(f" bit {i} = {b}")
    chuoi = "".join(str(b) for b in reversed(bits))


    print(f"Chuoi (MSB -> LSB): {chuoi}")

def count_ones(reg):
    count = 0
    for i in range(8):
        count += read_bit(reg, i)
    return count
    
print(count_ones(reg))
    