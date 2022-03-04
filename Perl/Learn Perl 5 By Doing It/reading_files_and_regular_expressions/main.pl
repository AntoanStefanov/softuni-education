use strict;
use warnings;

# https://superuser.com/questions/903168/how-should-i-write-a-regex-to-match-a-specific-word
# \W*(rocket)\W*  FLAGS -> G M I in regex101 -> match word in any form 

# turn off output buffering
$| = 1;

sub main {

# use single quotes when we talk about literal string, nothing in needs to be interpreted as special sequence.
# \t -> is just \t not tab in single quotes('')
    my $file_path =
'/home/antoan/GitHub/SoftUni-Education/Perl/Learn Perl 5 By Doing It/reading_files_and_regular_expressions/employees.txt';

    # open file
    open( FH, $file_path ) or die "File didn't open: $file_path.\n";

    # die; -> quit program
    # \n at the end so thhat "at main.pl line 18." doesn't output at the end.
    # die "File didn't open: $file_path.\n";

    # https://www.perltutorial.org/perl-open-file/
    # <FH> -> reads one line from the file., while file returns line, do it .
    while ( my $line = <FH> ) {
        # https://stackoverflow.com/questions/10019049/what-does-do-in-perl
        if ( $line =~ /Programmer/ ) {
            print $line;
        }
    }

    close(FH);
}

main();
