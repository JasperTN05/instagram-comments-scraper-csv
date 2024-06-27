# Easy-to-Use Instagram Comments Scraper

This project automates the extraction of comments from any Instagram post. It logs into Instagram using provided credentials, navigates to the specified post URL, and exports all comments along with their corresponding likes to a CSV file.

## Installation

### Prerequisites

- Python => 3.8
- [Selenium Chrome Driver](https://pypi.org/project/selenium/)
- It is recommended to use a [virtual environments](https://docs.python.org/3/library/venv.html).

### Python Packages

Install the required Python packages using the `requirements.txt` file:

```pip install -r requirements.txt```

### Usage

- Run the App -> ```python app.py```
- Enter your Instagram Credentials (will not be stored) and the URL of the Post you want to extract the comments from.
- Receive a CSV file containing all extracted comments.

## Disclaimer

This script relies on specific HTML class names that may change over time. The script is intended for educational purposes only and should not be used to violate Instagram's policies or anyone's privacy.

## Contributing

I welcome contributions to this project! Feel free to submit pull requests for bug fixes, improvements, or new features. Please ensure your code adheres to the existing coding style and includes proper documentation.

## License
This project is under the MIT License. See the [License](https://github.com/JasperTN05/instagram-comments-scraper-csv/blob/main/LICENSE.md) file for Details.
