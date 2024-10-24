from utils.hackattic import data_request, read_token, solution_post
import os
import json
import hashlib

def main(token):
    # Name of challenge
    challenge_name = "mini_miner"
    
    # Data of the challenge to a dict/json
    challenge_dict = data_request(challenge_name, token)

    # -----Solution------
    # Parse JSON
    block = challenge_dict["block"]
    difficulty = challenge_dict["difficulty"]
    
    # Convert difficulty into a target prefix of "zero_bits"
    # Four bits per hex digit, a hex is "16" at max which is "1111" in binary
    zero_bits = '0' * (difficulty // 4)
    extra_bits = difficulty % 4
        
    # Find nonce
    nonce = 0
    while True:
        block['nonce'] = nonce
        block_string = json.dumps(block, separators=(',', ':'), sort_keys=True)
        hash_result = hashlib.sha256(block_string.encode('utf-8')).hexdigest()
        check_digit_binary = int(hash_result[len(zero_bits)], 16)
        if hash_result.startswith(zero_bits) and (extra_bits == 0 or (check_digit_binary >> extra_bits) == 0):
            break
        nonce += 1
    # -------------------
    
    # Generating the dict and sending the solution
    challenge_solution = {
        "nonce": nonce
    }
    return solution_post(challenge_name, token, challenge_solution)

# only executed when the script is run as the main program, and not when it is imported as a module into another script.
if __name__ == "__main__":
    # Token filename
    token_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'token.config')
    token = read_token(token_path)
    main(token)