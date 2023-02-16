import requests, json

TOKEN = "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"
BASE_URL = "https://api.github.com/"
header = {
    "Accept": "application/vnd.github+json",
    'Authorization': "Bearer {}".format(TOKEN)
}
owner = "sanyam121R"
repo = "about2020"
username = "AnujKV123"


def list_repo():
    ''' 1. List repository collaborators --------- GET  --   /repos/{owner}/{repo}/collaborators '''
    
    list_repo_url = BASE_URL + ("repos/{}/{}/collaborators".format(owner, repo))
    request_list_repo = requests.get(list_repo_url, headers=header)

    print("\n-- 1. List repository collaborators --------- GET  --   /repos/owner/repo/collaborators")

    print(request_list_repo.url)
    print(request_list_repo)
    # print(json.loads(request_list_repo.text))


def user_repo_coll():
    print("\n-- 2. Check if a user is a repository collaborator ------ GET  --   /repos/owner/repo/collaborators/username")
    
    user_repo_coll_url = BASE_URL + ("repos/{}/{}/collaborators/{}".format(owner, repo, owner))
    request_user_repo_coll = requests.get(user_repo_coll_url, headers=header)

    print(request_user_repo_coll, request_user_repo_coll.url)


def add_repo_coll():
    print("\n-- 3. Add a repository collaborator ---------- PUT  --   /repos/owner/repo/collaborators/username")
    
    add_repo_coll_url = BASE_URL + ("repos/{}/{}/collaborators/{}".format(owner, repo, owner))
    request_add_repo_coll = requests.put(add_repo_coll_url, headers=header)

    print(request_add_repo_coll, request_add_repo_coll.url)
    print(request_add_repo_coll.text)



def rm_repo_coll():
    print("\n-- 4. Remove a repository collaborator ---------  DELETE --  /repos/owner/repo/collaborators/username")

    rm_repo_coll_url = BASE_URL + ("repos/{}/{}/collaborators/{}".format(owner, repo, username))
    request_rm_repo_coll = requests.delete(rm_repo_coll_url, headers=header)

    print(request_rm_repo_coll, request_rm_repo_coll.url)



def repo_perm_url():
    print("\n-- 5. Get repository permissions for a user ------- GET  --   /repos/owner/repo/collaborators/username/permission")

    repo_perm_url = BASE_URL + ("repos/{}/{}/collaborators/{}/permission".format(owner, repo, username))
    request_repo_perm = requests.delete(repo_perm_url, headers=header)

    print(request_repo_perm, request_repo_perm.url)



## Repository invitations

def list_rep_invi_url():
    print("\n-- 6. List repository invitations --------- GET  --   /repos/owner/repo/invitations")
    
    list_rep_invi_url = BASE_URL + ("/repos/{}/{}/invitations".format(owner, repo))
    request_list_rep_invi = requests.get(list_rep_invi_url, headers=header)

    print(request_list_rep_invi)
    print(request_list_rep_invi.text)




list_repo()
user_repo_coll()
add_repo_coll()
rm_repo_coll()
repo_perm_url()
list_rep_invi_url()




# ----- OUTPUT ------------------#####################
'''

https://api.github.com/repos/sanyam121R/about2020/collaborators
<Response [200]>
<Response [204]> https://api.github.com/repos/sanyam121R/about2020/collaborators/sanyam121R
<Response [422]> https://api.github.com/repos/sanyam121R/about2020/collaborators/sanyam121R
{"message":"Validation Failed","errors":[{"resource":"Repository","code":"custom","message":"Repository owner cannot be a collaborator"}],"documentation_url":"https://docs.github.com/rest/reference/repos#add-a-repository-collaborator"}
<Response [204]> https://api.github.com/repos/sanyam121R/about2020/collaborators/asdf
<Response [404]> https://api.github.com/repos/sanyam121R/about2020/collaborators/asdf/permission

'''