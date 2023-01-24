import os

from config import *
from flask import Flask, redirect, url_for, render_template

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

@server.route('/contact', methods=['GET'])
def contact():
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