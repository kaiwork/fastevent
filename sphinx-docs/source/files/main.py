from fastapi import FastAPI, Depends
from fastapi_cloudauth.firebase import FirebaseCurrentUser, FirebaseClaims
from fastapi.middleware.cors import CORSMiddleware


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
