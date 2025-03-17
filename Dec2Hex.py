import sys

def decimal_to_hex(decimal_value):
    """Convert decimal value to hexadecimal."""
    # List of hexadecimal characters
    hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    
    if decimal_value == 0:
        return "0"  # Handle edge case for 0
    
    hexadecimal = ""
    num = decimal_value
    
    # Logging the process
    print(f"Starting conversion of Decimal Value {num} to Hex...")
    # do some changes

    while num != 0:
        rem = num % 16
        hexadecimal = hex_chars[rem] + hexadecimal
        num //= 16

    print(f"Hexadecimal representation is: {hexadecimal}")
    return hexadecimal  # Return the hexadecimal value for testing

def main():
    """Main function to handle command line input and conversion."""
    if len(sys.argv) > 1:
        try:
            # Validate input
            print("always enter valid input")
            
            decimal_value = int(sys.argv[1])
            if decimal_value < 0:
                print("Please provide a positive integer.")
            else:
                print(f"Input decimal value: {decimal_value}")
                decimal_to_hex(decimal_value)
        except ValueError:
            print("Error: Please provide a valid integer.") #display error
    else:
        print("Usage: python script.py <decimal_number>")

if __name__ == "__main__":
    main()


