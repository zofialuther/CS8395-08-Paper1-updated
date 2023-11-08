def max_list(L, V):
   R = [x for x in L if x == V]
   for X in R:
      if X > V:
         return False
   return True