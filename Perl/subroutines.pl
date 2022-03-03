use strict;
use warnings;
use feature 'say';
use feature 'state';

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

    say get_random_max(3);

    sub get_sum {
        my ( $num_1, $num_2 ) = @_;

        $num_1 ||= 1;
        $num_2 ||= 1;

        return $num_1 + $num_2;
    }

    say get_sum();

    sub sum_unknown_numbers {
        my $sum = 0;
        foreach my $num (@_) {
            $sum += $num;
        }
        return $sum;
    }

    say sum_unknown_numbers( 2, 3, 4, 5 );

    sub increment {

        # remain value after each call
        state $execute_total = 0;
        $execute_total++;
        say "Executed $execute_total Total";
    }

    increment();
    increment();

    sub double_array {

        # return multiple values
        my @num_array = @_;
        $_ *= 2 for @num_array;
        return @num_array;
    }
    my @random_array = ( 2, 3, 4 );
    say join ', ', double_array(@random_array);

    sub get_mults {
        my ($rand_num) = @_;
        $rand_num ||= 1;

        return $rand_num * 2, $rand_num * 3;
    }

    my ( $doubled_num, $triplet_num ) = get_mults(3);

    say "$doubled_num, $triplet_num";

    # recursive subroutines.
    sub factorial {
        my ($num) = @_;
        return 0 if $num <= 0;
        return 1 if $num == 1;
        return $num * factorial( $num - 1 );
    }

    say factorial(5);
}

main();
