use strict;
use warnings;
use feature 'say';

sub main {

    sub get_random {
        return int( rand(11) );
    }

    say "Random Number ", get_random();

    sub get_random_max {

        # @_ is the array of passed args.
        # @ for arrays, % for hashes, $ for scalars.
        my ($max_number) = @_;

   # give default, just in case arg is not passed.
   # $max_number = max_number || 11 (if max_number boolean is false, give it 11)
   #    https://stackoverflow.com/questions/29302181/what-is-in-perl-for
        $max_number ||= 11;

        return int( rand($max_number) );
    }

    get_random_max(4);

}

main();
