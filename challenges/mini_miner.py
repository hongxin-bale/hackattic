from utils.hackattic import data_request, read_token, solution_post
import os

def main(token):
    # Name of challenge
    challenge_name = "mini_miner"
    
    # Data of the challenge to a dict/json
    challenge_dict = data_request(challenge_name, token)

    # -----Solution------
    
    # -------------------
    
    # Generating the dict and sending the solution
    challenge_solution = {
    }
    #return solution_post(challenge_name, token, challenge_solution)

# only executed when the script is run as the main program, and not when it is imported as a module into another script.
if __name__ == "__main__":
    # Token filename
    token_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'token.config')
    token = read_token(token_path)
    main(token)