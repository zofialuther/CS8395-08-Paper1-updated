```python
import numpy as np
import cv2

# Create a black image
image = np.zeros((512,512), dtype=np.uint8)

# Generate XOR pattern
for i in range(512):
    for j in range(512):
        image[i,j] = i ^ j

# Display the image in a window
cv2.imshow('XOR Pattern', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```