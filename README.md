<strong>Overview</strong>

This is an open resource directory for returning citizens in the DC metro area, created at the <a href="http://rebuildingreentry.com/">Rebuilding Re-entry</a> hackathon. The link to the project is available <a href="https://returning-citizen-dc.herokuapp.com/">here</a>.

<strong>The Process</strong><br>

First, Aaron Schumacher and Elaine Ayo scraped data from the <a href="http://cjcc.dc.gov/">CJCC Directories</a>. You can view this code in the Django management commands <a href="https://github.com/millzpaugh/returning_citizen/tree/master/app/management/scraping">here</a>. We then converted addresses to coordinates using the geopy library and mapped the locations of provider organizations on google maps. 

This project is modeled after the <a href="www.buscandomaryland.com">Buscando project</a>, an open resource directory to assist Latin American children seeking refuge. 




