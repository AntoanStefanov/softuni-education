use strict;
use warnings;
use feature 'say';

use Data::Dumper;

# turn off output buffering
$| = 1;

sub main {

# if full path is used -> use single quotes, to NOT interpret the special characters in string, if there are ones.
    my $input =
'/home/antoan/GitHub/SoftUni-Education/Perl/Learn Perl 5 By Doing It/join_and_viewing_data_using_dumper/text.csv';

    open( my $fh, '<', $input ) or die "\nCannot open $input\n";

    # INSTEAD OF WHILE LOOP LINE BY LINE, GET DATA IN ARRAY #

    # read the contents into an array, if needed.
    my @info = <$fh>;
    shift(@info);
    for my $line (@info) {
        chomp $line;
        my @values = split( /\s*,\s*/, $line );
        say join( ", ", @values );
    }

    # INSTEAD OF WHILE LOOP LINE BY LINE, GET DATA IN ARRAY #

    # WITH WHILE LOOP #
    
    # read first line from file just like that. (remove headings)
    <$fh>;    # Skip first line.

    # FOR LOOPED EXHAUSTED file handle (comment for loop to check how code works with while)
    # https://stackoverflow.com/questions/2802267/how-can-i-tell-if-a-filehandle-is-empty-in-perl/2802759
    while ( my $line = <$fh> ) {

# By default chomp will chomp the $_ variable , $_ is the line if variable $line is not defined.
        chomp $line;
        my @values = split( /\s*,\s*/, $line );

        # print $values[1] . "\n";

        # print join(", ", @values);

        print Dumper(@values);
    }

    # WITH WHILE LOOP #

    close $fh;
}

main();
