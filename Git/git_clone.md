# Git Clone
https://devconnected.com/how-to-clone-a-git-repository/

### clone all the repository with all the versions and branches
`git clone <remote_repo>`

### Git clone a specific branch
notice that you are fetching all the branches but you are checking out the branch you chose

`git clone -b <branch_or_tag_name> <remote_repo>`
  
### Git clone exclusively one branch
`git clone --single-branch --branch <branch_or_tag_name> <remote_repo>`
