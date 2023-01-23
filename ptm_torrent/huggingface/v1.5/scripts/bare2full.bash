#! /bin/bash

fullRepo=$(echo $1 | sed 's/.git$//')
remote=$(git -C $1 remote get-url origin)

git clone -l $1 $fullRepo
git -C $fullRepo remote set-url origin $remote
git -C $fullRepo lfs fetch --all
git -C $fullRepo lfs checkout
git -C $fullRepo restore --source=HEAD :/
