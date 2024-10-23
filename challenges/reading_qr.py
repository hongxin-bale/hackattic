from utils.hackattic import image_request, data_request, read_token, solution_post
import cv2
from pyzbar.pyzbar import decode
from os import remove


def main(token):
    # Name of challenge
    challenge_name = "reading_qr"
    
    # Data of the challenge to a dict/json
    challenge_dict = data_request(challenge_name, token)
    
    # Get image and save path to challenge_image
    challenge_image = image_request(challenge_dict["image_url"], "qr_image.png")

    # -----Solution------
    decodeQR = decode(cv2.imread(challenge_image))
    qrdata = decodeQR[0].data.decode()
    # -------------------
    
    # Remove the image
    remove(challenge_image)
    
    # Generating the dict and sending the solution
    challenge_solution = {}
    challenge_solution['code'] = qrdata

    return solution_post(challenge_name, token, challenge_solution)

# only executed when the script is run as the main program, and not when it is imported as a module into another script.
if __name__ == "__main__":
    # Token filename
    token = read_token("token.config")
    main(token)