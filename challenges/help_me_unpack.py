from utils.hackattic import data_request, read_token, solution_post
import os
import base64
import struct

def main(token):
    # Name of challenge
    challenge_name = "help_me_unpack"
    
    # Data of the challenge to a dict/json
    challenge_dict = data_request(challenge_name, token)

    # -----Solution------
    byte_data = base64.b64decode(challenge_dict['bytes'])
    
    '''
    By default, `struct.unpack` uses standard C alignment rules. This means there may be padding bytes added between the fields to align each field to its natural alignment boundary.
    
    1. `'i'` (4 bytes): Starts at offset 0 (aligned at 4 bytes).
    2. `'I'` (4 bytes): Starts at offset 4 (aligned at 4 bytes).
    3. `'h'` (2 bytes): Starts at offset 8 (aligned at 2 bytes).
    4. Padding may be added here to align the next 4-byte type:
    - Since `h` is 2 bytes, there are no additional padding bytes needed after it.
    5. `'f'` (4 bytes): Starts at offset 12 (aligned at 4 bytes).
    ''' 
    
    # Padding for 2 bytes between
    decoded_numbers = struct.unpack('iIhfd8s', byte_data)
    big_endian_double = struct.unpack('>d', decoded_numbers[5])[0] # Double in big endian (network byte order)
    # -------------------
    
    # Generating the dict and sending the solution
    challenge_solution = {
        'int': decoded_numbers[0],
        "uint": decoded_numbers[1],
        "short": decoded_numbers[2],
        "float": decoded_numbers[3],
        "double": decoded_numbers[4],
        "big_endian_double": big_endian_double
    }
    return solution_post(challenge_name, token, challenge_solution)

# only executed when the script is run as the main program, and not when it is imported as a module into another script.
if __name__ == "__main__":
    # Token filename
    token_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'token.config')
    token = read_token(token_path)
    main(token)