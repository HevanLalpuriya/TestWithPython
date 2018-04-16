import inspect
import logging


def custom_logger(logLevel):
    """

    :param logLevel:
    :return:
    """

    logfilename = "testlogs.log"
    logformat = "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
    dateformat = "%m/%d/%Y %I:%M:%S %p"

    # Get the class or method name from where this method is being called
    logger = logging.getLogger( inspect.stack()[1][3] )

    # By setting it to DEBUG it logs all messages
    logger.setLevel( logging.DEBUG )

    # name of the log file and mode
    filehandler = logging.FileHandler( logfilename) #, mode='w' )

    # over riding log level
    filehandler.setLevel( logLevel )

    # formatting the logs
    formatter = logging.Formatter( logformat, datefmt=dateformat)
    filehandler.setFormatter( formatter )

    logger.addHandler( filehandler )

    return logger
