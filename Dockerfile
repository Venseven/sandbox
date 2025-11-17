# 1. Use an official Python runtime as a parent image
FROM python:3.9-slim

# 2. Set the working directory in the container
WORKDIR /app

# 3. Copy the requirements file into the container at /app
COPY requirements.txt .

# 4. Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application's code from your host to your image filesystem.
COPY . .

# 6. Make port 8000 available to the world outside this container
EXPOSE 8000

# 7. Run main.py when the container launches
CMD ["python", "main.py"]