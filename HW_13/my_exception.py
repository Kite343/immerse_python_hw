class BaseException(Exception):
    def __init__(self):
        pass
    def __str__(self):
        pass

class SizeException(BaseException):
    def __init__(self, size):
        self.size = size
    def __str__(self):
        return f"the size cannot be <= 0, your value {self.size} "
    
class MissingFolderException(BaseException):
    def __init__(self, folder):
        self.folder = folder
    def __str__(self):
        return f"folder {self.folder} missing "
    
