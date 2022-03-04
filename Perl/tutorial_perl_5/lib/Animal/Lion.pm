package Animal::Lion;

use lib 'lib';
use Animal::Cat;
use strict;

# inherit all variables and subroutines from Cat

our @ISA = qw(Animal::Cat);

sub getSound {
    my ($self) = @_;
    return $self->{name}, ' says "Rowrr"';
}

1;
