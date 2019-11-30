# pylint: disable-msg = disable-msg = wildcard-import, unused-wildcard-import

from .base import Backend
from .backend import *

# Tensorflow
def load_tensorflow():
    """
    Internal function to register the TensorFlow backend.
    This function is called automatically once a TFSimulation is instantiated.

    :return: True if TensorFlow could be imported, else False
    """
    try:
        from .tensorflow_backend import TFBackend
        for b in backend.backends:
            if isinstance(b, TFBackend): 
                return True
        backend.backends.append(TFBackend())
        return True
    except BaseException as e:
        import logging
        logging.fatal("Failed to load TensorFlow backend. Error: %s" % e)
        print("Failed to load TensorFlow backend. Error: %s" % e)
        return False


load_tensorflow()

# overwrite with other functions
from .nd import *
from .initializers import *  # this replaces zeros_like (possibly more) and must be handled carefully
