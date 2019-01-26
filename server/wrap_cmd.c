#define _GNU_SOURCE         /* See feature_test_macros(7) */
#include <sys/types.h>

#include <unistd.h>

#include <errno.h>
#include <stdio.h>

int main( int argc, char * argv[], char ** envp )
{
    if (argc < 1) {
        return 1;
    }
    
    argv[0] = SCRIPTPATH;
    
    int ouid = getuid();
    
    int ogid = getgid();
    
    int oeuid = geteuid();
    
    int oegid = getegid();
    
    char buffer[50];
    sprintf(buffer, "ouid=%i", ouid);
    
    char *strings[] = {buffer, NULL};
    
    

    
    setresuid(oeuid, oeuid, ouid);
    
    setresgid(oegid, oegid, ouid);
    
    //printf("errno: %i\n", );
    
    
    
    envp = 0; /* blocks IFS attack on non-bash shells */
    execve( SCRIPTPATH, argv, strings );
    return 0;
}
