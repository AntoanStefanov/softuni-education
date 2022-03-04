use strict;
use warnings;

# https://superuser.com/questions/903168/how-should-i-write-a-regex-to-match-a-specific-word
# \W*(rocket)\W*  FLAGS -> G M I in regex101 -> match word in any form

# turn off output buffering -> seeing stuff that we print immediately
$| = 1;

sub main {

#   FH -> FileHandle- The reference to the file, that can be used within the program or until its closure.

    my $file_path =
'/home/antoan/GitHub/SoftUni-Education/Perl/Learn Perl 5 By Doing It/reading_files_and_regular_expressions/employees.txt';

    # open file
    open( my $FH_READ, $file_path ) or die "File didn't open: $file_path.\n";

    my $output_file = 'output.txt';

    # https://www.perltutorial.org/perl-open-file/
    # '>', $output_file is like '>'.$output_file which means '>output.txt',
    #  you could write '>output.txt' in $output_file variable, but that's ugly.
    open( my $FH_WRITE, '>', $output_file )
      or die "Can't create '$output_file'.\n";

    # die; -> quit program
    # \n at the end so thhat "at main.pl line 18." doesn't output at the end.
    # die "File didn't open: $file_path.\n";

    # https://www.perltutorial.org/perl-open-file/
    # <FH> -> reads one line from the file., while file returns line, do it .
    while ( my $line = <$FH_READ> ) {

        # https://stackoverflow.com/questions/10019049/what-does-do-in-perl
        if ( $line =~ /Programmer/ ) {

#           replacement
#           /Sally{replace this}/Tisho{with this}/{PLACE FOR FLAGS} ex. /Sally/Tisho/ig (i -> case insensitive, g -> replace all occurences of Sally)
            $line =~ s/sally/Tisho/i;
            print $FH_WRITE $line;
        }
    }

    close($FH_READ);
    close($FH_WRITE);

# give file a relative name, which will be the working directory of this program.

    # between open/close , manipulate file.
    # NO , BETWEEN FH AND WHAT YOU WANT IT THE FILE.
    # print $FH "Hello.\n";

}

main();
