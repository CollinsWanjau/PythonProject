import cmd
import os

class ShellEnabled(cmd.Cmd):

    last_output = ''

    def do_shell(self, line):
        "Run a shell command"
        print("running shell command:",line)

        # the line of code runs a shell command given as the value
        # of the line variable using the `os.open` function and
        # captures the output og the command.

        # The os.open function opens a pipe to or from the command
        # specified by the line and returns a file object, which can
        # be used to read the output of the command.

        # The read method of the file object is then called to read
        # the entire output of the command as a string, which is stored
        # in the output variable.
        output = os.popen(line).read()
        print (output)
        self.last_output = output
    def do_echo(self, line):
        "Print the input, replacing '$out' with the output of the last shell command"
        print (line.replace('$out', self.last_output))

    def do_EOF(self, line):
        return True

if __name__ == "__main__":
    # The cmdloop() runs a loop that continously prompts the user
    # for a command, executes the command, and displays the results.

    # This line of code would start the ShellEnabled command line
    # interface and allow the user to enter and execute commands
    # until the interface is exited
    ShellEnabled().cmdloop()
