import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2

def translate(*gestures) -> list[str]:
    """
    Translates model responses to English text
    """
    # Define a dictionary for translation
    dictionary = {
        "Thumb_Up": "good",
        "Thumb_Down": "bad",
        "Closed_Fist": "friend",
        "Victory": "victory",
        "Pointing_Up": "look up",
        "Open_Palm": "hello",
        "ILoveYou": "i love you"
    }
    # Initialize a list for translated strings
    result = []

    # Loop through the model response and translate it according to the dictionary
    for i in gestures:
        result.append(dictionary[i])

    return result

def gesture(frame_path: str) -> list[str]:
    # Settings for model
    base_options = python.BaseOptions(model_asset_path='gesture_recognizer.task')
    options = vision.GestureRecognizerOptions(base_options=base_options)
    recognizer = vision.GestureRecognizer.create_from_options(options)

    mp_image = mp.Image.create_from_file(frame_path)
    gesture_result = recognizer.recognize(mp_image)

    if gesture_result.gestures:
        if gesture_result.gestures[0][0].category_name != "None":
            return translate(gesture_result.gestures[0][0].category_name)
    return ["No gesture detected"]