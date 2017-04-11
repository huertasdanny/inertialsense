def cal_chksum(sentence):
	rmvchars = ['\r','\n','$']
	for c in rmvchars:
		sentence = sentence.strip(c)
	chksum_data = sentence[:sentence.find('*')]
	#print(chksum_data)
	chksum = 0
	for n in chksum_data:
		chksum ^=ord(n)
	return chksum
	
def chksum(sentence):
	cal_sum = hex(cal_chksum(sentence))
	temp = sentence.find('*')
	
	snt_sum = hex(int( sentence[temp+1:temp+3],16))
	if cal_sum == snt_sum:
		return True
	else:
		return False
def padzero(checksum):
	if len(checksum) == 1:
		return '0'+checksum
	else:
		return checksum
