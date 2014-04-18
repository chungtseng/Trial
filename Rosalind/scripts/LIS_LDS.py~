#The Recursive Solution
def recursive_solution(remaining_sequence, bigger_than=None):                    
  """Finds the longest increasing subsequence of remaining_sequence that is      
  bigger than bigger_than and returns it.  This solution is O(2^n)."""           
  # Base case: nothing is remaining.                                             
  if len(remaining_sequence) == 0:                                               
    return remaining_sequence                                                    
  # Recursive case 1: exclude the current element and process the remaining.     
  best_sequence = recursive_solution(remaining_sequence[1:], bigger_than)        
  # Recursive case 2: include the current element if it's big enough.            
  first = remaining_sequence[0]                                                  
  if (first > bigger_than) or (bigger_than is None):                             
    sequence_with = [first] + recursive_solution(remaining_sequence[1:], first)  
    # Choose whichever of case 1 and case 2 were longer.                         
    if len(sequence_with) >= len(best_sequence):                                 
      best_sequence = sequence_with                                              
  return best_sequence
#The O(n^2) Dynamic Programming Solution
def dynamic_programming_solution(sequence):                                      
  """Finds the longest increasing subsequence in sequence using dynamic          
  programming.  This solution is O(n^2)."""                                      
  longest_subsequence_ending_with = []                                           
  backreference_for_subsequence_ending_with = []                                 
  current_best_end = 0                                                           
  for curr_elem in range(len(sequence)):                                         
    # It's always possible to have a subsequence of length 1.                    
    longest_subsequence_ending_with.append(1)                                    
    # If a subsequence is length 1, it doesn't have a backreference.             
    backreference_for_subsequence_ending_with.append(None)                       
    for prev_elem in range(curr_elem):                                           
      subsequence_length_through_prev = (                                        
          longest_subsequence_ending_with[prev_elem] + 1)                        
      # If the prev_elem is smaller than the current elem (so it's increasing)   
      # And if the longest subsequence from prev_elem would yield a better       
      # subsequence for curr_elem.                                               
      if ((sequence[prev_elem] < sequence[curr_elem]) and                        
          (subsequence_length_through_prev >                                     
           longest_subsequence_ending_with[curr_elem])):                         
        # Set the candidate best subsequence at curr_elem to go through prev.    
        longest_subsequence_ending_with[curr_elem] = (                           
            subsequence_length_through_prev)                                     
        backreference_for_subsequence_ending_with[curr_elem] = prev_elem         
    # If the new end is the best, update the best.                               
    if (longest_subsequence_ending_with[curr_elem] >                             
        longest_subsequence_ending_with[current_best_end]):                      
      current_best_end = curr_elem                         
  # Output the overall best by following the backreferences.                     
  best_subsequence = []                                                          
  current_backreference = current_best_end                                       
  while current_backreference is not None:                                       
    best_subsequence.append(sequence[current_backreference])                     
    current_backreference = (                                                    
        backreference_for_subsequence_ending_with[current_backreference])        
  best_subsequence.reverse()                                                     
  return best_subsequence
#The O(n log n) Dynamic Programming Solution
def find_smallest_elem_as_big_as(sequence, subsequence, elem):                   
  """Returns the index of the smallest element in subsequence as big as          
  sequence[elem].  sequence[elem] must not be larger than every element in       
  subsequence.  The elements in subsequence are indices in sequence.  Uses       
  binary search."""                                                              
  low = 0                                                                        
  high = len(subsequence) - 1                                                    
  while high > low:                                                              
    mid = (high + low) / 2                                                       
    # If the current element is not as big as elem, throw out the low half of    
    # sequence.                                                                  
    if sequence[subsequence[mid]] < sequence[elem]:                              
      low = mid + 1                                                              
    # If the current element is as big as elem, throw out everything bigger, but 
    # keep the current element.                                                  
    else:                                                                        
      high = mid                                                                 
  return high    

def optimized_dynamic_programming_solution(sequence):                            
  """Finds the longest increasing subsequence in sequence using dynamic          
  programming and binary search (per                                             
  http://en.wikipedia.org/wiki/Longest_increasing_subsequence).  This solution   
  is O(n log n)."""                                                              
  # Both of these lists hold the indices of elements in sequence and not the        
  # elements themselves.                                                         
  # This list will always be sorted.                                             
  smallest_end_to_subsequence_of_length = []                                     
  # This array goes along with sequence (not                                     
  # smallest_end_to_subsequence_of_length).  Following the corresponding element 
  # in this array repeatedly will generate the desired subsequence.              
  parent = [None for _ in sequence]                                              
  for elem in range(len(sequence)):                                              
    # We're iterating through sequence in order, so if elem is bigger than the   
    # end of longest current subsequence, we have a new longest increasing          
    # subsequence.                                                               
    if (len(smallest_end_to_subsequence_of_length) == 0 or                       
        sequence[elem] > sequence[smallest_end_to_subsequence_of_length[-1]]):   
      # If we are adding the first element, it has no parent.  Otherwise, we        
      # need to update the parent to be the previous biggest element.            
      if len(smallest_end_to_subsequence_of_length) > 0:                         
        parent[elem] = smallest_end_to_subsequence_of_length[-1]                 
      smallest_end_to_subsequence_of_length.append(elem)                         
    else:                                                                        
      # If we can't make a longer subsequence, we might be able to make a        
      # subsequence of equal size to one of our earlier subsequences with a         
      # smaller ending number (which makes it easier to find a later number that 
      # is increasing).                                                          
      # Thus, we look for the smallest element in                                
      # smallest_end_to_subsequence_of_length that is at least as big as elem       
      # and replace it with elem.                                                
      # This preserves correctness because if there is a subsequence of length n 
      # that ends with a number smaller than elem, we could add elem on to the   
      # end of that subsequence to get a subsequence of length n+1.              
      location_to_replace = find_smallest_elem_as_big_as(                        
          sequence, smallest_end_to_subsequence_of_length, elem)                 
      smallest_end_to_subsequence_of_length[location_to_replace] = elem          
      # If we're replacing the first element, we don't need to update its parent 
      # because a subsequence of length 1 has no parent.  Otherwise, its parent  
      # is the subsequence one shorter, which we just added onto.                
      if location_to_replace != 0:                                               
        parent[elem] = (                                                         
            smallest_end_to_subsequence_of_length[location_to_replace - 1])         
  # Generate the longest increasing subsequence by backtracking through parent.  
  curr_parent = smallest_end_to_subsequence_of_length[-1]                        
  longest_increasing_subsequence = []                                            
  while curr_parent is not None:                                                 
    longest_increasing_subsequence.append(sequence[curr_parent])                 
    curr_parent = parent[curr_parent]                                            
  longest_increasing_subsequence.reverse()                                       
  return longest_increasing_subsequence
                                      
