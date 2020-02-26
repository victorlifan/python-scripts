flowers = {}
with open('flowers.txt','r') as f:
	for line in f:
		line_sp = line.strip().split(':',2)
		flowers[line_sp[0]] = line_sp[1]


fullname = input('Enter your First [space] Last name only:')
fn = fullname.split(' ')[0]
related_flower = flowers[fn[0].upper()]
print('Unique flower name with the first letter:', related_flower)
