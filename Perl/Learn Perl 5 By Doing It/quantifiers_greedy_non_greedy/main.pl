use strict;
use warnings;

# turn off output buffering -> seeing stuff that we print immediately
$| = 1;

sub main {
    my $file_path =
'/home/antoan/GitHub/SoftUni-Education/Perl/Learn Perl 5 By Doing It/wildcards_in_regular_expressions/text.txt';

    open( my $FH, $file_path ) or die "File didn't open: $file_path.\n";

    while ( my $line = <$FH> ) {
        if ( $line =~ /(s.*?n)/ ) {
            print $1, "\n";
            if ($2) {
                print 'asd';
            }
        }
    }

    close($FH) or die "File didn't close: $file_path.\n";
}

main();
