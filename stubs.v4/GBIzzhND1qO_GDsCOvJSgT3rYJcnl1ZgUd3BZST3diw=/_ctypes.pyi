import builtins as _mod_builtins

PyCFuncPtr = PyCFuncPtrType
class ArgumentError(_mod_builtins.Exception):
    __class__ = ArgumentError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'ctypes'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class Array(_CData):
    'XXX to be provided'
    __class__ = Array
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        'XXX to be provided'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

CFuncPtr = PyCFuncPtr
class COMError(_mod_builtins.Exception):
    'Raised when a COM method call failed.'
    __class__ = COMError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Raised when a COM method call failed.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

def CopyComPointer(src, dst):
    'CopyComPointer(src, dst) -> HRESULT value\n'
    pass

FUNCFLAG_CDECL = 1
FUNCFLAG_HRESULT = 2
FUNCFLAG_PYTHONAPI = 4
FUNCFLAG_STDCALL = 0
FUNCFLAG_USE_ERRNO = 8
FUNCFLAG_USE_LASTERROR = 16
def FormatError(integer=None):
    'FormatError([integer]) -> string\n\nConvert a win32 error code into a string. If the error code is not\ngiven, the return value of a call to GetLastError() is used.\n'
    return ''

def FreeLibrary(handle):
    'FreeLibrary(handle) -> void\n\nFree the handle of an executable previously loaded by LoadLibrary.\n'
    pass

def LoadLibrary(name, load_flags):
    'LoadLibrary(name, load_flags) -> handle\n\nLoad an executable (usually a DLL), and return a handle to it.\nThe handle may be used to locate exported functions in this\nmodule. load_flags are as defined for LoadLibraryEx in the\nWindows API.\n'
    pass

def POINTER():
    pass

def PyObj_FromPtr():
    pass

def Py_DECREF():
    pass

def Py_INCREF():
    pass

RTLD_GLOBAL = 0
RTLD_LOCAL = 0
class Structure(_CData):
    'Structure base class'
    __class__ = Structure
    def __init__(self, *args, **kwargs):
        'Structure base class'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class Union(_CData):
    'Union base class'
    __class__ = Union
    def __init__(self, *args, **kwargs):
        'Union base class'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class _Pointer(_CData):
    'XXX to be provided'
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = _Pointer
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self, *args, **kwargs):
        'XXX to be provided'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def contents(self):
        'the object this pointer points to (read-write)'
        pass
    

class _SimpleCData(_CData):
    'XXX to be provided'
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = _SimpleCData
    def __ctypes_from_outparam__(self):
        pass
    
    def __init__(self, *args, **kwargs):
        'XXX to be provided'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def value(self):
        'current value'
        pass
    

__doc__ = 'Create and manipulate C compatible data types in Python.'
__file__ = 'c:\\python38\\dlls\\_ctypes.pyd'
__name__ = '_ctypes'
__package__ = ''
__version__ = '1.1.0'
_cast_addr = 140706447607132
def _check_HRESULT():
    pass

_memmove_addr = 140707091827280
_memset_addr = 140707091828400
_pointer_type_cache = _mod_builtins.dict()
_string_at_addr = 140706447607908
def _unpickle():
    pass

_wstring_at_addr = 140706447607940
def addressof(Cinstance):
    'addressof(C instance) -> integer\nReturn the address of the C instance internal buffer'
    return 1

def alignment(Cinstance):
    'alignment(C type) -> integer\nalignment(C instance) -> integer\nReturn the alignment requirements of a C instance'
    return 1

def buffer_info():
    'Return buffer interface information'
    pass

def byref(Cinstance, offset=0):
    'byref(C instance[, offset=0]) -> byref-object\nReturn a pointer lookalike to a C instance, only usable\nas function argument'
    pass

def call_cdeclfunction():
    pass

def call_function():
    pass

def get_errno():
    pass

def get_last_error():
    pass

def pointer():
    pass

def resize():
    'Resize the memory buffer of a ctypes instance'
    pass

def set_errno():
    pass

def set_last_error():
    pass

def sizeof(Cinstance):
    'sizeof(C type) -> integer\nsizeof(C instance) -> integer\nReturn the size in bytes of a C instance'
    return 1

