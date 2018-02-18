#!/bin/sh
#
# Author: Rongyang Sun <sun-rongyang@outlook.com>
# Date: 2018-02-18 09:34
# Last Modified Date: 2018-02-18 09:34
# Last Modified By: Rongyang Sun <sun-rongyang@outlook.com>
# 
# Description: Generate the publish version of the sun-rongyang.github.io and
#              push to https://github.com/sun-rongyang/sun-rongyang.github.io
#

make publish

git add .
git commit -m "$1"
git push origin master

cd output
git add .
git commit -m "Update blog"
git push origin master
cd ..
