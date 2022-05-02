import json
import smtplib
import pywhatkit
import os

with open('quiz.json') as openfile:
    check = json.load(openfile)

Name = input("enter the name : ").upper()
Email_id = input("Enter the Email-id: ")
score = 0
wrong = 0
val = 0

print("***** Welcome to World quiz *****")
for i in check:
    print("Choose the best answer: ")
    val = val + 1
    print("question number :  ", val, check[i])
    print("Option1 : ", check[i]["a"])
    print("Option2 : ", check[i]["b"])
    print("Option3 : ", check[i]["c"])
    print("Option4 : ", check[i]["d"])

    answer = input("please enter anyone option: a/b/c/d: ").lower()
    if answer == check[i]["Correct answer"]:
        score = score + 1
        print("congratulations you got one point")
    else:
        wrong = wrong + 1
        print("wrong answer")
a = "Total number of question you have answered: ", val
b = "Number of wrong answer is: ",wrong
c = "Total score is:", score
d = (score/val) * 100
e = round(d)


print(a)
print(b)
print(c)
print("Percentage is",e)

string1 = "1.user name is {}".format(Name)
string2 = "2.Total number of question you have answered{}".format(val)
string3 = "3.Number of the correct answer is{}".format(score)
string4 = "4.Number of the wrong answer is{}".format(wrong)
string5 = "5.Percentage is {}".format(e)

msg = string1+os.linesep+string2+os.linesep+string3+os.linesep+string4+os.linesep+string5

print(msg)

main = smtplib.SMTP_SSL('smtp.gmail.com', 465)

send = 's.gangadharan07@gmail.com'
password = 'g123456.'
rec = 's.gangadharan07@gmail.com'
main.login(send, password)
main.sendmail(send,
              rec,
              msg)
print("mail sent successfully")

pywhatkit.sendwhatmsg("+919655135540",msg, 12,40)
