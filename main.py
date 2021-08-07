from fastapi import FastAPI, Depends
from fastapi_cloudauth.firebase import FirebaseCurrentUser, FirebaseClaims
from fastapi.middleware.cors import CORSMiddleware
import os
import pyAesCrypt

# get credential file
cwd = os.getcwd()
password = os.environ['fast_api_password']
encrypted_file_path = "{}/credentials/credentials.json.aes".format(cwd)
decrypted_file_path = "{}/credentials/credentials.json".format(cwd)
print("password",password)

pyAesCrypt.decryptFile(encrypted_file_path,
                       decrypted_file_path, password)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = decrypted_file_path

app = FastAPI()
origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
)

get_current_user = FirebaseCurrentUser(
    project_id="fastevent-fec5c"
)


@app.get("/user/")
def get_user(current_user: FirebaseClaims = Depends(get_current_user)):
    """An api to get current user data

    Args:
        Valid ID Token

    Returns:
        A json response containing the user id of the current user
    """
    # ID token is valid and getting user info from ID token
    return {"id": current_user.user_id}
