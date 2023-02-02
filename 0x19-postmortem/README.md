Postmortem

At approximately 08:30 West African Time (WAT), an outage occurred on an isolated Ubuntu 14.04 container running an Nginx web server. GET requests on the server led to 500 Internal Server Error's, when the expected response was an HTML file defining a simple website.
Debugging Process

I encountered the issue upon opening the project and being well instructed to address it, roughly 11:00 WAT. I quickly proceeded to begin solving the problem.

    Checked running processes using ps aux. Two nginx processes - root and www-data - were properly running.

    Looked in the sites-available folder of the /etc/nginx/sites-available directory. Determined that the web server was serving content located in /var/www/html/.

    In one terminal, ran strace on the PID of the root nginx process. In another, curled the server. Expected verbose results... only to be disappointed. strace gave no useful information.

    Repeated step 3, except on the PID of the www-data process. Alas! strace revelead an strace: exec: Permission denied error occurring upon an attempt to access the file /var/www/html/home.html.

    Reviewed the permissions for the files in the html directory and found out that the directory had been erroneously set as read-only, subsequently all files in the directory inherited the parent folder's access control.

    Corrected the access control for the 'html' directory using the chmod command.

    Tested another curl on the server. returned 200!

Summation

The fix involved a simmple chmod command to reset the access control
Prevention

This outage was a web server error that occured due to restricted access to the server files, to prevent such outages moving in future, below are some suggestions.

    Test! Test the application before deploying. This error would have arisen and could have been corrected earlier had the app been tested.

    Status monitoring. Enable some server-monitoring service such as Datadog to alert instantly upon outage of the website.
