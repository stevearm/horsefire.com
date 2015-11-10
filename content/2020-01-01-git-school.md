Title: Git School
Date: 2020-01-01T01:01
Tags: git, learning

"Git is not a Prius. Git is a Model T. Its plumbing and wiring sticks out all over the place." - [Nick Farina](http://nfarina.com/post/9868516270/git-is-simpler)

Git is a great source control system, but because of its power, programmers really need to learn it or they can shoot themselves in the foot. There are tons of articles walking through how to get started.  it's like a Model T, the internals hang out all over the place.

https://try.github.io/levels/1/challenges/1

I was reading an article about education through exploring and [getting the problem-solution ordering correct](http://mkremins.github.io/blog/doors-headaches-intellectual-need/) and realized I need to find/make a real tutorial for git school. It should:

* Show simple commits
* Show amend commits
* Show merge
* Show how a merge can hide code changes
* Show rebasing
* Show how to rebase if all commits are conflicting (do a squash first?)

Each lesson should let the user explore. They should be doing local commits and edits. See the conflict happen and resolve it interactively on their own computer. Many articles just say what to do, but they don't come with a repo that sets up the scenarios. Some interactive tutorials exist, but they seem geared towards getting people from 0 to basic usability, not how to get a 

* http://pcottle.github.io/learnGitBranching/

## Prerequisites

This tutorial assumes:

* You have git and gitk installed on your computer
* You have a [github.com](https://github.com) account with ssh keys properly setup
* You've learned how to add and commit changes, and have (at least blindly) done merges and pushes

## Prepare

 1. Fork [github.com/stevearm/git-school](https://github.com/stevearm/git-school) into your own account
 2. Clone copies of the new git-school fork to your machine

    mkdir -p ~/git-school
    cd ~/git-school
    git clone git@github.com:myuser/git-school alice
    cd alice
    git config user.email alice@git-school.horsefire.com
    git config user.name Alice
    git clone git@github.com:myuser/git-school bob
    git config user.email bob@git-school.horsefire.com
    git config user.name Bob

## Lesson 1 - Pull and merge change before push

To introduce rebases and how they

Alice
1. Check out lesson_1 on Alice
1. Open gitk on Alice
1. Make a change
1. Commit it (do not push)
1. Refresh gitk (see your branch ahead of origin)

Bob
1. Check out lesson_1 on Bob
1. Open gitk on Bob
1. Make a change
1. Commit it (do not push)
1. Refresh gitk (see your branch ahead of origin)
1. Push your change to origin
1. Refresh gitk (see that origin now points to the new path)

Alice
1. Try to push (see the problem)
1. Do a pull (causes a merge)
1. Refresh gitk (see the local merge)
1. Do a push
1. See everything is synced on gitk

## Lesson 2 - Local rebase to avoid merges

Alice
1. Check out lesson_2 on Alice
1. Open gitk on Alice
1. Make a change
1. Commit it (do not push)
1. Refresh gitk (see your branch ahead of origin)

Bob
1. Check out lesson_2 on Bob
1. Open gitk on Bob
1. Make a change
1. Commit it (do not push)
1. Refresh gitk (see your branch ahead of origin)
1. Push your change to origin
1. Refresh gitk (see that origin now points to the new path)

Alice
1. Try to push (see the problem)
1. Do a fetch
1. Refresh gitk (see the difference)
1. Rebase on top of origin/lesson_2


## Lesson 2 - Amend a commit and change history

Alice
1. Check out a given branch on Alice
1. Open gitk on Alice
1. Make a change
1. Commit it (do not push)
1. Refresh gitk (see your branch ahead of origin)

Bob
1. Check out the same branch on Bob
1. Open gitk on Bob
1. Fix a line changed in the most recent commit
1. Amend the commit
1. Refresh gitk (see the difference)
1. Force push your change to origin
1. Refresh gitk (see that origin now points to the new path)

Alice
1. Try to push (see the problem)
2. 

## Lessons
* I have a ton of changes, and master got formatted, how do I fix this
* Answer: Format your changes, then create a new commit that changes from formatted master to formatted yourbranch
