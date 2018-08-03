# tumbo-demoapp

Demonstrates Tumbo's features with an example application.

    git clone git@github.com:sahlinet/tumbo-demoapp.git
    zip -r tumbo-demoapp  . -x ".git/*" .     # creates tumbo-demoapp.zip
    tumbo-cli.py project tumbo-demoapp import tumbo-demoapp.zip

or

    tumbo-cli.py project tumbo-demoapp create --git_url=https://github.com/sahlinet/tumbo-demoapp.git --branch=master

Then visit the application on the dashboard and open `index.html`.
