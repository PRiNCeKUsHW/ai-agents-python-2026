import sys
from pathlib import Path

# let the tests import hello.py and check_setup.py from the project folder
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
