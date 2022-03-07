use strict;
use warnings;

# turn off output buffering
$| = 1;

sub main {

# if full path is used -> use single quotes, to NOT interpret the special characters in string, if there are ones.
    my $input = 'text.csv';

    open( my $fh, '<', $input ) or die "\nCannot open $input\n";

    # read first line from file just like that (remove headings)
    <$fh>;

    while ( my $line = <$fh> ) {

        my @values = split( ',', $line );
        # print $values[1] . "\n";

        print join(' ', @values);
    }

    close $fh;
}
main();
