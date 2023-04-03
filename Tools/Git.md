# Git

## Data model

Git use a directed acyclic graph. Each node is a commit containing

- Snapshot
- Author
- Message

Data types

```
blob = array<byte>
tree = map<string, tree | blob>
commit = struct{
	parents: array<commit>, 
	author: string, 
	message: string, 
	snapshot: tree
}
object = blob | tree | commit
objects = map<string, object>

def store(o):
	id = sha1(o)
	objects[id] = o

def load(id):
	return objects[id]

references = map<string, string>, from human readable to hash key
```

## Commands

- `git log --all --graph --decorate`: show the history as a graph
  - `git log --all --graph --decorate --oneline`: show one line of each node
- `git checkout <n>`: checkout the commit hash of a previous commit. `<n>` is the prefix of a hash. This will change the files to the snapshot of the previous commit, and the HEAD to the previous commit
  - `git checkout master`: set the HEAD to master
  - `git checkout <fileName>`: set the content of `fileName` to the one in the snapshot where HEAD points to
- `git diff <commitHash> <fileName>`: show the changes to the file `fileName` since the commit `commitHash`
  - By default, files are compared to HEAD
- `git branch <branchName>` : create a new branch, a reference pointing to the HEAD
- `git merge <branchName>`: merge the branch `<branchName>` into the current branch
  - The programmer needs to fix some conflicts. 
  - Then `git add` the file that has is changed manually to fix conflicts
  - Then `git merge --continue`
- `git remote`: list all the remote repositories.
  - `git remote add <remoteName> <remoteUrl>`: remoteName is default to `origin`
- `git push <remoteName> <localBranch>:<remoteBranch>`
- Maintain the relationship between local branches and remote branches
  - `git branch --set-upstream-to=<remoteBranch>`: after this command, can just call  `git push` to push commits.
- `git pull`:
  - = `git fetch <remote>` + `git merge`

- `git clone --shallow`: just have the lastest snapshot of the remote repostiory
- `git stash`: save the changes and return the content to the state it was the last commit
  - `git stash pop`: undo the stach
- Specify names of the files that don't want to be tracked in the `.gitignore` file.