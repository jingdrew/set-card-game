
## Prerequisites

- **Python 3.7+**
- **pip** (Python package installer)
- **virtualenv** (optional but recommended)

## How to Run Locally

### 1. Clone the Repository

`git clone https://github.com/jingdrew/set-card-game.git`
`cd set-card-game`

### 2. Set Up a Virtual Environment

It is recommended to use a virtual environment to avoid conflicts between Python packages.

-   On **macOS/Linux**:

    `python3 -m venv venv`
    `source venv/bin/activate` 
    
-   On **Windows**:

    `python -m venv venv`
    `venv\Scripts\activate` 
    

### 3. Install the Dependencies

`pip install -r requirements.txt` 

### 4. Run the FastAPI Server

To start the FastAPI server, run the following command:
`uvicorn main:app --reload` 

-   The server will start at `http://127.0.0.1:8000/`.
-   The `--reload` flag allows the server to auto-reload whenever you make changes to your code (useful during development).

### 5. Test the API

You can access the API documentation and test the endpoints using Swagger UI:

-   Open your browser and go to: `http://127.0.0.1:8000/docs`.

You can also test the API using `curl` or Postman.

#### Example Request

Send a POST request to `/find-sets/` with a JSON body that contains a list of cards.

-   **URL**: `http://127.0.0.1:8000/find-sets/`
-   **Method**: `POST`
-   **Content-Type**: `application/json`
-   **Body**:

`{
  "cards": ["1111", "2222", "3333", "1112", "2221"]
}` 

#### Example Response

`{
  "valid_sets": [
    ["1111", "2222", "3333"],
    ["1111", "2221", "3333"]
  ]
}` 

### 6. Deactivate the Virtual Environment

When you are done, deactivate the virtual environment by running:
`deactivate` 

### 7. More Examples**

Valid examples

`{
    "cards": ["1111", "2222", "3333", "2221", "3331"]
}`

`{
    "cards": ["1111", "2222", "3333"]
}`

`{
    "cards": ["1111", "2221", "3331"]
}`


Invalid Examples


`{
    "cards": ["1111", "1222", "3333"]
}`

`{
    "cards": ["1211", "2221", "3331"]
}`
