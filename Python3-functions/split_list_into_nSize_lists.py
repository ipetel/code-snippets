	'''
	  this function split given list by using N value into small list in size of N.
    if the last group is not big enough, the last list will be in the size that was left.
    
    for example let's say you have the next list: [1,2,3,4,5,6,7,8,9,10]
    when you will send this list to the function with N=4 the result will be: [[1,2,3,4],[5,6,7,8],[9,10]]
	'''

def split_list_into_nSize_lists(data_list,N):
	if isinstance(data_list,list):
		new_list=[]
		count_list_elem=len(data_list)
		num_of_sub_lists=round(count_list_elem/N)
		
		i=0
		while i <= num_of_sub_lists:
			offset=N*i
			new_list.append(data_list[offset:offset+N])
			i+=1
			
		return new_list
	else:
		print('ERROR - Data provide is not a list type')
		return None
