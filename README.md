# git_assignment_HeroVired

Q1: CalculatorPlus Application
Step 1: Repository Setup via GitHub.com
* Created repository: `git_assignment_HeroVired`
* Cloned repository locally
# git clone https://github.com/learndevopsabhash/git_assignment_HeroVired
# cd git_assignment_HeroVired
Step 2: Created Development Branch
# git checkout -b dev
Step 3: Added Calculator Code -> CalculatorPlus.py
* Implemented give code:
Step 4: Commit & Push
# git add .
# git commit -m "CalculatorPlu"
# git push origin dev
Step 5: Merge to Main
# git checkout main
# git merge dev
# git push origin main
Step 6: Release Version 1
* Created release: `v1.0`
Step 7 Feature Branch (sqrt)
# git checkout -b feature/sqrt
* Implemented sqrt feature
* Created Pull Request
* Merged into `dev` and then `main`
Step 8: Release Version 2
* Created release: `v2.0`
Q2: Git LFS (Large File Storage)
Step 1: Install Git LFS
# git lfs install
Step 2: Create LFS Branch
# git checkout -b lfs
Step 3: Track Large Files
# git lfs track "*.zip"
Step 4: Add Large File (>200MB)
# git add .
# git commit -m "Added large 200MB file using Git LFS"
# git push origin lfs
Step 5: Verification
git clone https://github.com/learndevopsabhash/LinuxAssignment.git

* Verified large file downloads correctly
Q3: Geometry Calculator (Git Stash)
Step 1: Created Base Branch
# git checkout dev
# git checkout -b geometry-calculator
* Implemented:
Step 2: Circle Feature Branch
# git checkout -b feature/circle-area
* Added incomplete circle implementation & Used stash:
# git add .
# git stash push -m "circle incomplete"
Step 3: Rectangle Feature Branch
# git checkout -b feature/rectangle-area
* Added incomplete rectangle implementation & Used stash:
# git add .
# git stash push -m "rectangle incomplete"
Step 4: Completed Circle Feature
# git checkout feature/circle-area
# git stash apply stash@{1}
* Completed implementation & Committed and pushed
Step 5: Completed Rectangle Feature
# git checkout feature/rectangle-area
# git stash apply stash@{0}
* Completed implementation & Committed and pushed
Step 6: Pull Requests -> Created PRs:
  * `feature/circle-area → dev`
  * `feature/rectangle-area → dev`
Step 7: Merge
* Merged into `dev` -> `feature/circle-area → dev` then feature/rectangle-area → dev
* Then merged `dev → main`
# git checkout dev
# git merge feature/circle-area
# git push origin dev
# git merge feature/rectangle-area
# git push origin dev
# git checkout main
# git merge dev
# git push origin main

GitHub link - https://github.com/learndevopsabhash/git_assignment_HeroVired 
