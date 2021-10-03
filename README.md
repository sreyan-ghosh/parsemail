# parsemail - bulk mail sender
To be read pars-ayy-mail. Made for VITMAS. With love <3

### Usage
1. Clone the repo: `git clone git@github.com:sreyan-ghosh/parsemail.git`
1. [`mailsender.py`](mailsender) contains the code for a Python class `MailDeets.py`. Either uncomment the block or paste in another file. Make necessary changes in the import statements.
1. Fill in `MailDeets` class with your details. Click [here](https://myaccount.google.com/apppasswords) to get your SMTP password.
1. Add the dataset to the `data` directory and make necessary changes in the `filepath` variable in both the files.
1. To the [`parser.py`](parser) file, make changes in the line where the `pd.Series` object is loaded into the variable `maillist`
1. And you're done! SMTP allows sending of 85 mails at a go. Slice your list to resume sending mails if you get timed-out. The counter value will help there.

### Contribution
- Contribution is highly appreciated. 
- Go ahead and add better methods of sending mails that is not limited to SMTP or mailing limits.
- Add a feature to send attachments as well.
- Add a frontend to enable non-python users to work on this project.
- Go ahead and open an issue if you want to add something else.
- Take note to make a branch in your fork and open a PR for the commits on the branch. **master branch PRs will not be accepted**

[mailsender]: (https://github.com/sreyan-ghosh/parsemail/blob/master/mailsender.py)
[parser]: (https://github.com/sreyan-ghosh/parsemail/blob/master/parser.py)
