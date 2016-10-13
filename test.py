#!/usr/bin/env python
# -*- coding:utf-8 -*-
#  Author: Jason Wang


namespace = {'name':'xs','data':[18,73,84]}
code =  '''def hellocute():return  "name %s ,age %d" %(name,data[0],) '''

func = compile(code, '<string>', "exec")
print(func)


# exec(func in namespace)

result = namespace['hellocute']()

print(result)