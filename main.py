import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import *
from flask import Flask, redirect, url_for, render_template, request
from mailgun import send_message_mailgun

text = "your message"
subject = "subject of message"
recipient = "alexanisandr@email.com"
sender = "foo@" + "sandboxe1b6d6fde10947e5bda8e97a756f59c2.mailgun.org"
smtp_login = "postmaster@sandboxe1b6d6fde10947e5bda8e97a756f59c2.mailgun.org"
smtp_server = "smtp.mailgun.org"
password = "98eee30ec43cdaace3db16649ed1dfbc-c9746cf8-07fb9912"
port = 587

server = Flask(__name__)

@server.route('/')
def start():
    return redirect(url_for('mainpage'))

@server.route('/mainpage', methods=['GET'])
def mainpage():
    return render_template('mainpage.html')

@server.route('/contracts/health_insurance/<price>', methods=['GET']) # Health
def form_health(price):
    return render_template('contracts/insurance_health_form.html', price=price)
@server.route('/contracts/auto_insurance/<price>', methods=['GET'])
def car_form(price):
   print(price)
   cars = ["Audi", "Mazda", "Volkswagen", "BMW", "Mercedes", "Chevrolet", "Renault", "Peugeot", "Fiat","Ford", "Honda",
           "Hyundai", "Toyota", "Nissan", "Daewoo", "Mitsubishi", "Porsche", "Ferrari",
           "Lamborghini", "Bugatti", "Dodge", "Chrysler", "Rolls-Royce", "Cadillac", "Cherry", "Citroen",
           "Dacia", "Geely", "Hummer", "Infiniti", "Jaguar", "Jeep", "Kia", "Lexus", "Mercedes-Benz",
           "Land Rover", "Range Rover", "Lotus", "Lincoln", "Maserati", "Maybach", "Opel", "Seat", "Subaru",
           "Skoda", "Tesla", "Volvo", "VAZ", "ZAZ", "UAZ", "Moskvich"
           ]
   cars.sort()
   return render_template('contracts/car_insurance_form.html', price=price, cars=cars)
@server.route('/contracts/household_insurance/<price>', methods=['GET'])
def new_contract(price):
    return render_template('contracts/flat_form.html', price=price)
@server.route('/contracts/property_insurance/<price>', methods=['GET'])
def property_insurance(price):
    return render_template('contracts/property_insurance.html', price='pro')

@server.route('/contracts/cases',methods=['GET'])
def cases():
    return render_template('contracts/insurance_case.html')

@server.route('/contact', methods=['GET', 'POST'])
def contact():
   if request.method == 'GET':
      return render_template('contact.html')
   else:
      send_message_mailgun(text, subject, recipient, sender, smtp_login, password, smtp_server, port)
      return render_template('contact.html')

@server.route('/users/login', methods=['GET'])
def login():
    return render_template('users/sign_in.html')
@server.route('/users/register', methods=['GET'])
def register():
    return render_template('users/registration.html')
@server.route('/users/logout')
def logout():
    return render_template('mainpage.html')


if __name__ == '__main__':
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))