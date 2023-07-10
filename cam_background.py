from collections import namedtuple
from pathlib import Path

import cv2

import numpy as np
import torch
from IPython.display import HTML, FileLink, display
from model import U2NET, U2NETP
from openvino.runtime import Core
from openvino.tools import mo


model_ir = mo.convert_model(
    "u2net.onnx",
    mean_values=[123.675, 116.28 , 103.53],
    scale_values=[58.395, 57.12 , 57.375],
    compress_to_fp16=True
)



# Load the network to OpenVINO Runtime.
ie = Core()
compiled_model_ir = ie.compile_model(model=model_ir, device_name="CPU")
# Get the names of input and output layers.
input_layer_ir = compiled_model_ir.input(0)
output_layer_ir = compiled_model_ir.output(0)


# Get the input and output layer names
input_layer = 'input.1'
output_layer = '1875'


# Open the video capture
cap = cv2.VideoCapture(1)  # Use the default camera (change to the appropriate index if necessary)

while True:
    # Read a frame from the video feed

    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess the frame
    resized_frame = cv2.resize(src=frame, dsize=(512, 512))
    input_frame = np.expand_dims(np.transpose(resized_frame, (2, 0, 1)), 0)
    bg_removed_result = compiled_model_ir([input_frame])[output_layer_ir]

    # Resize the network result to the frame shape and round the values
    resized_result = np.rint(cv2.resize(src=np.squeeze(bg_removed_result), dsize=(frame.shape[1], frame.shape[0]))).astype(np.uint8)

    # Create a copy of the frame and set all background values to 255 (white)
    bg_removed_result = frame.copy()
    bg_removed_result[resized_result == 0] = 255

    # Display the original frame and the frame with the background removed
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Background Removed Frame", bg_removed_result)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()