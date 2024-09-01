import firebase_admin
from firebase_admin import credentials, messaging

# Initialize Firebase Admin SDK
cred = credentials.Certificate(r'replace/with/path/to/your/serviceAccountKey.json')
firebase_admin.initialize_app(cred)


#  Sends a push notification to a specific device token.

def send_notification(notification_title, notification_body, token):
    

    # Define the message
    message = messaging.Message(
        notification=messaging.Notification(
            title=notification_title,  # The title of the notification.
            body=notification_body,    # The body content of the notification. 
        ),
        token=token,    #  The device token to which the notification will be sent.
        android=messaging.AndroidConfig(
            notification=messaging.AndroidNotification(
                sound="src_assets_new",  # Sound file name for Android 
                channel_id='sound_channel'  # Channel ID for Android
            )
        ),
        apns=messaging.APNSConfig(
            payload=messaging.APNSPayload(
                aps=messaging.Aps(
                    category="NEW_MESSAGE_CATEGORY", # Channel ID for iOS
                    sound='src_assets_new.wav'  # Sound file name for iOS 
                )
            )
        )
    )

    # Send the notification
    response = messaging.send(message)
    print('Successfully sent message:', response)

# Define notification parameters
notification_title = "New Notification"
notification_body = "This is a test notification."
token =  "Replace with Device Token"

send_notification(notification_title, notification_body, token)
