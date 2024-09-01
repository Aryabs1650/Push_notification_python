import firebase_admin
from firebase_admin import credentials, messaging

# Initialize Firebase Admin SDK
cred = credentials.Certificate(r'replace/with/path/to/your/serviceAccountKey.json')
firebase_admin.initialize_app(cred)

# Define a function to send multicast notifications
def send_multicast_notification(notification_title, notification_body, tokens):
    # Create a MulticastMessage object with the specified notification title and body
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=notification_title,
            body=notification_body,
        ),
        # Configure settings specific to iOS (APNS)
        apns=messaging.APNSConfig(
            payload=messaging.APNSPayload(
                aps=messaging.Aps(
                    category="NEW_MESSAGE_CATEGORY",
                    sound="src_assets_new.wav"  # Specify the sound file name with extension for iOS
                )
            )
        ),
        # Configure settings specific to Android
        android=messaging.AndroidConfig(
            notification=messaging.AndroidNotification(
                sound="src_assets_new.wav",  # Specify the sound file name for Android
                channel_id="sound_channel"   # Specify the channel ID for Android
            )
        ),
        tokens=tokens  # Pass the list of tokens here
    )

    # Send the multicast message
    response = messaging.send_multicast(message)

    # Handle the response
    print('Successfully sent message:', response.success_count)
    print('Failed to send message:', response.failure_count)

    

# Define notification parameters
notification_title = "New Notification"
notification_body = "This is a test notification."
tokens = [
    "Token 1",
    "Token 2",
    " Token 3"
    
    # Add more device tokens as needed
]

# Call the function to send the notification to the list of tokens
send_multicast_notification(notification_title, notification_body, tokens)

