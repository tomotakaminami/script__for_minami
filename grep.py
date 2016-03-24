# -*- coding: utf-8 -*-
import os
import subprocess
import sys

#cmd='grep class AbstractExecutionAwareRequest.java'
cmd='ls *.java'
result=subprocess.check_output(cmd, shell=True)
result = result.replace('\r', '')
result_list=result.split('\n')
result_list.pop()
for i in result_list:
	print i
	cmd='grep "class" ' + i
	try:
		result = subprocess.check_output(cmd, shell=True)
	except subprocess.CalledProcessError:
		continue
	sa=result.split(' ')
	classs=sa.index('class')
	print sa[classs+1]
	
