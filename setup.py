from setuptools import setup
import os

def get_subdirectories(path):
	return [item for item in os.listdir(path) if os.path.isdir(item) and not (item in ("build", "datastructs.egg-info", "dist", ".git"))]

def run_setup():
	setup(name = os.getcwd().split('/')[-1], packages = get_subdirectories('.'))

if __name__ == "__main__":
	run_setup()
