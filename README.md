*******************************************************************
create new repository on the command line
*******************************************************************
echo "# DailyPractice" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/okute5014/DailyPractice.git
git push -u origin main
*********************************************************************
 push an existing repository from the command line
*********************************************************************
git remote add origin https://github.com/okute5014/DailyPractice.git
git branch -M main
git push -u origin main
