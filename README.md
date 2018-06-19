# footballNotifier
---
> A Python application that sends you a SMS when the football team you support scores.

## Getting Started
---
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

1. Download and install [Python 3.6](https://www.python.org/downloads/).
2. Clone this repository.
3. Open the terminal, navigate to the folder where your clone of this repository is located and type:
  
  `$ pip install -r requirements.txt`

  This will install all the necessary packages to run this script.

4. Open `config.ini`.
  * 4.1. Add in your `NUMBER` and `TEAM` (e.g: Portugal, Sweden, Real Madrid)
  * 4.2. Go to [Textlocal](https://www.textlocal.com/), register an account and then create an `API_KEY` [here](https://control.txtlocal.co.uk/settings/apikeys/). Copy the `API_KEY` key and fill it in `config.ini` accordingly.
5. Type `$ python app.py` in the terminal and the script will run for as long as you let it.

> Textlocal has a limit of 10 messages per month, so let's hope your team doesn't score more than 10 goals per month!

If you follow these steps, you will receive a message on your phone when your team scores, as seen below:
![Example](https://i.imgur.com/lP7ULoi.png)

## To-Do
---
[ ] Add support for multiple teams.
[ ] Deploy the project on GitHub pages and allow more people to use this without having to install Python on their machine.
[ ] Probably re-do a lot of the code. This is my second *"big"* Python project and I'm sure there are a lot of things I can optimize. I appreciate any PRs! :)

### Thanks for checking the project!
