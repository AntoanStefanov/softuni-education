# https://www.youtube.com/watch?v=WEghIXs8F6c&t=2107s
use strict;
use warnings;
use diagnostics;

# use feature 'say';

use feature 'switch';

use v5.16;

# INTRO & SCALARS

my $asd = 'Hello';
print('Hello World');
print($asd);

# my $perl_cmd = "perl --version";

# my $perl_str = `$perl_cmd`;
# print "PERL VERSION = " . $perl_str;

my $name = 'Tony';
say $name;

my ( $age, $street ) = ( 21, 'Al. Stambo' );

# my $street = 'Al. Stambo';
say $age, $street;

my $my_info = "$name lives on \"$street\"";

$my_info = qq{$name lives on "$street" !};

say $my_info;

my $bunch_of_info = "This is a 
Bunch of info:
$my_info
on multiple
Lines";
say $bunch_of_info;
say $name;

my $big_int = ~0;

say $big_int;

print "BIG INT: $big_int \n";

my $big_float = .100000000001;

printf( "%.3f\n", $big_float );

# say("$big_float.3f");

my $first  = 1;
my $second = 2;

( $first, $second ) = ( $second, $first );

say( $first, ' ', $second );


# MATH

say "EXP 1 = ", exp 1;
say "INT 6.45 = ", int 6.45;
say "RANDOM 0 - 10 = ", rand 11;

my $rand_num = 6;

# PRINT THEN INCREMENT
say "6++ = ", $rand_num++;
# INCREMENT THEN PRINT
say "7++ = ", ++$rand_num;