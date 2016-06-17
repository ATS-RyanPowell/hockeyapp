__version__ = '0.4.0'

 
import os
import sys
SCRIPTDIR=os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(SCRIPTDIR,'..','requests'))


from .app import Application
from .app import Applications

# Deprecated import mapping
from . import app as apps

from . import cli
from . import crashes
from . import crashlog
