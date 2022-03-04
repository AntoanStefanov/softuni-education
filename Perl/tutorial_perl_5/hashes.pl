use strict;
use warnings;
use feature 'say';

sub main {
    my %employees = (
        "Tony"  => 21,
        "Steve" => 32,
        "Sam"   => 33,
    );

    printf( "Tony is %d\n", $employees{Tony} );

    $employees{Frank} = 44;
    say join ', ', %employees;

    while ( my ( $key, $value ) = each %employees ) {
        print "$key: $value\n";
    }

    my @ages = @employees{ "Tony", "Sam" };
    say join ', ', @ages;
    print( ref(@ages) );

    # convert hash into an array
    my @hash_array = %employees;
    say join ', ', @hash_array;

    # delete key
    my $frank_age = delete $employees{Frank};
    say $frank_age;

    while ( my ( $key, $value ) = each %employees ) {
        print "$key: $value\n";
    }

    # Sort the hash in alphabetical order of its keys

    foreach my $name ( sort keys %employees ) {
        printf "%-8s %s\n", $name, $employees{$name};
    }

    # check if exists
    say( ( exists $employees{'Sam'} ) );

    # LOOP through keys

    for my $name ( keys %employees ) {
        if ( $employees{$name} == 21 ) {
            say $name;
        }
    }

    # keys
    my @names = keys %employees;
    say @names;

    # values
    my @ages = values %employees;
    say @ages;

}

main();
