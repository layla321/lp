# import requests
import pandas as pd
from github import Github

from access_info import access_token

# auth = Auth.Token(access_token)
g = Github(login_or_token=access_token)
gh_user = g.get_user('layla321')
gh_repos = gh_user.get_repos()
print(list(gh_repos))

# wiki_url = r1.html_url+'/wiki/Info'
# print(r1.html_url)
# print(f'Accessing {wiki_url}')
# response = requests.get(wiki_url)
# r2 = requests.get("https://github.com/layla321/brightwheel-crawler/wiki/Info")
# https://github.com/layla321/brightwheel-crawler/wiki/Info

# Create class for repo or class for authors

all_repo_data = pd.DataFrame(columns=['name', 'num_stars', 'topics', 'num_commits'])
all_repo_l = []

for repo in gh_repos:
    
    # Get repo attributes
    num_stars = repo.stargazers_count
    topics = ", ".join(repo.get_topics())
    num_commits = repo.get_commits().totalCount
    contrib_list = ", ".join([x.login for x in repo.get_contributors()])
    most_recent_commit = str(repo.get_commits().get_page(0)[0].commit.author.date)[:10]
    num_open_issues = int(len(list(repo.get_issues(state='open'))))
    description = repo.description
    # contrib_stats = repo.get_stats_contributors()
    
    # Get commits by author
    commit_dict = {}
    for commit in repo.get_commits():
        COMMIT_AUTHOR = str(commit.commit.author.name)
        if COMMIT_AUTHOR not in commit_dict:
            commit_dict[COMMIT_AUTHOR] = 1
        else:
            commit_dict[COMMIT_AUTHOR] += 1
            
    # Read test section
    readme_content = repo.get_contents("README.md").decoded_content.decode()
    try:
        test_section = str(readme_content).split("Test section")[1].split("#")[0].strip()
    except IndexError:
        test_section = 'test section not found'
    
    # Aggregate repo data
    repo_data = {"Project Name":repo.name,
                 "Description":description,
                 'Contributors':contrib_list,
                 'Topics':topics, 
                 'Most Recent Commit':most_recent_commit,
                 'Num. Commits':num_commits,
                 'Num. Open Issues':num_open_issues,
                 'Num. Stars':num_stars, 
                 'Commit dict':commit_dict,
                 'Test section':test_section,
                 }
    
    # Append repo data
    all_repo_l.append(repo_data)
    
all_repo_data = pd.DataFrame(all_repo_l).sort_values(by=['Project Name'])
all_repo_data.to_markdown('test.md')
all_repo_data.to_csv('test.csv')
print(all_repo_data[['Topics','Num. Open Issues']].head())

