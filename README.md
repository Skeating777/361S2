For this version of the microservice to access array information, it needs the information parsed to the data.txt text file; this is suggested to be done by appending data to the text file as items are added to the array, but compiling the data all at once is also acceptable. The data needs to be written as individual lines representing rows, and it needs to use "/" as a delimiter (ex. writing your column headings might look something like "City/State/Note"). 

Running this program locally will require installation of pandas Library. 

The program is designed to monitor the contents of export_service.txt and then clear it when done, so the program will run until terminated once started. In order to initiate the export, "run" needs to be written to export_service.txt. 

Given the purpose of the program is to adapt and export the contents of a text file, the only information available to the calling program on completion of the process will be a confirmation string written to export_response.txt that states where the file was sent to; this may be read and displayed as desired. 

[Sequence diagram for this project](Sequence diagram.png)