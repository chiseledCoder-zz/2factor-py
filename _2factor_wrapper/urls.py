class SmsOtpUrls(object):
    check_sms_otp_balance = "https://2factor.in/API/V1/{}/BAL/SMS"
    send_auto_generated_otp = "https://2factor.in/API/V1/{}/SMS/{}/AUTOGEN"  # API key and Phone number
    send_auto_generated_otp_custom_template = "https://2factor.in/API/V1/{}/SMS/{}/AUTOGEN/{}" # api, ph, template
    send_custom_otp = "https://2factor.in/API/V1/{}/SMS/{}/{}" # API, Phone, OTP
    send_custom_otp_custom_template = "https://2factor.in/API/V1/{}/SMS/{}/{}/{}" # API, Phone, OTP, Template
    verify_sms_otp_input = "https://2factor.in/API/V1/{}/SMS/VERIFY/{}/{}" # Api, Session ID, Otp Input