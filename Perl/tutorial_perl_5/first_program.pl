# https://www.youtube.com/watch?v=WEghIXs8F6c&t=2107s
use strict;
use warnings;
use diagnostics;

# use feature 'say';

use feature 'switch';

use v5.16;

# INTRO & SCALARS
# SCALARS ARE VARIABLES THAT HOLD UP JUST ONE VALUE. STRING NUMBER OR WHATEVER
# %d used for integers.
# concat strings -> . instead of +

# "" -> INTERPOLATIONS INCLUDING \n, '' -> PLAIN STRING, here \n will be just \n.

# length() is only used with strings(scalars)
# to find array length use scalar()

my $asd = 'Hello';
print('Hello World');
print($asd);

# $, = ', '

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

say "EXP 1 = ",         exp 1;
say "INT 6.45 = ",      int 6.45;
say "RANDOM 0 - 10 = ", rand 11;

my $rand_num = 6;

# PRINT THEN INCREMENT
say "6++ = ", $rand_num++;

# INCREMENT THEN PRINT
say "++7 = ", ++$rand_num;

# Conditionals

# False -> undef, 0, 0.0, "", "0"

my $age      = 80;
my $is_drunk = 0;    # 1 -> True | 0 -> False

if ( $age < 16 ) {
    say "You can't drive.";
}
elsif ($is_drunk) {
    say "You can't drive.";
}
else {
    say "You can drive.";
}

#  eq ne lt le gt ge

if ( 'a' eq 'b' ) {
    say "a equals b";
}
else {
    say "a doesn't equal b";
}

# Ternary operator
say( ( $age > 18 ) ? "Can vote" : "Can't vote" );

#  LOOPING

# for ( my $i = 0 ; $i < 10 ; $i++ ) {
#     say $i;
# }

my $i = 0;

while ( $i < 10 ) {
    if ( $i % 2 == 0 ) {
        say $i;
    }
    $i++;

    # next; -> continue
    # last; -> break
    if ( $i == 7 ) {
        last;
    }
}

# DO-WHILE -> USE WHEN YOU WANT TO  GO ATLEAST ONE TIME THROUGH THE LOOP

my $lucky_num = 7;
my $guess;

# do {
#     say "Guess the number between 1 and 10";

#     # GET INPUT FROM USER -> STANDARD IN;
#     $guess = <STDIN>;
# } while ( $guess != $lucky_num );

# say "You are right, number is 7";

# Switch in perl is called  "given when statement"

my $age_old = 18;

given ($age_old) {

    # $_ represents age_old variable
    when ( $_ > 16 ) {
        say 'Drive';

        # put continue, to check other when's
        continue;
    }
    when ( $_ > 17 ) {
        say "Go Vote!";
    }

    # default when none of the when's are true
    default {
        say "Default";
    }
}

# Strings -> It is scalar like anything else except arrays and hashes.

my $long_string = "Random Long String";

say "Length of string ", length $long_string;

printf( "Long is at %d\n", index( $long_string, 'Long' ) );

printf( "Last g is at %d\n", rindex( $long_string, 'g' ) );

# Concatenate
$long_string = $long_string . "\n";

say $long_string;

# substring -> first = string, second = starting index , third = number of chars to retrieve.

say "Index 7 through 10 ", substr $long_string, 7, 4;

my $animal = "animals";

#  chop delete and return the last char of string
# https://stackoverflow.com/questions/36882022/difference-between-printf-print-and-sprintf-in-perl
my $last_char = sprintf "Last character is %s\n", chop $animal;

# say $last_char;
say $animal;

# chomp delete new lines

my $no_new_line = "No newline\n";
print $no_new_line;
chomp $no_new_line;
print $no_new_line;

my $string = 'stRing is here';

printf( "Uppercase: %s\n",     uc $string );
printf( "Lowercase: %s\n",     lc $string );
printf( "1st Uppercase: %s\n", ucfirst $string );

# Takes list of chars on left and replace them with the chars on right.

# replace spaces with , and space , g flag replace all occurences
$string =~ s/ /, /g;

say $string;

my $two_times = "What I said is \n" x 2;
print $two_times;

# array with @
my @abcs = ( 'a' .. 'z' );
print join( ", ", @abcs ) . "\n";

#  INCREMENT LETTER
my $letter = 'c';
say "Next letter: ", ++$letter;

#  ARRAYS
