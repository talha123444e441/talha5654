# Inteligent Wordlist Generator
#
# By: Online Hacking [SUMAN MONDAL]
# Goblin Wordlist Generator
# Version: 2.0
#
#
##################
 
import itertools
 
 
ban = '''
 
                                                    '''
 
print('''\033[91m
 
     
.------..------..------..------..------.
|T.--. ||A.--. ||L.--. ||H.--. ||A.--. |
| :/\: || (\/) || :/\: || :/\: || (\/) |
| (__) || :\/: || (__) || (__) || :\/: |
| '--'T|| '--'A|| '--'L|| '--'H|| '--'A|
`------'`------'`------'`------'`------'
  
                                                               		 
                     \033[93mMr Hacking (\033[96mTALHa\033[93m) 
''')
print('''\033[92m
     
                                          
                                          
  ,----..    .--.--.       ,---,.         
 /   /   \  /  /    '.   ,'  .'  \        
|   :     :|  :  /`. / ,---.' .' |        
.   |  ;. /;  |  |--`  |   |  |: |        
.   ; /--` |  :  ;_    :   :  :  /        
;   | ;     \  \    `. :   |    ;         
|   : |      `----.   \|   :     \        
.   | '___   __ \  \  ||   |   . |        
'   ; : .'| /  /`--'  /'   :  '; |        
'   | '/  :'--'.     / |   |  | ;         
|   :    /   `--'---'  |   :   /          
 \   \ .'              |   | ,'           
  `---`                `----'             
                                          

''')
print('''\033[91m
        \033[91m [\033[96m*\033[91m] \033[97mWebsite  \033[91m=  \033[4m\033[1; 97mHttps.teamcsb.com \033[24m
 
        \033[91m [\033[96m*\033[91m] \033[97mTelegram \033[5m\033[1;91m=  \033[97m@teamcsb   \033[25m 
	
	\033[91m [\033[96m*\033[91m] \033[97mFacebook \033[1;91m= \033[5m \033[97mAbu Talha \033[25m
''')
 
scale = input('\033[36m[!] provide a size scale [eg: "4 to 8" = 4:8] : ')
start = int(scale.split(':')[0])
final = int(scale.split(':')[1])
 
use_nouse = str(input("\n\033[36m[?] Do you want to enter personal data ? [y/N]: "))
if use_nouse == 'y':
	first_name = str(input("\n\033[36m[*] Fist Name: "))
	last_name = str(input("\n\033[36m[*] Last Name: "))
	birthday = str(input("\n\033[36m[*] Birthday: "))
	month = str(input("\n\033[36m[*] Month: "))
	year = str(input("\n\033[36m[*] Year: "))
	chrs = first_name + last_name + birthday + month + year
else:
	chrs = 'abcdefghijklmnopqrstuvwxyz'
	pass
 
chrs_up = chrs.upper()
chrs_specials = '!\][/?.,~-=";:><@#$%&*()_+\' '
chrs_numerics = '1234567890'
 
file_name = input('\n\033[36m[!] Insert a name for your wordlist file: ')
arq = open(file_name, 'w')
if input('\n\033[36m[?] Do you want to use uppercase characters? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_up])
if input('\n\033[36m[?] Do you want to use special characters? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_specials])
if input('\n\033[36m[?] Do you want to use numeric characters? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_numerics])
 
for i in range(start, final+1):
	for j in itertools.product(chrs, repeat=i):
		temp = ''.join(j)
		print(temp)
		arq.write(temp + '\n')
arq.close()
