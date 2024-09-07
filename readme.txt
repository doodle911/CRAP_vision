cropBoard - takes camera feed and finds the board and straightens it 
detection - detects pieces on board and their location, outputs findings
stream - sets up virtual webcam of cropped video feed to pass into video_reference for detection
view - script to view virtual feed
server - sets up flask server to receive chessboard data
serverTestScript - test data to send to Flask server (Won't work as its only got 8 squares)

Run stream, detection and server at the same time!