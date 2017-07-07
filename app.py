""" This example uses docopt with the built in cmd module to demonstrate an

interactive command application.

Usage:

     main.py skills_completed <username>

Options:

    -i, --interactive  Interactive Mode

    -h, --help  Show this screen and exit.



"""

import sys
import cmd
from docopt import docopt, DocoptExit
from src.main import User



def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match
            # We print a message to the user and the usage block
            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def intro():

    print(__doc__)


class DojoCLI(cmd.Cmd):
    intro = "Welcome to my interactive program type help for a list of commands!"
    prompt = '(dojo) '

    file = None

    """ method to display the skills studied """
    @docopt_cmd
    def do_skills_completed(self, arg):
        """Usage: skills_completed <username> """
        username = arg['<username>']
        user     = User(username)
        user.view_completd_skills()  
            
    def do_quit(self, arg):

        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

DojoCLI().cmdloop()


#print(opt)
