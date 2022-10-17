roman = input("Enter the Roman symbols: ")

def romanToInt(s:str) -> int:
        
        dic= {'I': 1,
              'V': 5,
              'X': 10,
              'L': 50,
              'C': 100,
              'D': 500,
              'M': 1000
              }
        
        previous =0
        current =0
        total = 0
            
        for i in range(len(s)):
          current= dic[s[i]]
          if current>previous:
              total = total+ current - 2*previous
          else :
              total += current
                  
          previous =current
        return total
    
p= romanToInt(roman)
print(f"the number written in roman evaluates to: {p}")

# another solution:

# from re import S

# roman = input("Enter the Roman symbols: ")

# def roman_to_int(r):
#     symbols = ['I','V','X','L','C','D','M']
#     values = [1,5,10,50,100,500,1000]
#     I = {'V','X'}
#     X = {'L','C'}
#     C = {'D','M'}
#     key_val = dict(zip(symbols,values))
#     num = 0
#     for i in range(0,len(r)):
#         st = r[i:i+2]     
#         if (st[0] == 'I' and st[-1] in I) or (st[0] == 'X' and st[-1] in X) or (st[0] == 'C' and st[-1] in C):
#             num -= key_val[r[i]]
#         else:
#             num += key_val[r[i]]
     
#     return num

# print(f"the number written in roman evaluates to: {roman_to_int(roman)}")