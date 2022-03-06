use strict;
use warnings;

# turn off output buffering -> seeing stuff that we print immediately
$| = 1;

sub main {
    my $text    = 'I am 117 years old tomorrow.';
    # Get all matches, below line. 
    # https://stackoverflow.com/questions/1723440/how-can-i-find-all-matches-to-a-regular-expression-in-perl
    my @matches = $text =~ /\d*/g;
    if ( $text =~ /(\d+)/g ) {
        print "Matched : '$1'";
    }
}

main();
