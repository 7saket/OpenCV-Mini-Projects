#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2

# Get the webcam
cap = cv2.VideoCapture(0)

while True:
    # Step 1: Capture the frame
    _, frame = cap.read()

    # Step 2: Show the frame with blurred background
    cv2.imshow("Webcam", frame)
    # If q is pressed terminate
    if cv2.waitKey(1) == ord('q'):
        break

# Release and destroy all windows
cap.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




