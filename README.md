# Real-Time-COVID-19-Tracker-for-Slack
This automated tracker tracks the spread of Covid-19 in a real time basis by scraping data from Ministry of Health and Family Welfare and notifies the same at Slack

# What it does

It scrapes the below table periodically from website of Ministry of Health and Family Welfare(https://www.mohfw.gov.in/).



If any changes has happened to the table compared to the state of last time checked, it creates a message describing the change and sends the message to a given user/channel in Slack.

# Pre-requisites

Python 2.7.x

Latest Pip with all envirionment variables set

# How to Set up the tracker

Run the following commands:

<h6>pip install beautifulsoup4</h6>
<h6>pip install requests</h6>

Then simply run the Notifier.py file by running the below command in Command Prompt

<h6>py Notifier.py</h6>

