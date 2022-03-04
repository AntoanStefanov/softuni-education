use strict;
use warnings;

# for retrieving html file from internet
use LWP::Simple;

sub main {

    print "Downloading...\n";

    # print get("https://edition.cnn.com/");
    # HTML
    # getstore( "https://edition.cnn.com/", "cnn_home.html" );

    # picture
    getstore(
'https://media.cnn.com/api/v1/images/stellar/prod/220303094228-max-verstappen-smiling-tease.jpg?c=16x9&q=h_720,w_1280,c_fill',
        "picture.png"
    );

    # getstore returns status_code
    my $status_code = getstore(
'https://media.cnn.com/api/v1/images/stellar/prod/220303094228-max-verstappen-smiling-tease.jpg?c=16x9&q=h_720,w_1280,c_fill',
        "picture.png"
    );

    if ( $status_code == 200 ) {
        print "Success\n";
    }
    else {
        print "Failed\n";
    }

    print "Finished\n";

}

main();
