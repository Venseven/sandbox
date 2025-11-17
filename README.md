# sandbox

## How to run

### For macOS/Linux (bash)

1.  **Clone the repository:**
    ```bash
    git clone git@github.com:Venseven/sandbox.git
    cd sandbox
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    uvicorn main:app --reload --port 8002
    ```

5.  **Open your browser and go to:** [http://0.0.0.0:8002/docs](http://0.0.0.0:8002/docs)

### For Windows (PowerShell)

1.  **Clone the repository:**
    ```powershell
    git clone git@github.com:Venseven/sandbox.git
    cd sandbox
    ```

2.  **Create a virtual environment and activate it:**
    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```

3.  **Install the dependencies:**
    ```powershell
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```powershell
    uvicorn main:app --reload --port 8002
    ```

5.  **Open your browser and go to:** [http://0.0.0.0:8002/docs](http://0.0.0.0:8002/docs)
