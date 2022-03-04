use strict;
use warnings;

# https://superuser.com/questions/903168/how-should-i-write-a-regex-to-match-a-specific-word
# CHECK BELOW LINK FOR THIS: \W*(rocket)\W*  FLAGS -> G M I in regex101 -> match word in any form
#  check \b if you need the word only https://stackoverflow.com/questions/6664151/difference-between-b-and-b-in-regex

# turn off output buffering -> seeing stuff that we print immediately
$| = 1;

sub main {
    my $file_path =
'/home/antoan/GitHub/SoftUni-Education/Perl/Learn Perl 5 By Doing It/wildcards_in_regular_expressions/text.txt';

    open( my $FH, $file_path ) or die "File didn't open: $file_path.\n";
    print "\nThese are\ntwo lines.";
    while ( my $line = <$FH> ) {
        if ( $line =~ / h.s / ) {
            print $line;
        }
    }

    close($FH) or die "File didn't close: $file_path.\n";
}

main();
