f_in = open('supplementary_tableS1.txt')
f_out = open('disease_names.txt', 'w')

f_out.write(f_in.readline())

for line in f_in:
	did, name = line.strip().replace('"', '').split('\t')[:2]
	name = name.split(',')[0]
	f_out.write('%s\t%s\n' % (did, name))

f_in.close()
f_out.close()
