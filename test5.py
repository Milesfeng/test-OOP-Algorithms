# -*- coding: utf-8 -*-

import numpy as np

a = np.array([77,5,5,22,13,55,97,4,796,1,0,9])
b = np.array(range(10))
c = np.array([],dtype='i')
d = np.array([],dtype='i')
e = np.array([],dtype='i')

# =============================================================================
# 1. 陣列 c = 陣列a 交集 陣列b  
# =============================================================================

if len(a) <= len(b):
    for i in range(len(a)):
        if a[i] in b and a[i] not in c:
            c = np.append(c,a[i])
else:
    for i in range(len(b)):
        if b[i] in a and b[i] not in c:
            c = np.append(c,b[i])
            
# =============================================================================
# 2. 陣列d = 陣列a 差集 陣列b
# =============================================================================

for i in range(len(a)):
    if a[i] not in d and a[i] not in b:
        d = np.append(d,a[i])
        
# =============================================================================
# 3. 陣列e = 陣列a 聯集 陣列b 
# =============================================================================

for i in range(len(a)):
    if a[i] not in e:
        e = np.append(e,a[i])
        
for i in range(len(b)):
    if b[i] not in e:
        e = np.append(e,b[i])