import cv2

path = '../Images/image_1.jpg'
image = cv2.imread(path)

# Check if the image was successfully loaded
if image is None:
    print("Error loading image")
else:
    # Display the image in a window
    cv2.imshow('Loaded Image', image)

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

