use strict;
use warnings;

# https://stackoverflow.com/questions/6303515/perl-1-what-is-this
$| = 1;

sub main {

#     my $file_path =
# '/home/antoan/GitHub/SoftUni-Education/Perl/Learn Perl 5 By Doing It/download_text_images/picture.png';

    my @file_paths = (
'/home/antoan/GitHub/SoftUni-Education/Perl/Learn Perl 5 By Doing It/download_text_images/picture.png',
'/home/antoan/GitHub/SoftUni-Education/Perl/Learn Perl 5 By Doing It/download_text_images/hello_world.pl',
'/home/antoan/GitHub/SoftUni-Education/Perl/Learn Perl 5 By Doing It/download_text_images/non-existing.png',
    );

    foreach my $file_path (@file_paths) {

        if ( -f $file_path ) {
            print "IT EXISTS: $file_path\n";
        }
        else {
            print "NO FILE FOUND: $file_path\n";
        }
    }

#   -f means check if this file exists or not
#   https://stackoverflow.com/questions/2601027/how-can-i-check-if-a-file-exists-in-perl

}

main();
