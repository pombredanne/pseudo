class PseudonError(Exception):
    pass

class PseudonStandardLibraryError(PseudonError):
    pass

class PseudonDSLError(PseudonError):
    pass