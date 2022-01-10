from instapy import InstaPy
from instapy import smart_run
#COMMENT OUT THE BELOW PART TO MAKE IT WORK
#====================================================#
print('\n')
print("[-] PROJECT TEMPORARILY CLOSED..../")
print('\n')
print('\n')
print("[-] WILL BE CONTINUED LATER..../")
print('\n')
project_int = str(input("PRESS X TO EXIT: "))

if project_int == 'X':
    exit()

else:
    exit()

exit()

#====================================================#

username_insta = str(input("[+] Enter Your Username: "))
password_insta = str(input("[+] Enter Your Password: "))
gui = input("[+] GUI Enabled/Disabled: ")



if gui == 'enabled':
    E_GUI = False
else:
    E_GUI = True

#session = InstaPy("username=str({username_insta}), password=str({password_insta}),headless_browser=False".format(username_insta,password_insta))

session = InstaPy(username=username_insta, password=password_insta,headless_browser=E_GUI)
#session = InstaPy(username="darkestbrush", password="charms1234",headless_browser=False)

session.login()

#session.like_by_tags(['penandink', 'inkartworks'], amount= 4)


input_by_tags = input("[+] Search With Tags ? [ Y/N ]: ")
input_by_location = input("[+] Search With Location ? [ Y/N ]: ")


input_by_location = str(input_by_location)
input_by_tags = str(input_by_tags)





if input_by_tags == "Y":
    #with smart_run(session):
        enter_tags = input("[+] Enter Your 1st tag you want: ")
        enter_tags_2 = input("[+] Enter Your 2nd tag you want: ")

        #enter_tags = str(enter_tags)
        #enter_tags_2 = str(enter_tags_2)
        enter_amount_of_likes_for_tags = int(input("[+] Enter amount of likes MAX = 10: "))

        print("liked by tags started...")
        #print(f"tag_1: {enter_tags} tag_2: {enter_tags_2} , amount: {enter_amount_of_likes_for_tags}")

        #print(session.like_by_tags(f"['{enter_tags}', '{enter_tags_2}'], amount={enter_amount_of_likes_for_tags}"))
        session.like_by_tags([enter_tags, enter_tags_2], amount=enter_amount_of_likes_for_tags)


elif input_by_location == 'Y':
    #enter_location = input("[+] Enter The Location: ")
    enter_amount_of_likes_for_locations = int(input("[+] Enter amount of likes MAX = 10: "))
     
    session.like_by_locations(['213601591/vadodara-gujarat-india/'], amount = 5, skip_top_posts = False)
    

    enter_location_output = input("[+] Enter The Location With Input? Y/N: ")
    

elif input_by_location == 'N':
    print('\n')
    print("bro if you dont want it go find someone else")
    print('\n')
    session.end()

if enter_location_output == 'Y':
    enter_location = input("[+] Enter The Location (Eg: 213601591/vadodara-gujarat-india/): ")
    enter_amount_of_likes_for_locations = int(input("[+] Enter amount of likes MAX = 10: "))
    #session.like_by_locations(['c1018450/baroda-india/'], amount = enter_amount_of_likes_for_locations, skip_top_posts = False)
    session.like_by_locations([enter_location], amount = 5, skip_top_posts = False)

else:
    print('\n')
    print("Sorry I Cant Do Anything, Its Your Problem Figure It Out Yourself Pshh ")

session.end()




#session.like_by_locations(['213601591/vadodara-gujarat-india/'], amount = 5, skip_top_posts = False)

#session.like_by_locations(['c1018450/baroda-india/'], amount = 5, skip_top_posts = False)

#print(session.like_by_locations)

#print(session)
