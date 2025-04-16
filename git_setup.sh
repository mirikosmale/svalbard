# setup your github
#-------------------------------------------------------------------------
## done only once; repository exists  
# echo "# svalbard" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin git@github.com:mirikosmale/svalbard.git
# git push -u origin main

### setup:
git init  
#### check remote connection  
git remote -v  
git remote add svalbard_ssh git@github.com:mirikosmale/svalbard.git  
git remote add svalbard https://github.com/mirikosmale/svalbard.git  
# git remote remove svalbard_ssh
# git remote remove svalbard
git remote -v  
git config user.email "mirikosmale@github.com"  
git config user.name "mirikosmale"  
git branch -M master  
#-------------------------------------------------------------------------
### first push:
#### on development server:
git add .  
git add bash_code  
git add python_code  
git add settings  
git commit -a -m 'first commit'  
####
git push -u svalbard_ssh master  
#-------------------------------------------------------------------------
### first pull:
#### on target server first pull:
# git remote add origin git@github.com:mirikosmale/svalbard.git
# git branch -M main
# git push -u origin main
# git pull g3p_oper_ssh master
git stash
git pull svalbard_ssh master
chmod -R 755 .

