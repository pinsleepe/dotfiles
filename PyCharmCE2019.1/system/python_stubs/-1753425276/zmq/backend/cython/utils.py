# encoding: utf-8
# module zmq.backend.cython.utils
# from /home/mono/anaconda3/envs/twitter/lib/python3.6/site-packages/zmq/backend/cython/utils.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
""" 0MQ utils. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import zmq.error as __zmq_error


# functions

def curve_keypair(*args, **kwargs): # real signature unknown
    """
    generate a Z85 keypair for use with zmq.CURVE security
        
        Requires libzmq (≥ 4.0) to have been built with CURVE support.
        
        .. versionadded:: libzmq-4.0
        .. versionadded:: 14.0
        
        Returns
        -------
        (public, secret) : two bytestrings
            The public and private keypair as 40 byte z85-encoded bytestrings.
    """
    pass

def curve_public(*args, **kwargs): # real signature unknown
    """
    Compute the public key corresponding to a secret key for use
        with zmq.CURVE security
    
        Requires libzmq (≥ 4.2) to have been built with CURVE support.
    
        Parameters
        ----------
        private
            The private key as a 40 byte z85-encoded bytestring
        Returns
        -------
        bytestring
            The public key as a 40 byte z85-encoded bytestring.
    """
    pass

def has(*args, **kwargs): # real signature unknown
    """
    Check for zmq capability by name (e.g. 'ipc', 'curve')
        
        .. versionadded:: libzmq-4.1
        .. versionadded:: 14.1
    """
    pass

def _check_rc(rc, errno=None): # reliably restored by inspect
    """
    internal utility for checking zmq return condition
        
        and raising the appropriate Exception class
    """
    pass

def _check_version(min_version_info, msg=None): # reliably restored by inspect
    """
    Check for libzmq
        
        raises ZMQVersionError if current zmq version is not at least min_version
        
        min_version_info is a tuple of integers, and will be compared against zmq.zmq_version_info().
    """
    pass

# classes

class ZMQError(__zmq_error.ZMQBaseError):
    """
    Wrap an errno style error.
    
        Parameters
        ----------
        errno : int
            The ZMQ errno or None.  If None, then ``zmq_errno()`` is called and
            used.
        msg : string
            Description of the error or None.
    """
    def __init__(self, errno=None, msg=None): # reliably restored by inspect
        """
        Wrap an errno style error.
        
                Parameters
                ----------
                errno : int
                    The ZMQ errno or None.  If None, then ``zmq_errno()`` is called and
                    used.
                msg : string
                    Description of the error or None.
        """
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    errno = None


# variables with complex values

__all__ = [
    'has',
    'curve_keypair',
    'curve_public',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f775b0e0a20>'

__spec__ = None # (!) real value is "ModuleSpec(name='zmq.backend.cython.utils', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f775b0e0a20>, origin='/home/mono/anaconda3/envs/twitter/lib/python3.6/site-packages/zmq/backend/cython/utils.cpython-36m-x86_64-linux-gnu.so')"

__test__ = {}

