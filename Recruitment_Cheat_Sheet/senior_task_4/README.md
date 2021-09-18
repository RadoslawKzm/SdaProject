
Build a basic HTTP application using a python web framework of your 
choosing. 
 
1.    Create a public Github repo. This repo should be publicly 
accessible) 
 
1.    Application to have the following endpoints: 
 
         1. ping 
 
             1. METHOD: `POST` 
 
             1. endpoint: `ping` 
 
              1. accepts a body containing a url key and corresponding 
link, ie `{‘url’: ‘ https://www.foobar.com‘}`; This route should send a 
GET request to that endpoint, ignoring SSL for simplicity, and return 
the payloadof that request as the response for the route. 
 
1.    
 
         1. info 
 
            1. METHOD: `GET` 
 
            2. endpoint: `info` 
 
            3. returns hardcoded status of `{“Receiver”: “Dupa is the 
best!”}` 
 
3.    All of this should be started/stopped using cli 
 
4.    Assume you are working on a team who will need to interpret and 
develop your code further. Publish this in Github and assume it will be 
reviewed with the team lead. Add appropriate documentation as 
necessary. 
 
5.    Without overcomplicating the original design of the script, you 
are encouraged to improve the assignment however you see fit.   
 
BONUS points: 
 
1. Run application in container 
 
2. Expose API documentation for the services using swagger 
 
