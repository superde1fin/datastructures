from setuptools import setup
import os

def get_subdirectories(path):
	return [item for item in os.listdir(path) if (os.path.isdir(item) and item != "build" and item != "datastructs.egg-info" and item != "dist")]

def run_setup():
	setup(name = os.getcwd().split('/')[-1], packages = get_subdirectories('.'))

if __name__ == "__main__":
	run_setup()
