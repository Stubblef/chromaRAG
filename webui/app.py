import subprocess
import os
import argparse

# streamlit run app.py --server.port 8000 

class App:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--save_path", default="./data/persist", help="Path to save the data")
        self.parser.add_argument("--port", default=8000, help="Port to run the server")
        self.args = self.parser.parse_args()
        self.save_path = self.args.save_path
        os.makedirs(self.save_path, exist_ok=True)
        self.port = self.args.port

    def run(self):
        print("Starting the server")
        cmd = f"streamlit run app.py --server.port {self.port}"
        subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    app = App()
    app.run()

    