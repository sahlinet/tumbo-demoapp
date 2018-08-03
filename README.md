# tumbo-demoapp
Demo App for Tumbo

    git clone git@github.com:sahlinet/tumbo-demoapp.git
    zip -r tumbo-demoapp  . -x ".git/*" .     # creates tumbo-demoapp.zip
    tumbo-cli.py project tumbo-demoapp import tumbo-demoapp.zip

or

    tumbo-cli.py project tumbo-demoapp create --git_url=https://github.com/sahlinet/tumbo-demoapp.git --branch=master
