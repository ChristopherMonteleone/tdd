from flask import Flask
from src import status

app = Flask(__name__)

COUNTERS = {}

# Create a route for creating a counter using POST
@app.route('/counters/<name>', methods=['POST'])
def create_counter(name):
    """Create a counter"""
    app.logger.info(f"Request to create counter: {name}")
    
    global COUNTERS
    if name in COUNTERS:
        return {"Message": f"Counter {name} already exists"}, status.HTTP_409_CONFLICT
    COUNTERS[name] = 0
    return {name: COUNTERS[name]}, status.HTTP_201_CREATED

# Create a route for updating a counter using PUT
@app.route('/counters/<name>', methods=['PUT'])
def update_counter(name):
    """Update a counter by 1"""
    app.logger.info(f"Request to update counter: {name}")
    
    global COUNTERS
    if name in COUNTERS:
        COUNTERS[name] += 1
        return {name: COUNTERS[name]}, status.HTTP_200_OK
    else:
        return {"Message": f"Counter {name} not found"}, status.HTTP_404_NOT_FOUND

# Create a route for reading a counter using GET
@app.route('/counters/<name>', methods=['GET'])
def read_counter(name):
    """Read a counter"""
    if name in COUNTERS:
        return {name: COUNTERS[name]}, status.HTTP_200_OK
    else:
        return {"Message": f"Counter {name} not found"}, status.HTTP_404_NOT_FOUND
    
# Create a route for deleting a counter using DELETE
@app.route('/counters/<name>', methods=['DELETE'])
def delete_counter(name):
    """Delete a counter"""
    app.logger.info(f"Request to delete counter: {name}")
    
    global COUNTERS
    if name in COUNTERS:
        del COUNTERS[name]
        return "", status.HTTP_204_NO_CONTENT
    else:
        return {"Message": f"Counter {name} not found"}, status.HTTP_404_NOT_FOUND