import cmd

"""
cmdloop() is the main processing loop of the interpreter.You can
override it, but it is usually not neccessary, since the preloop()
and postloop() hooks are available

Each iteration thru cmdloop() calls onecmd() to dispatch the command to its
processor.

The actual input is parsed with parseline() to create a tuple containing the
command, and the remaining portion of the line

If the line is empty, emptyline() is called.The default implementation runs
the previous command again.If the line contains a command, first precmd()
is called then the processor is looked up and invoked.

If none is found, default() is called instead.Finally postcmd() is called
"""
class Illustrate(cmd.Cmd):
    "Illustrate the base class method use."
    
    def cmdloop(self, intro=None):
        print ('cmdloop(%s)' % intro)
        return cmd.Cmd.cmdloop(self, intro)
    
    def preloop(self):
        print ('preloop()')
    
    def postloop(self):
        print ('postloop()')
        
    def parseline(self, line):
        print ('parseline(%s) =>' % line,)
        ret = cmd.Cmd.parseline(self, line)
        print (ret)
        return ret
    
    def onecmd(self, s):
        print ('onecmd(%s)' % s)
        return cmd.Cmd.onecmd(self, s)

    def emptyline(self):
        print ('emptyline()')
        return cmd.Cmd.emptyline(self)
    
    def default(self, line):
        print ('default(%s)' % line)
        return cmd.Cmd.default(self, line)
    
    def precmd(self, line):
        print ('precmd(%s)' % line)
        return cmd.Cmd.precmd(self, line)
    
    def postcmd(self, stop, line):
        print ('postcmd(%s, %s)' % (stop, line))
        return cmd.Cmd.postcmd(self, stop, line)
    
    def do_greet(self, line):
        print ('hello,', line)

    def do_EOF(self, line):
        "Exit"
        return True

if __name__ == '__main__':
    Illustrate().cmdloop('Illustrating the methods of cmd.Cmd')
