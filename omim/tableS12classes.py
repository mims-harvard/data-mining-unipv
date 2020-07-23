f_in = open('supplementary_tableS1.txt')
f_out = open('disease_classes.txt', 'w')

f_out.write(f_in.readline())

dids = []
for line in f_in:
	line = line.strip().replace('"', '').split('\t')
	did, dclass = line[0], line[-1]
	f_out.write('%s\t%s\n' % (did, dclass))
	dids.append(did)

print('Different dids: %d Total number of dids: %d' % (len(set(dids)), len(dids)))
f_in.close()
f_out.close()
