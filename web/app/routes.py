from app import app, db, queue_client, cache
from datetime import datetime
from app.models import Attendee, Conference, Notification
from flask import render_template, session, request, redirect, url_for, flash, make_response, session
from azure.servicebus import Message
import logging

registrationCacheMessageKey = 'message'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        attendee = Attendee()
        attendee.first_name = request.form['first_name']
        attendee.last_name = request.form['last_name']
        attendee.email = request.form['email']
        attendee.job_position = request.form['job_position']
        attendee.company = request.form['company']
        attendee.city = request.form['city']
        attendee.state = request.form['state']
        attendee.interests = request.form['interest']
        attendee.comments = request.form['message']
        attendee.conference_id = app.config.get('CONFERENCE_ID')

        try:
            db.session.add(attendee)
            db.session.commit()
            cache.push(registrationCacheMessageKey, 'Thank you, {} {}, for registering!'.format(
                attendee.first_name, attendee.last_name))
            return redirect('/Registration')
        except:
            logging.error('Error occured while saving your information')

    else:
        if cache.exists(registrationCacheMessageKey):
            message = cache.peak(registrationCacheMessageKey)
            return render_template('registration.html', message=str(message))
        else:
            return render_template('registration.html')


@app.route('/Attendees')
def attendees():
    attendees = Attendee.query.order_by(Attendee.submitted_date).all()
    return render_template('attendees.html', attendees=attendees)


@app.route('/Notifications')
def notifications():
    notifications = Notification.query.order_by(Notification.id).all()
    return render_template('notifications.html', notifications=notifications)


@app.route('/Notification', methods=['POST', 'GET'])
def notification():
    if request.method == 'POST':
        notification = Notification()
        notification.message = request.form['message']
        notification.subject = request.form['subject']
        notification.status = 'Notifications submitted'
        notification.submitted_date = datetime.utcnow()

        try:
            db.session.add(notification)
            db.session.commit()
            db.session.refresh(notification)
            # other way m = bytes([notification.id])
            m = '{}'.format(notification.id)
            try:
                msg = Message(m)
                sentResult = queue_client.send(msg)
            except Exception as e:
                logging.error(
                    'An error has ocurred when sending msg to queue {}', str(e))
            return redirect('/Notifications')
        except:
            logging.error('log unable to save notification')

    else:
        return render_template('notification.html')
