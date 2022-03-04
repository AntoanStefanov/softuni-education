use strict;
use warnings;
use feature 'say';

use lib 'lib';

# class - package, self-contained unit of variables and subroutines
use Animal::Cat;

sub main {

    my $whiskers = new Animal::Cat( 'whiskers', "Tony" );

    say $whiskers->getName();

    $whiskers->setName('Jack');

    say $whiskers->getName();

    say $whiskers->getSound();

    use Animal::Lion;

    my $king = new Animal::Lion( 'King', 'Tony' );

    say $king->getName();
    say $king->getSound();
}

main();
