import pandas as pd
hn = pd.read_csv("hacker_news.csv")

import re

titles = hn["title"].tolist()
python_mentions = 0
pattern = "[Pp]ython"

for t in titles:
    if re.search(pattern, t):
        python_mentions += 1
        
        

pattern = '[Pp]ython'
titles = hn['title']
python_mentions = titles.str.contains(pattern).sum()

titles = hn['title']
ruby_titles = titles[titles.str.contains(r"[Rr]uby")]


# The `titles` variable is available from
# the previous screens
email_bool = titles.str.contains("e-?mail")
email_count = email_bool.sum()
email_titles = titles[email_bool]



pattern = "\[\w+\]"
tag_titles = titles[titles.str.contains(pattern)]
tag_count = tag_titles.shape[0]



# pattern = r"\[\w+\]"
pattern = r"\[(\w+)\]"
tag_freq = titles.str.extract(pattern).value_counts()



def first_10_matches(pattern):
    """
    Return the first 10 story titles that match
    the provided regular expression
    """
    all_matches = titles[titles.str.contains(pattern)]
    first_10 = all_matches.head(10)
    return first_10
pattern = r"[Jj]ava[^Ss]"
java_titles = titles[titles.str.contains(pattern)]



pattern = r"\b[Jj]ava\b"
java_titles = titles[titles.str.contains(pattern)]


pattern_beginning = r"^\[\w+\]"
beginning_count = titles.str.contains(pattern_beginning).sum()

pattern_ending =  r"\[\w+\]$"
ending_count = titles.str.contains(pattern_ending).sum()



import re

email_tests = pd.Series(['email', 'Email', 'e Mail', 'e mail', 'E-mail',
              'e-mail', 'eMail', 'E-Mail', 'EMAIL', 'emails', 'Emails',
              'E-Mails'])
pattern = r"\be[\-\s]?mails?\b"
email_mentions = titles.str.contains(pattern, flags=re.I).sum()


