import requests

# The URL of the API endpoint
url = 'http://localhost:8000/api/'

# Path to the image file you want to test
image_path = 'tests/thumb_up.jpg'

# Open the image file in binary mode
with open(image_path, 'rb') as image_file:
    # Create a dictionary to store the image file
    files = {'image': image_file}
    
    # Make the POST request to the API endpoint
    response = requests.post(url, files=files)

    # Print the response from the server
    print(response.status_code)
    print(response.text)