import os, logging
from loggerpackage import customLogger as cl
from Helpers import helpermethods


def sortFileContent(file, keyvalue, reverseorder):
    """

    :param file: filename
    :param keyvalue:
    :param reverseorder: boolean , True or False
    :return:
    """

    log = cl.custom_logger( logging.DEBUG )
    filecontent = readFileContent(file)
    filecontent = helpermethods.removespace(filecontent)

    log.debug("python sorting started...")
    response = sorted(filecontent, key=keyvalue, reverse=reverseorder)
    log.debug("python sorting completed...")

    return response


def sortFileContentUnique(file, keyvalue, reverseorder):
    """
    :param file: filename
    :param keyvalue:
    :param reverseorder: boolean , True or False
    :return:
    """

    log = cl.custom_logger( logging.DEBUG )
    filecontent = readFileContent( file )

    log.debug("python sorting started...")
    response = sorted(set(filecontent), key=keyvalue, reverse=reverseorder)
    log.debug("python sorting completed...")

    return response

def readFileContent(file):
    """

    :param file: FileName
    :return: file content as a list
    """

    log = cl.custom_logger( logging.DEBUG )
    filecontent = ""

    if os.path.exists( file ):

        try:
            log.info("reading the file...")
            fileobj = open( file, "r")
            filecontent = fileobj.read().splitlines()
        except IOError:
            log.error("error while reading the file: "+file)
        finally:
            log.info("closing the file...")
            fileobj.close()
    else:
        log.error("file does not exist...")
    return filecontent
