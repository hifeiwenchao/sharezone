from api.service import dao
from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
from aliyunsdkdysmsapi.request.v20170525 import QuerySendDetailsRequest
from aliyunsdkcore.client import AcsClient
import uuid
from aliyunsdkcore.profile import region_provider
# from django.conf import settings
from api.const import SmsTemplateCode, SmsExpire
import random
from common import utils


# 注意：不要更改
REGION = "cn-hangzhou"
PRODUCT_NAME = "Dysmsapi"
DOMAIN = "dysmsapi.aliyuncs.com"

ACCESS_KEY = utils.config('SMS', 'access_key')
SECRET = utils.config('SMS', 'secret')
SIGN_NAME = utils.config('SMS', 'sign_name')

acs_client = AcsClient(ACCESS_KEY, SECRET, REGION)
region_provider.add_endpoint(PRODUCT_NAME, REGION, DOMAIN)


def send_sms(phone_numbers, template_code, template_param=None, business_id=None):
    sms_request = SendSmsRequest.SendSmsRequest()
    # 申请的短信模板编码,必填
    sms_request.set_TemplateCode(template_code)
    # 短信模板变量参数
    if template_param is not None:
        sms_request.set_TemplateParam(template_param)
    # 设置业务请求流水号，必填。
    if business_id is not None:
        sms_request.set_OutId(business_id)
    # 短信签名
    sms_request.set_SignName(SIGN_NAME)
    # 数据提交方式
    # smsRequest.set_method(MT.POST)
    # 数据提交格式
    # smsRequest.set_accept_format(FT.JSON)
    # 短信发送的号码列表，必填。
    sms_request.set_PhoneNumbers(phone_numbers)
    # 调用短信发送接口，返回json
    sms_response = acs_client.do_action_with_exception(sms_request)
    return sms_response


def send_register_code(phone):
    code = random.randint(1000, 10000)
    now = utils.current_timestamp()

    dao.identity_code.create(
        phone=phone, code=code, expire_at=now + SmsExpire.REGISTER, template_code=SmsTemplateCode.REGISTER)
    send_sms(phone, SmsTemplateCode.REGISTER, {'code': code})


def send_login_code(phone):
    code = random.randint(1000, 10000)
    now = utils.current_timestamp()

    dao.identity_code.create(
        phone=phone, code=code, expire_at=now + SmsExpire.LOGIN, template_code=SmsTemplateCode.LOGIN)
    send_sms(phone, SmsTemplateCode.LOGIN, {'code': code})


def send_reset_pwd_code(phone):
    code = random.randint(1000, 10000)
    now = utils.current_timestamp()

    dao.identity_code.create(
        phone=phone, code=code, expire_at=now + SmsExpire.RESET_PWD, template_code=SmsTemplateCode.RESET_PWD)
    send_sms(phone, SmsTemplateCode.RESET_PWD, {'code': code})


def send_find_pwd_code(phone):
    code = random.randint(1000, 10000)
    now = utils.current_timestamp()

    dao.identity_code.create(
        phone=phone, code=code, expire_at=now + SmsExpire.FIND_PWD, template_code=SmsTemplateCode.FIND_PWD)
    send_sms(phone, SmsTemplateCode.FIND_PWD, {'code': code})
