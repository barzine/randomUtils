#!/usr/local/bin/perl
# err... forgot from whom the inial script was (sorry) 

#define function
sub strip {
        my$string= $_[0];
        $string =~ s/^\s+|\s+$//g ;
        return($string);
}

my$numArgs = $#ARGV + 1;
if($numArgs==0){
        print "\nUsage lstrip.pl file1 [file2 .. fileN]\n\n bye bye\n\n";
        exit;
}
foreach $argnum (0 .. $#ARGV) {
        if( -e $ARGV[$argnum]){
                print "stripping left spaces of $ARGV[$argnum]:";
                open(TOCLEAN,$ARGV[$argnum]) or die "cannot open file!";
                open(my $new,'>',"$ARGV[$argnum]_cleaned") or die "Cannot create new file!";
                while(my$line=<TOCLEAN>){
                        my$string=strip($line);
                        print $new "$string\n";
                }
                close(TOCLEAN);
                close(NEW);
                print " done\n\n";
        }else{
                print "file: $ARGV[$argnum] not found\n";
        }
}
exit;
