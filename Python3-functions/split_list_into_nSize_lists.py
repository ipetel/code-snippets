	'''
	  this function split given list by using N value into small list in size of N.
    if the last group is not big enough, the last list will be in the size that was left.
    
    for example let's say you have the next list: [1,2,3,4,5,6,7,8,9,10]
    when you will send this list to the function with N=4 the result will be: [[1,2,3,4],[5,6,7,8],[9,10]]
	'''
from math import ceil
	
def split_list_into_nSize_lists(data_list,N):
	if isinstance(data_list,list):
		new_list=[]
		count_list_elem=len(data_list)
		num_of_sub_lists=ceil(count_list_elem/N)
		
		i=0
		while i <= num_of_sub_lists:
			offset=N*i
			if len(data_list[offset:offset+N])>0:
				new_list.append(data_list[offset:offset+N])
			i+=1
			
		return new_list
	else:
		print('ERROR - Data provide is not a list type')
		return None
'''
   this function return a list of tuples (start and end number) by using N value that indicates the size of the tuple's number range
    if the last group is not big enough, the last list will be in the size that was left.
    for example: 
    	split_int_into_nSize_lists(number=7,3)
	return: [(0,2),(3,5),(6,7)]
'''

def split_int_into_nSize_lists(number,N):
    if isinstance(number,int):
        new_list=[]
        num_of_sub_lists=ceil(number/N)
        print(num_of_sub_lists)
        
        i=0
        prev = 0
        while i <= num_of_sub_lists-1:
            offset=N*i
            
            if number > N*i+N:
                new_list.append((N*i,N*i+N-1))
            else:
                new_list.append((N*i,number))
            
            i+=1
            
        return new_list
    else:
        print('ERROR - Data provide is not a list type')
        return None
