class SmsOtpUrls(object):
    check_sms_otp_balance = "https://2factor.in/API/V1/{}/BAL/SMS"
    send_auto_generated_otp = "https://2factor.in/API/V1/{}/SMS/{}/AUTOGEN"  # API key and Phone number
    send_auto_generated_otp_custom_template = "https://2factor.in/API/V1/{}/SMS/{}/AUTOGEN/{}" # api, ph, template
    send_custom_otp = "https://2factor.in/API/V1/{}/SMS/{}/{}" # API, Phone, OTP
    send_custom_otp_custom_template = "https://2factor.in/API/V1/{}/SMS/{}/{}/{}" # API, Phone, OTP, Template
    verify_sms_otp_input = "https://2factor.in/API/V1/{}/SMS/VERIFY/{}/{}" # Api, Session ID, Otp Input


class VoiceOtpUrls(object):
    send_voice_otp_url = "http://2factor.in/API/V1/{}/VOICE/{}/AUTOGEN"  # Api key and Phone number
    send_custom_voice_otp_url = "http://2factor.in/API/V1/{}/VOICE/{}/{}"  # Key, Phone and Custom OTP
    verify_voice_otp_url = "http://2factor.in/API/V1/{}/VOICE/VERIFY/{}/{}"  # Key, Session ID and OTP Input


class TransactionalSMSUrls(object):
    check_credit_balance_url = "http://2factor.in/API/V1/{}/ADDON_SERVICES/BAL/TRANSACTIONAL_SMS"  # Api Key
    pull_delivery_report_url = "http://2factor.in/API/V1/{}/ADDON_SERVICES/RPT/TSMS/{}"  # Key and Session ID
    send_transactional_sms_open_template = "http://2factor.in/API/V1/{}/ADDON_SERVICES/SEND/TSMS"  # Key only POST
    send_transactional_sms_dynamic_template = "http://2factor.in/API/V1/{}/ADDON_SERVICES/SEND/TSMS"  # Key only POST


class PromotionalSMSUrls(object):
    check_credit_balance = "http://2factor.in/API/V1/{}/ADDON_SERVICES/BAL/PROMOTIONAL_SMS"  # Key
    send_promotional_sms = "http://2factor.in/API/V1/{}/ADDON_SERVICES/SEND/PSMS"  # Key (POST) request


class BlockListManagementUrls(object):
    block_number_sms_service_url = "http://2factor.in/API/V1/{}/BLOCK/{}/SMS/ADD"  #  APi Key
    block_number_voice_service_url = "http://2factor.in/API/V1/{}/BLOCK/{}/VOICE/ADD"  # Api key
    unblock_number_sms_service_url = "http://2factor.in/API/V1/{}/BLOCK/{}/SMS/REMOVE"  # Api Key and phone number
    unblock_number_voice_service_url = "http://2factor.in/API/V1/{}/BLOCK/{}/VOICE/REMOVE"  #  Api key and phone number

