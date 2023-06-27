# String Matching Similarity APP Service

This project calculates the similarity score between two input strings using [FuzzyWuzzy](https://github.com/seatgeek/thefuzz) includes a Flask web application that allows users to interact with the string similarity calculation. 

It utilizes the fuzzywuzzy library to calculate the similarity score based on the [Levenshtein distance algorithm](https://en.wikipedia.org/wiki/Levenshtein_distance).

## Getting Started

To get started with this project, follow the steps below:

### Prerequisites

- Python 3.9 or higher
- FuzzyWuzzy:
  
     ```bash
      pip install fuzzywuzzy
     ```
- Flask:
  
  ```bash
      pip install flask
  ```
### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/zoharasulin/string-matching-app-service.git
   ```
2. Navigate to the project directory:
   ```bash
    cd your-repository
      ```
4.  Install the project dependencies:
   ```bash
     pip install -r requirements.txt
   ```

### Usage
To use the string similarity calculation in your application, follow these steps:

1. Run the Flask application:
   ```bash
    python app.py
2. The application will start running on http://localhost:5000/string-matching.

3. Open your web browser and navigate to http://localhost:5000/string-matching.
    You will see a form where you can enter two strings for similarity calculation.

4. Enter the input strings and click the "Calculate Similarity" button.

5. The application will display the similarity score between the two strings.

### Example
Here's an example usage of the application:

Input 1: "hello"
Input 2: "hallo"

The application will calculate the similarity score and display 

```bash
the result:0.8
```
### Testing

To run the unit tests for this project, execute the following command:
```bash
python -m unittest discover tests
```
### Contributing
Contributions to this project are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or a pull request.

### License
This project is licensed under the [MIT License](https://opensource.org/license/mit/)

