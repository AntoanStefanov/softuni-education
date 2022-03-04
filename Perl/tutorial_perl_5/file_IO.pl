use strict;
use warnings;
use feature 'say';

# READ LINE BY LINE OR https://stackoverflow.com/questions/4505381/perl-read-line-by-line
sub read_file {

    # $_ is the error message if we have that
    my $employees_file = 'employees.txt';

    # fh -> file handler -> used to access the file
    # '<' means opening the file for read-only
    # file we will be reading from
    # die -> kill program
    open my $fh, '<', $employees_file
      or die "Can't open file '$employees_file'. Error: $_";

    while ( my $line = <$fh> ) {

        # remove \n at the end of line
        chomp($line);

        my ( $employee_name, $job, $id ) = split( /:/, $line );

        say join ', ', $employee_name, $job, $id;

    }

    close $fh or die "Can't close file '$employees_file'. Error: '$_'";
}

read_file();

sub read_file_2 {
    my $file = 'employees.txt';

    open my $info, $file or die "Could not open $file: $!";

    while ( my $line = <$info> ) {
        chomp($line);

        my ( $employee_name, $job, $id ) = split( /:/, $line );

        say join ', ', $employee_name, $job, $id;

    }

    close $info or die "Can't close file '$file'. Error: '$_'";
}

read_file_2();

sub appending_to_file {
    my $employees_file = 'employees.txt';

    open my $fh, '>>', $employees_file
      or die "Can't open file '$employees_file. Error: '$_'";

    # append to the end of the file
    print $fh "Tony:Programmer:126\n";

    close $fh or die "Can't close file '$employees_file'. Error: '$_'";

}

# putting data at the end of the file
appending_to_file();

# OPEN FILE TO READ AND WRITE

sub read_and_write_file_1 {
    my $employees_file = 'employees.txt';

    open my $fh, '+<', $employees_file
      or die "Can't open file '$employees_file. Error: '$_'";

    # move to beginning of file
    seek $fh, 0, 0;
    print $fh "Magare:Programmer:127\n";

    close $fh or die "Can't close file '$employees_file'. Error: '$_'";
}

read_and_write_file_1();

sub read_and_write_file {
    my $employees_file = 'employeees.txt';

    open my $employees_file_fh, '<', $employees_file
      or die "Can't open file '$employees_file. Error: '$_'";

    my $newfile = 'newfile.txt';

    open my $newfile_fh, '>', $newfile
      or die "Can't open file '$newfile. Error: '$_'";

    print $newfile_fh "Magare:Programmer:127\n";
    while (<$employees_file_fh>) {
        print $newfile_fh $_;
    }

    close $employees_file_fh
      or die "Can't close file '$employees_file'. Error: '$_'";

    close $newfile_fh or die "Can't close file '$newfile_fh'. Error: '$_'";
}

read_and_write_file();
