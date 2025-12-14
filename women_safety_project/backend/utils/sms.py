import requests

FAST2SMS_API_KEY = "YOUR_FAST2SMS_API_KEY"  # Replace with your key

def send_sms_alert(phone, message):
    """
    Sends SMS alert using Fast2SMS API
    """

    url = "https://www.fast2sms.com/dev/bulkV2"

    headers = {
        "authorization": FAST2SMS_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "route": "v3",
        "sender_id": "TXTIND",
        "message": message,
        "language": "english",
        "numbers": phone
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        print("SMS Response:", response.json())
        return response.json()
    except Exception as e:
        print("SMS Error:", e)
        return {"status": "failed", "error": str(e)}
