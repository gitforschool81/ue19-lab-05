Joke App with a Public API

This project is a simple script that fetches a random joke from a public API and prints it to the console.

🚀 How to Install and Run the Project

You have two options to run this project.

Option 1: Run Natively with Python

This method runs the script directly on your machine.

Clone the repository:

git clone https://github.com/gitforschool81/ue19-lab-05.git
cd ue19-lab-05
pip install requests
(Note: It's highly recommended to do this inside a virtual environment.)
python3 app.py

Option 2: Run with Docker

This method uses the included Dockerfile to build and run the app in an isolated container.

Clone the repository:

git clone https://github.com/gitforschool81/ue19-lab-05.git
cd ue19-lab-05
docker build -t mon-app-joke .
docker run --rm mon-app-joke

📜 Example Output

You will see a different joke each time you run it:
Plaintext

Here's your joke:
Setup: Why are pirates called pirates?
Punchline: Because they arrr!
