import colorama

def HexadecimalToDecimal():
    while True:
        hex_number = input(f"{colorama.Fore.CYAN}Hexadecimal number: {colorama.Fore.RESET}")
        decimal_number = int(hex_number, 16)
        print(f'Decimal number: {colorama.Fore.GREEN}{decimal_number}{colorama.Fore.RESET}')

def main():
    HexadecimalToDecimal()

if __name__ == '__main__':
    main()
    
