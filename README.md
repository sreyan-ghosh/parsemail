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

#### Parseteams (in dev) (Only for VIT)
- To use the [`get_mail_from_teams.py`](teamsparser) file, you must have the `WHO` bot installed in your teams profile.
- The driver function is the `get_emails()` function which accepts a list of registration numbers and returns the emails of the provided numbers.
- This utility is still buggy, since the script often runs faster than the page loads yielding repeated emails. Still can be used for bolk mail spamming.
- To be used in conjunction with the [`mailsender.py`](mailsender) file with minor code insertions to feed the list of emails into the `mailsender`.

[mailsender]: (https://github.com/sreyan-ghosh/parsemail/blob/master/mailsender.py)
[parser]: (https://github.com/sreyan-ghosh/parsemail/blob/master/parser.py)
[teamsparser]: (https://github.com/sreyan-ghosh/parsemail/blob/master/parseteams/get_mail_from_teams.py)
