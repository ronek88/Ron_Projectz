l1 = [12541,12546,21659,16448,15488]
l2 = [1,1,1,1,1]
s = dict(zip(l1,l2))
print(s)

l1_after = [12541,12546,21659,16448,15488]
l2_after = [0,0,0,0,0]
s2       = dict(zip(l1_after,l2_after))
print(s2)

keys_s = s.keys()
print(keys_s)

val_s  = s.values()
val_s2 = s2.values()

print(val_s)
print(val_s2)

print(s[12541])

len_d = len(s)
for i in keys_s:
    if s[i] == 0 and s2[i] == 1:
        print('All is OK for S1' + str(i) +'ID: ' + str(s[i]) + ' value, and for S2' + str(i) + 'ID: ' + str(s2[i]))
    elif s[i] == 1 and s2[i] == 0:
        print('All is OK for S1' + str(i) + 'ID: ' + str(s[i]) + ' value, and for S2' + str(i) + 'ID: ' + str(s2[i]))
    else:
        assert False

