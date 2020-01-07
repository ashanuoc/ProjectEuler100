% Project Euler problem 1

clc
clear

tic

n = 1000;

total = sum(0:3:n-1) + sum(0:5:n-1) - sum(0:15:n-1)
 
toc