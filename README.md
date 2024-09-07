# C.R.A.P Computer Vision

C.R.A.P Computer Vision is a toolkit designed to enhance interactions with chess games through computer vision techniques. The project includes several modules, each handling a specific aspect of the process from capturing the chessboard to processing and streaming the data.

## Modules

- **cropBoard**: Captures camera feed, finds the chessboard, and straightens the image for further processing.
- **detection**: Detects chess pieces on the board, determines their locations, and outputs the findings.
- **stream**: Sets up a virtual webcam to stream the cropped video feed, which can be used as input for the detection module.
- **view**: Contains scripts to view the virtual video feed.
- **server**: Establishes a Flask server to receive and process chessboard data from the detection module.
- **serverTestScript**: Includes test data to send to the Flask server. Note: This script only includes data for 8 squares and won't work fully.

## Running the Project

To get the full functionality of the C.R.A.P Computer Vision system, run the `stream`, `detection`, and `server` modules simultaneously. This setup allows for real-time capturing, processing, and streaming of chess game data.



