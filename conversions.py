def detectar_base(entrada):
    entrada = entrada.strip().upper()
    if entrada.startswith("0B"):
        return "bin"
    elif entrada.startswith("0O"):
        return "oct"
    elif entrada.startswith("0X"):
        return "hex"
    else:
        return "dec"

def binario_a_decimal(bin_str):
    num = 0
    for char in bin_str[2:]:
        if char == '1':
            num = (num * 2) + 1
        elif char == '0':
            num = num * 2
        else:
            raise ValueError("Binario inválido")
    return num

def octal_a_decimal(oct_str):
    num = 0
    for char in oct_str[2:]:
        if not ('0' <= char <= '7'):
            raise ValueError("Octal inválido")
        dig = ord(char) - ord('0')
        num = (num * 8) + dig
    return num

def hex_a_decimal(hex_str):
    num = 0
    hex_digits = "0123456789ABCDEF"
    for char in hex_str[2:]:
        if char not in hex_digits:
            raise ValueError("Hexadecimal inválido")
        dig = hex_digits.index(char)
        num = (num * 16) + dig
    return num

def decimal_a_binario(num):
    if num == 0:
        return "0b0"
    binario = ""
    while num > 0:
        residuo = num % 2
        binario = str(residuo) + binario
        num = num // 2
    return "0b" + binario

def decimal_a_octal(num):
    if num == 0:
        return "0o0"
    octal = ""
    while num > 0:
        residuo = num % 8
        octal = str(residuo) + octal
        num = num // 8
    return "0o" + octal

def decimal_a_hex(num):
    if num == 0:
        return "0x0"
    hex_digits = "0123456789ABCDEF"
    hex_num = ""
    while num > 0:
        residuo = num % 16
        hex_num = hex_digits[residuo] + hex_num
        num = num // 16
    return "0x" + hex_num

def validar_binario(bin_str):
    if not bin_str.startswith("0b"):
        return False
    for char in bin_str[2:]:
        if char not in "01":
            return False
    return True

def validar_octal(oct_str):
    if not oct_str.startswith("0o"):
        return False
    for char in oct_str[2:]:
        if not ('0' <= char <= '7'):
            return False
    return True

def validar_hex(hex_str):
    if not hex_str.startswith("0x"):
        return False
    hex_digits = "0123456789ABCDEF"
    for char in hex_str[2:].upper():
        if char not in hex_digits:
            return False
    return True

def main():
    while True:
        try:
            entrada = input("Introdueix un número (0b..., 0o..., 0x... o decimal): ")
            
            base = detectar_base(entrada)
            
            if base == "dec":
                num = int(entrada)
            elif base == "bin":
                if not validar_binario(entrada):
                    raise ValueError("Binario inválido")
                num = binario_a_decimal(entrada)
            elif base == "oct":
                if not validar_octal(entrada):
                    raise ValueError("Octal inválido")
                num = octal_a_decimal(entrada)
            elif base == "hex":
                if not validar_hex(entrada):
                    raise ValueError("Hexadecimal inválido")
                num = hex_a_decimal(entrada)
            
            print(f"Decimal: {num}")
            print(f"Binari: {decimal_a_binario(num)}")
            print(f"Octal: {decimal_a_octal(num)}")
            print(f"Hexadecimal: {decimal_a_hex(num)}")
            break
            
        except ValueError as e:
            print(f"Error: {e}. Inténtalo de nuevo.")
        except:
            print("Error: Número inválido. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
