import cv2
import mediapipe as mp

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
        "Open_Palm": "Hello",
        "ILoveYou": "I love you"
    }
    # Initialize a list for translated strings
    result = []

    # Loop through the model response and translate it according to the dictionary
    for i in gestures:
        result.append(dictionary[i])

    return result

def gesture(video_path: str) -> list[str]:
    """
    Recognizes gestures from a video input
    """
    # Settings for model
    BaseOptions = mp.tasks.BaseOptions
    GestureRecognizer = mp.tasks.vision.GestureRecognizer
    GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
    VisionRunningMode = mp.tasks.vision.RunningMode

    # Get video from path
    video = cv2.VideoCapture(video_path)
    # Get FPS of a video
    fps = video.get(cv2.CAP_PROP_FPS)

    # A list which will contain recognized gestures
    results = []

    # Create a gesture recognizer instance with the video mode:
    options = GestureRecognizerOptions(
        base_options=BaseOptions(model_asset_path='gesture_recognizer.task'),
        running_mode=VisionRunningMode.VIDEO)

    # A string to compare results
    previous_res = ""
    with GestureRecognizer.create_from_options(options) as recognizer:
        # Read the video frame by frame
        while(video.isOpened()):
            ret, frame = video.read()
            if ret == True:
                frame_number = video.get(cv2.CAP_PROP_POS_FRAMES) # get current frame's number
                timestamp = int(frame_number / fps * 1_000_000) # get timestamp of the current frame in ms
            
                mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame) # convert image for a model
                gesture_result = recognizer.recognize_for_video(mp_image, timestamp) # model response object
                
                # if there are gestures recognized in a frame and it is not equal to the previous result,
                if gesture_result.gestures:
                    if (
                        gesture_result.gestures[0][0].category_name != previous_res
                        and gesture_result.gestures[0][0].category_name != "None"
                        ):
                        previous_res = gesture_result.gestures[0][0].category_name # set the previous to the current result
                        results.append(previous_res) # include the gesture result to the results list
        
            # Break the loop
            else: 
                break

    video.release() # close connection with the video
    results = translate(*results) # translate model response to English text
    return results