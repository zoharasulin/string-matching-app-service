# String Matching Similarity

This project calculates the similarity score between two input strings using fuzzy string matching techniques. It utilizes the fuzzywuzzy library to calculate the similarity score based on the Levenshtein distance algorithm.

## Getting Started

To get started with this project, follow the steps below:

### Prerequisites

- Python 3.9 or higher
- Pip package manager

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git

   Change to the project directory:
   cd your-repository
   Install the project dependencies:
   pip install -r requirements.txt
### Usage
1. Run the Flask application:
   ```bash
    python app.py
2. The application will start running on [http://localhost:5000/string-matching](http://localhost:5000/string-matching).

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
