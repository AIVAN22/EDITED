This script requires the following Python packages:

pip3 install selenium , beautifulsoup4 , json

Make sure to have these packages installed before running the script.
 
Geckodriver is a WebDriver implementation that allows you to control Firefox web browser. To use Geckodriver with Firefox, you need to have Geckodriver executable file in the system PATH or in the same folder as your browser executable file.  
 
In addition, this script uses the Firefox web driver provided by GeckoDriver. The path to the driver executable file is hardcoded in the script and may need to be changed depending on the system configuration.
Usage

To use the script, call the scrape function with the following arguments:

    url: the URL of the product page to scrape
    class_element_name: the class name of the HTML element containing the product name
    class_element_color: the class name of the HTML element containing the product color
    class_element_price: the class name of the HTML element containing the product price
    class_element_size: the class name of the HTML element containing the product size

The function will then launch a Firefox browser, navigate to the specified URL, scrape the information using the specified HTML class names, and save the information to a JSON file with a timestamped filename.



