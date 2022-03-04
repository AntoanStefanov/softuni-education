package Animal::Cat;

use strict;
use warnings;

# contructor
sub new {
    my $class = shift;
    my $self  = {
        name  => shift,
        owner => shift,
    };

    # bless returns reference
    bless $self, $class;
    return $self;
}

sub getName {
    my ($self) = @_;
    return $self->{'name'};
}

sub setName {
    my ( $self, $name ) = @_;
    $self->{'name'} = $name if defined($name);
    return $self->{'name'};
}

sub getSound {
    my ($self) = @_;
    return $self->{'name'}, ' says "Meow"';
}

# finish off packages, package must return true whenever is called.
1;
