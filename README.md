# WPUSH 推送每日60s早报信息

通过 [wpush消息推送平台](https://wpush.cn) 来推送每日60s早报信息

## 使用教程

1. fork 本仓库
2. 设置Github Action Secret 信息

| 参数名称         | 必填 | 说明                                                         |
|--------------|----|------------------------------------------------------------|
| WPUSH_APIKEY | 是  | [WPUSH](https://wpush.cn)平台的APIKEY                         |
| ALAPI_TOKEN  | 是  | [ALAPI](https://www.alapi.cn)平台的APIKEY                     |
| TYPE         | 否  | image或者text,默认image                                        |
| CHANNEL      | 否  | 发送通道，默认wechat ,[更多通道](https://docs.wpush.cn/docs/channel/) |

