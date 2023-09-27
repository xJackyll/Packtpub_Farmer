# Packtpub_Farmer
A simple bot written in Python that automatically redeems the free book of the day from packtpub.com.

 Requirements:
- Install Selenium (see more at https://selenium-python.readthedocs.io/index.html)
- Have the right Chromedriver version (see more at https://chromedriver.chromium.org/downloads)
- Make the proper changes to the file accounts.txt
- Change the variables at the beginning of the file (mostly the Chrome User Profile Path )

This script do NOT support captcha. if the code stumble across a captcha verification you have to manually do it.

Tip:
- Make an automated task using the Task Scheduler if you're on windows
- You may want to comment this option in order to see the actual books being redeemed: options.add_argument('--headless=new') 
