# Packtpub_Farmer

Packtpub_Farmer is a simple Python bot designed to automatically redeem the free book of the day from [Packtpub](https://www.packtpub.com/).

## Requirements:

- **Selenium**: Ensure you have Selenium installed. For installation instructions, refer to the official documentation [here](https://selenium-python.readthedocs.io/index.html).
- **Webdriver Manager**: Install the `webdriver-manager` module by running the command `pip install webdriver-manager`.
- **Configure accounts.txt**: Make necessary changes to the `accounts.txt` file.
- **Adjust variables**: Modify the variables at the beginning of the script, especially the Chrome User Profile Path.

**Note**: This script does not support captcha. If the code encounters a captcha verification, you will need to manually complete it.

## Tips:

- **Automate with Task Scheduler**: On Windows, consider setting up an automated task using the Task Scheduler.
- **Optionally Disable Headless Mode**: To view the actual books being redeemed, comment out the option: `options.add_argument('--headless=new')`. This is useful for debugging or monitoring the script's behavior.

Feel free to customize the script according to your needs and automate the process of claiming your daily free book effortlessly.
