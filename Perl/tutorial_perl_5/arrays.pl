use strict;
use warnings;
use diagnostics;
use feature 'say';

my @primes = ( 2, 3, 5, 7, 11, 13, 17 );

# THIS WAY WE GET ARRAY LENGTH ! there is another way too
my $len = @primes;
say $len;

my @mixed_data_types = ( 21, 'Tony', "Al. Stamb.", 1.80 );
say @mixed_data_types;

# assign new values by referencing an index
$mixed_data_types[4] = "Bananas";

say @mixed_data_types;

for my $element (@mixed_data_types) {
    say $element;
}

foreach my $num (@primes) {
    say $num;
}

for (@mixed_data_types) {

    # $_ is automatically used if no variable was declared like above for loops.
    say $_;
}

# slice data from array

my @my_name = @mixed_data_types[ 1, 4 ];

say join( ' ', @my_name );

# length of array
# scalar used with array, returns length
my $number_of_items = scalar(@mixed_data_types);

say $number_of_items;

my ( $age, $addess ) = @mixed_data_types[ 0, 2 ];

print( join( ', ', $age, $addess ), "\n" );

# pop last value off, returns value

say "Popped value ", pop @mixed_data_types;

# push value of end of array, doesnt return item, but length of the array
say "Length with Pushed Value ", push @mixed_data_types, 15.3;

print( join( ', ', @mixed_data_types ), "\n" );

# removes and return first item of array
say "First item ", shift @mixed_data_types;

print( join( ', ', @mixed_data_types ), "\n" );

# Add value to front, return length of array
say "Length with Pushed at start array Value ", unshift @mixed_data_types, 21;
print( join( ', ', @mixed_data_types ), "\n" );

# splice out values
# splice(array, starting index, how many items we pull out), returns values
say "Remove index 0 - 2 ", splice @mixed_data_types, 0, 2;
print( join( ', ', @mixed_data_types ), "\n" );

print( join( " ", ( "list", "of", "words", "\n" ) ) );

# split turn a string into an array

my $customers       = 'tony, mony, shony';
my @customers_array = split( ', ', $customers );
print( join( ' ', @customers_array ), "\n" );

# reverse an array

@customers_array = reverse(@customers_array);
print( join( ' ', @customers_array ), "\n" );

# sort array

@customers_array = sort(@customers_array);
print( join( ' ', @customers_array ), "\n" );

# grep -> filter list , according to expression

my @number_array = ( 1, 2, 3, 4, 5, 6, 7, 8 );

#  $_ each individual value in array if a variable is not defined.
# regex could be used with grep in {} https://stackoverflow.com/questions/2925604/how-do-i-search-a-perl-array-for-a-matching-string
my @odd_array = grep { $_ % 2 } @number_array;

# OR

# my @odd_array = grep( $_ % 2, @number_array );

print( join( ' ', @odd_array ), "\n" );

# MAP
my @double_array = map { $_ * 2 } @number_array;
print( join( ' ', @double_array ), "\n" );
