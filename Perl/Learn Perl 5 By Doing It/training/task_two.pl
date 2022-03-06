use strict;
use warnings;

# turn off output buffering -> seeing stuff that we print immediately
$| = 1;

sub main {

    # single quotes turns of interpretation of special characters.
    my @emails = (
        'stefan@abv.bg', 'antoan_stefanov@abv.bg',
        '@invalid.com',  'stefan_stefanov@abv.bg',
    );

    for my $email (@emails) {
        if ( $email =~ /\w+@\w+\.\w+/g ) {
            print "Valid email: ", $email, "\n";
        }
        else {
            print "Invalid email: ", $email, "\n";

        }
    }
}

main();
