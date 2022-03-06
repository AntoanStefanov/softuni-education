use strict;
use warnings;

# turn off output buffering -> seeing stuff that we print immediately
$| = 1;

sub main {
    my $text = 'The code for this device is GP8452.';

    # 2 alphanumeric characters, 4 digits
    if ( $text =~ /([A-Z]{2}\d{2,6})/ ) {
        print $1, "\n";
    }
    else {
        print 'Not Found !';
    }

    # Second way

    if ( $text =~ /\bis (.+?)\./ ) {
        print "Second way $1\n";
    }
    else {
        print 'Not Found !';
    }
}

main();
