from github import Github
from bs4 import BeautifulSoup
from markdown import markdown
import json

def getWhat(text):
	what_list = []
	for i in text:
		if(i.upper().find('[X]') !=-1):
			what_list.append(i.upper().replace('[X] ', '').replace('-','').strip())
	return(what_list)
def getWhen(text):
	month = ''
	for i in text:
		if(i.upper().find('JANUARY') !=-1 or i.upper().find('JAN') !=-1 ):
			month = 'JANUARY'
		if(i.upper().find('FEBRUARY') !=-1 or i.upper().find('FEB') !=-1 ):
			month = 'FEBRUARY'
		if(i.upper().find('MARCH') !=-1 or i.upper().find('MAR') !=-1 ):
			month = 'MARCH'
		if(i.upper().find('APRIL') !=-1 or i.upper().find('APRIL') !=-1 ):
			month = 'APRIL'
		if(i.upper().find('MAY') !=-1 or i.upper().find('MAY') !=-1 ):
			month = 'MAY'
		if(i.upper().find('JUNE') !=-1 or i.upper().find('JUN') !=-1 ):
			month = 'JUNE'
		if(i.upper().find('JULY') !=-1 or i.upper().find('JUL') !=-1 ):
			month = 'JULY'
		if(i.upper().find('AUGUST') !=-1 or i.upper().find('AUG') !=-1 ):
			month = 'AUGUST'
		if(i.upper().find('SEPTEMBER') !=-1 or i.upper().find('SEPT') !=-1 or i.upper().find('SEP') !=-1 ):
			month = 'SEPTEMBER'
		if(i.upper().find('OCTOBER') !=-1 or i.upper().find('OCT') !=-1 ):
			month = 'OCTOBER'
		if(i.upper().find('NOVEMBER') !=-1 or i.upper().find('NOV') !=-1 ):
			month = 'NOVEMBER'
		if(i.upper().find('DECEMBER') !=-1 or i.upper().find('DEC') !=-1 ):
			month = 'DECEMBER'
	return month

### Use your credentials
###
g = Github("USER", "PASSWORD")
###
###
repo = g.get_repo("campus-experts/being-an-expert")
list_of_issues = []

issues = repo.get_issues(state='all')



for countIssues,i in enumerate(issues):
	issue = {}
	issue['number'] = (i.number)
	issue['title'] = i.title
	issue['labels'] = []
	issue['user'] = i.user.login
	for label in repo.get_issue(i.number).labels:
		issue['labels'].append(label.name)
	for count, line in enumerate(i.body.splitlines()):
		if(line == '## What do you want to do? Tick all applicable!'):
			issue['what'] = getWhat(i.body.splitlines()[count+2 :count+9])
		if(line == '## When?'):
			count_where = 0
			for countNext, sl in enumerate(i.body.splitlines()[count:]):
				if(sl == "## Where?"):
					count_where = count + countNext
			issue['month'] = getWhen(i.body.splitlines()[count+1 :count_where])
	list_of_issues.append((issue))
	print(issue)
	
with open('data.json', 'w') as outfile:
    json.dump(list_of_issues, outfile)

