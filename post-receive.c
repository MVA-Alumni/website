#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
     setuid( 0 );
     system( "/srv/git/mvaalumni.git/hooks/post-receive-script" );

     return 0;
}
