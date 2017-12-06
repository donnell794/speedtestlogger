
class Logger(object):
    def __init__(self, type, config):
        if type == 'csv':
            self.logger = CsvLogger(config['filename'])

    def log(self, logItems):
        self.logger.log(logItems)

    def datelog(self, logItem):
        self.logger.datelog(logItem)

class CsvLogger(object):
    def __init__(self, filename):
        self.filename = filename

    def log(self, logItems):
        with open(self.filename, "a") as logfile:
            logfile.write("%s\n" % ','.join(logItems))

    def datelog(self, logItem):
        with open(self.filename, "a") as logfile:
            logfile.write("\n" + logItem + "\n")