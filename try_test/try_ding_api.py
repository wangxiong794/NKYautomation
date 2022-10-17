# # encoding=utf-8
# # 调试钉钉上传文档到钉盘
#
# import dingtalk.api
# from alibabacloud_dingtalk import
#
# req=dingtalk.api.OapiFileUploadSingleRequest("https://oapi.dingtalk.com/file/upload/single")
#
# req.agent_id="1704925969"
# req.file_size=2730854
# req.file=dingtalk.api.FileItem('abc.jpg',open('abc.jpg','rb'))
# try:
# 	resp= req.getResponse(access_token)
# 	print(resp)
# except Exception,e:
# 	print(e)

import dingtalk.api
request = dingtalk.api.OapiGettokenRequest("https://oapi.dingtalk.com/user/get")
request.userid="userid1"
response = request.getResponse()
print(response)