# Step 1:
# Build image and add a descriptive tag
docker build --tag=pslencinas/myproject .

# Step 2: 
# List docker images
docker image ls

# Step 3: 
# Run create-react-app
docker run -p 5000:80 pslencinas/myproject
