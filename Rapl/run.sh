#!/bin/sh

for dir in $(find . -type d);
do
  (
    cd $dir;
    make compile;
    make measure;
    make mem;
  )
done
