# ToolsAndServices

### Info

- server: **FastAPI**
    
    - reason: 

        Lightweight and high performance framework.

        Automatic Documentation (Swagger UI).
    
        Supports asynchronous programming, allowing to make async requests to the external API.
  
        

- database: **MongoDB**

    - reason:

      There is just one table users, so NoSQL database was chosen.

      MongoDB is a document-oriented database and used for store complex, hierarchical data structures.

      Structure of users from the external API is suitable for MongoDB.


### Launch

#### API Launch

`cd .../ToolsAndServices`

`docker-compose up --build`

