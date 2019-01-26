from os import pipe, close, read, _exit, write, dup, fork, waitpid, system

def popen(cmd, wait=True):
    import builtins
    stdout_i, stdout_o = pipe()
    stderr_i, stderr_o = pipe()
    pid = fork()
    if not pid:
        close(1)
        close(2)
        close(stdout_i)
        close(stderr_i)
        dup(stdout_o)
        dup(stderr_o)
        close(0)
        close(stdout_o)
        close(stderr_o)
        s = system(cmd)
        if s > 255:
            s = 255
        _exit(s)
    else:
        close(stdout_o)
        close(stderr_o)
        if wait:
            rcode = waitpid(pid, 0)[1]
        else:
            rcode = pid
        return rcode, builtins.open(stdout_i, 'r'), builtins.open(stderr_i, 'r')

