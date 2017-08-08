import cmd


class BaseInterpreter(cmd.Cmd):
    """
    This class acts as superclass for all interpreters and
    defines common function(s) which must be present in every
    interpreter.
    """
    def do_exit(self, *args):
        """
        Use to exit from current interpreter. Ctrl + D (EOF) can also
        be used.
        """
        print("Goodbye")
        return True

    do_EOF = do_exit
