use strict;
use warnings;

# turn off output buffering -> seeing stuff that we print immediately
$| = 1;

sub main {
    my $file_path =
'/home/antoan/GitHub/SoftUni-Education/Perl/Learn Perl 5 By Doing It/wildcards_in_regular_expressions/text.txt';

    open( my $FH, $file_path ) or die "File didn't open: $file_path.\n";

    while ( my $line = <$FH> ) {
        if ( $line =~ /\b(([lL][A-Za-z]{5,})...)/ ) {

            # $1 is the group that is matched. group 1 check in regex101.
            # $2 is the group that is matched. group 2 check in regex101.
            # $1,2,3, 4 ... are the groups
            print "$1\n";
            print "$2\n";
        }
    }

    close($FH) or die "File didn't close: $file_path.\n";
}

main();
