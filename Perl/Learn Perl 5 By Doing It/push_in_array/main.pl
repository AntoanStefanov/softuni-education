use strict;
use warnings;
use feature 'say';

use Data::Dumper;

#  CHECK IF FILE HANDLE IS EXHAUSTED:
# https://stackoverflow.com/questions/2802267/how-can-i-tell-if-a-filehandle-is-empty-in-perl/2802759

# STDOUT, STDERR
# https://www.google.com/search?q=perl+stdout+stderr&oq=perl+stdout+S&aqs=chrome.1.69i57j0i22i30l9.5350j0j7&sourceid=chrome&ie=UTF-8

# what tail command do
# https://www.google.com/search?q=ubuntu+what+tail+do&oq=ubuntu+what+tail+do&aqs=chrome..69i57j0i22i30l3j0i10i22i30j0i22i30l5.2702j0j7&sourceid=chrome&ie=UTF-8

# turn off output buffering
$| = 1;

sub main {

# # if full path is used -> use single quotes, to NOT interpret the special characters in string, if there are ones.
    my $input =
'/home/antoan/GitHub/SoftUni-Education/Perl/Learn Perl 5 By Doing It/join_and_viewing_data_using_dumper/text.csv';

    open( my $fh, '<', $input ) or die "\nCannot open $input\n";

    <$fh>;    # Skip first line.

# What if we want to store file as we go along, how ?
# Be careful if file is HUGE! If file is huge ,
#  add it to database or write it to an output file, rather than storing it in memory

    # But how to store it in memory ?
    # put each line in array, define array .

    my @array_lines;
    # my $count = 0;

    while ( my $line = <$fh> ) {

#       By default chomp will chomp the $_ variable , $_ is the line if variable $line is not defined.
        chomp $line;
        # my @values = split( /\s*,\s*/, $line );

        # say join( "|", @values );

        push( @array_lines, $line );

        # $array_lines[$count] = $line;
        # $count++;
    }
    close $fh;

    foreach my $line (@array_lines) {
        say $line;
    }

# Change dir with "-" in path name
#     my $file_name =
# '/home/antoan/GitHub/SoftUni-Education/Perl/Learn-Perl-5-By-Doing-It/join_and_viewing_data_using_dumper/text.csv';

    #     my $find = "Rene";

    #     open my $fh, '-|', "tail -n 10 $file_name | grep $find" or die $!;

    #     if ( eof $fh ) {
    #         print "No lines\n";
    #     }
    #     else {
    #         print <$fh>;
    #     }
}

main();
