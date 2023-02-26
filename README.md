Handwriting Recognition AI
This project is a handwriting recognition AI that uses a convolutional neural network (CNN), recurrent neural network (RNN), and connectionist temporal classification (CTC) to recognize handwritten text. The AI is trained using the Hackthon program, and the trained model is deployed in the Hackthon_v0.5 mobile app.

The Hackthon program contains the code for training the handwriting recognition AI. It takes in a dataset of handwritten text and trains the AI using a combination of a CNN, RNN, and CTC. The program uses TensorFlow as its deep learning framework.

To use the Hackthon program, follow these steps:
1. Install the necessary dependencies by running pip install -r requirements.txt.
2. Prepare your dataset. The dataset should be manually downloaded via https://fki.tic.heia-fr.ch/databases/iam-handwriting-database
3. Go to the src directory and execute python main.py --mode train --data_dir path/to/IAM

The Hackthon_v0.5 mobile app is an unpackaged app that allows users to input handwritten text and receive its recognized text output. The app uses the trained model from the Hackthon program to recognize the text.

To use the Hackthon_v0.5 mobile app, follow these steps:

1. Launch the app using a python interpreter to run main.py
2. Input your handwritten text using the upload feature
3. The recognized text will be displayed on the screen to copy and paste

Optional decoder
Hackthon_v0.5 also includes an optional decoder called WordBeamSearch for improved text recognition accuracy. To use this decoder, follow these additional steps:

1. Locate to the hackthon_v0.5/CTCWordBeamSearch-master directory.
2. Run pip install . to install the decoder.
3. Specify the command line option --decoder wordbeamsearch when executing main.py to actually use the decoder

Credits
This project was created by Toan Nham and Minh Nguyen with the help of Vannesa Vo as project manager and Mia Ho as tester. The AI model was trained using the TensorFlow deep learning framework and IAM line datasets. The Hackthon program and Hackthon_v0.5 mobile app were both written in Python. The WordBeamSearch decoder was developed by Harold Scheidl and is available under the MIT license.
