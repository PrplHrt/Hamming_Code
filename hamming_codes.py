from functools import reduce
# When running this locally, you will need numpy installed https://numpy.org/install/
import numpy as np

# Printing method that prints out the message in a square
def print_block(message):
    row_size = len(message) ** 0.5
    i = 0
    for bit in message:
        print(bit, end=" ")
        if i == row_size - 1:
            print()
        i = (i + 1) % row_size
    

def apply_parity(message):
    # Find which parity bits need to be changed
    ans = reduce(lambda x,y: x^y, [pos for pos, bit in list(enumerate(message)) if bit])
    # Removing the "0b" that python generates
    bits = bin(ans)[2:]
    print("Resulting binary from the XOR operation: ", bits)
    
    i = 0
    # Iterate through the binary in reverse to access bit 1, 2, 4, and so on...
    for bit in bits[::-1]:
        # If this bit was marked to be swapped by the XOR function, we change it
        if int(bit):
            print("Changing bit #", 2**i, " from ",  message[2**i], " to ", int(not  message[2**i]))
            message[2**i] = int(not message[2**i])
        # Using i to keep track of the parity bit we're at
        i += 1

    # Simple formula to use the 0th element to keep an even number of 1s
    message[0] = (sum(message) - message[0]) % 2

    return message

# Randomly change one bit in the message
def rand_error(message):
    error = np.random.randint(0, len(message))
    print("Changing bit #", error, " from ", message[error], " to ", int( not message[error]))
    message[error]  = not message[error]
    return message

# Fixing the faulty bit
def fix_error(message):
    # Find the faulty bit
    error = reduce(lambda x,y: x^y, [pos for pos, bit in list(enumerate(message)) if bit])

    print("Changing bit #", error, " from ", message[error], " to ", int( not message[error]))
    # Change the bit
    message[error]  = not message[error]

    return message



if __name__ == "__main__":
    # For debugging purposes (Makes sure that the same numbers appear each time)
    np.random.seed(42)

    while True:
        try:
            size = int(input(
"""Pick size:
        1. 4 bits
        2. 16 bits
        3. 64 bits
        4. 256 bits
            
    Choice: """))
            # Makes sure option is within limits
            if 1 <= size <= 4:
                break
            else:
                print("Please limit yourself to options 1 to 4")
        except Exception:
            # In case non integer is entered into the terminal
            print("Please try again!")

    # Get a random list of 1s and 0s
    message = np.random.randint(0, 2, 2**(size*2))

    print("Initial message:")
    print_block(message)

    # Applying the right parity bits
    message = apply_parity(message)

    print("After parity applied:")
    print_block(message)

    # Adding an error into the message
    print("Adding an error:")
    message = rand_error(message)
    print_block(message)

    print("Fixing the error:")
    message = fix_error(message)
    print_block(message)
