from logging import degub, info, warning, error, critical

class ILog:
    def __init__(self, message):
        self.Message = message

    def __str__(self):
        if self.Message == "":
            raise Exception("log message is empty")
        return self.Message

    def LogData(self):
        ConfigLog(DEBUG):
        degub(self.Message)
        info(self.Message)
        warning(self.Message)
        error(self.Message)
        critical(self.Message)

    def ConfigLog(self, level=DEBUG):
        basicConfig(level=level)
