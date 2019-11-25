# Kang Ming's API

## Set Up
<p>All you gotta do is run <code>docker-compose up</code> </p>

## Testing the API
1. Install Postman 
2. Import the Postman collection titled <code>Apple_Assessment_API.postman_collection.json</code>
3. Run all the APIs in the collection

#### Alternatively...
<p> Visit <code>localhost:8000/api/items/</code> to view the <code>API Root Directory</code>

## API Design
### API consists of the following endpoints
<ol>
    <li><code>GET</code> Created 2 different search endpoints for Rack and PDU objects</li>
    <li><code>POST</code> Created 2 different create endpoints for creating Rack and PDU objects</li>
    <li><code>PUT</code> Created 2 different update endpoints for updating Rack and PDU objects based on their ID<li>
    <li><code>GET</code> Created 2 different endpoints for retrieving a specific rack or pdu object based on their ID</li>
</ol>

## Things to work on (if I had more time):
1. Add Unit tests for every api 
2. Add an authentication token for the API that changes every hour for security purposes
3. Add User credentials
4. Find out how to persist data on docker container so there would be available sample data to test with when docker container is run

