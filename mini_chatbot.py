import webbrowser
import datetime

print("say something")
b = input()
a = ['hey', 'hai', 'hello', 'who are you', 'who created you', 'what is the weather today', 'what is the important news'
                                                                                           ' today', '1', '2',
     'you tube', 'facebook', 'instagram', 'Exit', ]

if b == a[0] or [1] or [2]:
    print('hello')
    print("what's your name")
else:
    print('hello')
    print("what's your name")
name = input()
print('ok ' + name + ' what you want from me')
print('(who are you ? or who created you )')
c = input()


def Exit():
    print('Thank you See you Next time!!.....')



def calling():
    global c
    if c == a[3]:
        print('iam chat bot')
    elif c == a[4]:
        print("muhzin")
    elif c == a[12]:
        return Exit()
    else:
        print("please Enter the questions")
        c = input()
        return calling()


calling()


def Goal():
    global c
    c = input('you want calculate your goal deadline days')
    if c == "yes":
        print('ok')
    elif c == 'no':
        return Exit()
    else:
        print('please say yes or no..')
        c = input()

    user_input = input("Enter your goal with a deadline separated by colon\n")
    input_list = user_input.split(":")

    goal = input_list[0]
    deadline = input_list[1]

    deadline_data = datetime.datetime.strptime(deadline, "%d.%m.%Y")
    today_data = datetime.datetime.today()
    time_till = deadline_data - today_data

    # hours_till = int(time_till.total_second() / 60 / 60)
    print(f"dear user time remaining for your goal: {goal} is {time_till.days} ")

    return Exit()


def social_media():
    global c
    print("which social media you want ?" + ' ,' + a[9] + ' ,' + a[10] + ' ,' + a[11] + " ," + a[12])
    c = input()
    if c == a[9]:
        print('https://www.youtube.com/')
        return Goal()
    elif c == a[10]:
        print('https://www.facebook.com/')
        return Goal()
    elif c == a[11]:
        print('oops!!...link not available')
        return Goal()
    elif c == a[12]:
        return Exit()
    else:
        print('choose any one')
        return social_media()


def social():
    global c
    print('you want any information ?' + ' Enter 1 ' + a[5] + ', Enter 2 ' + a[6] + " ," + a[12])
    c = input()
    if c == a[7]:
        print('https://www.accuweather.com/en/in/perinthalmanna/2875723/weather-forecast/2875723')
        social_media()
    elif c == a[12]:
        Exit()
    elif c == a[8]:
        print("https://www.bbc.com/news")
        social_media()
    elif c == 'no':
        social_media()
    else:
        print('choose any one')
        return social()


social()

# webbrowser.open('https://www.accuweather.com/en/in/perinthalmanna/2875723/weather-forecast/2875723')
