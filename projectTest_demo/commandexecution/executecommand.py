import subprocess
import os
import shlex
from subprocess import Popen, PIPE
import logging
from loggerpackage import customLogger as cl

def commandExecutionCygwin2(command):
    """
    :param command: pass the command line statement
    :return: returns the output of command being supplied
    """
    log = cl.custom_logger(logging.DEBUG)

    try:
        log.info( "executing command...." )
        print(command)

        with Popen([r'C:\cygwin64\bin\bash.exe'], stdin=PIPE, stdout=PIPE, shell=True) as p:
            p.stdin.write(command.encode())
            p.stdin.close()
            out = p.stdout
            output = out.read().splitlines()

    except:
        output = ""
        print("error :"+str(p.stderr.errors))
        log.error("error with executing command..")
    finally:
        p.terminate()
        p.kill()
        subprocess._cleanup()
    return output

def commandExecutionCygwin(command):
    """
    :param command: pass the command line statement
    :return: returns the output of command being supplied
    """
    log = cl.custom_logger(logging.DEBUG)

    try:
        log.info( "executing command...." )
        print(command)
        cmd = [r'C:\cygwin64\bin\bash.exe', '-c', '-l', command]
        output = (subprocess.check_output(cmd, shell=True).decode()).splitlines()

    except subprocess.CalledProcessError as e:
        output = e.output
        log.error("error with executing command..")
    finally:
        subprocess._cleanup()
    return output


def commandExecution(command):
    """
    :param command: pass the command line statement
    :return: returns the output of command being supplied
    """
    log = cl.custom_logger(logging.DEBUG)

    try:
        log.info( "executing command...." )
        output = subprocess.check_output(command, shell=True).decode()
    except subprocess.CalledProcessError as e:
        output = e.output
        log.error("error with executing command..")
    return output


def sortingCmd(fileToBeRead, *args):
    """
    :param fileToBeRead: file to be read
    :param args: specific command for sortingCmd
    :return: returns the sorted output
    """

    arguments = ""
    log = cl.custom_logger( logging.DEBUG )

    for arg in args:
        arguments = arguments + " " + arg

    command = "sort "+arguments + " " + fileToBeRead

    log.info("executing sorting command: "+command)
    # output = commandExecution(command)
    output = commandExecutionCygwin( command )

    return output
