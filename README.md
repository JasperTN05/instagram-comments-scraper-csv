# Easy-to-Use Instagram Comments Scraper

This project is an Instagram comments scraper that allows you to extract comments from any Instagram post. The script logs into Instagram using provided credentials, navigates to the specified post, and extracts all comments along with the number of likes each comment received.The results are directly exported as an .csv file.

## Installation

### Prerequisites

- Python => 3.8
- [Selenium Chrome Driver](https://pypi.org/project/selenium/)

### Python Packages

Install the required Python packages using the `requirements.txt` file:

```pip install -r requirements.txt```

### Usage

- Run the App -> ```python app.py```
- Enter your Instagram Credentials and the URL of the Post you want to extract the comments from.
- Receive .csv file with all comments.

## Disclaimer

This script relies on specific class names that might change in the future. Consider using more generic selectors or combining them with other attributes for better adaptability. The script is intended for educational purposes only and should not be used to violate Instagram's policies or anyone's privacy.

## Contributing

I welcome contributions to this project! Feel free to submit pull requests for bug fixes, improvements, or new features. Please ensure your code adheres to the existing coding style and includes proper documentation.

## License

