use strict;
use warnings;

use Data::Dumper;

# turn off output buffering
$| = 1;

sub main {

# if full path is used -> use single quotes, to NOT interpret the special characters in string, if there are ones.
    my $input = 'text.csv';

    open( my $fh, '<', $input ) or die "\nCannot open $input\n";

    # read first line from file just like that. (remove headings)
    <$fh>; # Skip first line.

    while ( my $line = <$fh> ) {

# By default chomp will chomp the $_ variable , $_ is the line if variable $line is not defined.
        chomp $line;
        my @values = split( /\s*,\s*/, $line );

        # print $values[1] . "\n";

        # print join(", ", @values);

        print Dumper(@values);
    }

    close $fh;
}
main();
