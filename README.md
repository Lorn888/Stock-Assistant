# Mini Project README

untill we officially started using git this is where I stored the mini Project progress:
[here](https://github.com/Lorn888/Mini-Project)

## Project Background
This mini project was developed over several weeks to create a command-line application for managing products, couriers, and orders. The application evolved from handling basic lists to using more complex data structures and eventually integrating database functionalities.

## Client Requirements
The initial requirements were to create functionalities to add, view, update, and delete products, couriers, and orders. Later stages included persistent data storage using CSV files and ultimately transitioning to a database-driven approach.

## How to Run the App
To run the application:
1. Clone the repository from [GitHub](https://github.com/generation-de-nat1/Patryk-miniproject.git)
.
2. Navigate to the project directory in your terminal.
3. Create a virtual environment:
   ```bash
   python -m venv week6/csr/venv
4. Activate the virtual environment:

    On Windows (PowerShell):
    ```bash
    .\week6\csr\venv\Scripts\Activate.ps1
    ```
    On macOS/Linux:

    ```bash
    source week6/csr/venv/bin/activate
    ```

5. Install required dependencies:

    ```bash
    pip install pymysql python-dotenv
    ```
6. Start the Docker containers:

    ```bash
    docker-compose up -d
    ```

## Project Reflections
### Meeting the project's requirements
The design of the application progressed from simple user input handling and list structures to more sophisticated data management using dictionaries and database tables. This progression allowed for a more scalable and maintainable application.

### Guaranteeing the project's requirements
Throughout the development process, each week's goals were carefully reviewed and implemented to ensure alignment with the client's requirements. Regular testing and debugging were conducted to address any issues promptly.

### Future Improvements
One area for improvement would be to implement comprehensive unit tests. Unit testing would help validate the functionalities of each module and ensure that any changes made in the future do not introduce unintended issues.

### What I enjoyed Implementing
I enjoyed implementing the transition from file-based data storage (CSV) to a database-driven approach. This not only improved data management efficiency but also provided a more robust foundation for future enhancements.
test
