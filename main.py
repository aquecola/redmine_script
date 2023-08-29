from redminelib import Redmine
from dotenv import load_dotenv, find_dotenv
import os

# change 'http://your-redmine-url' on URL yours Redmine

redmine_url = 'https://example.com'

# basic security

load_dotenv(find_dotenv())
env_key = (os.environ.get('KEY')) # api-key .env
api_key = env_key

redmine = Redmine(redmine_url, key=api_key)

def close_issues_by_title(project_id, issue_title):
    issues = redmine.issue.filter(project_id=project_id, status_id='open', subject=issue_title)
    
    NEW_STATUS_ID = 5 # ID 5 means closed
    for issue in issues:
        issue.status_id = NEW_STATUS_ID
        issue.save()
        print(f"Closed issue with ID {issue.id} - {issue.subject}")

# call function "close ticket by topic"

close_issues_by_title(1, "example title")
close_issues_by_title(1, "example title")
close_issues_by_title(1, "example title")
close_issues_by_title(1, "example title")
close_issues_by_title(1, "example title")