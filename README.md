# 机场自动签到
做这个项目主要是看到最近冒出来许多机场注册就能白嫖，签到就送流量。然后又顺便拿这个项目学习一下Github Actions。
请注意，本项目不讨论跟fq有关的话题，仅仅是技术讨论，不要询问白嫖jc等内容！！！
## 功能

废话，肯定就是机场自动签到啊。
## 部署



1. Fork此仓库
2. 到`Settings`→`Secrets`→`Actions` 添加以下参数：

| 参数  | 是否必须  | 内容  | 示例  |
| ------------ | ------------ | ------------ | ------------ |
| EMAIL  | 是  | 注册机场所用邮箱  | a@example.com  |
| PASSWORD  | 是  | 注册机场所用密码  | password1  |
| BASE_URL  | 是  | 机场地址  | https://examplea.com  |
| SCKEY  | 否  | Sever酱秘钥  | SCTxxxxxxxxxxxxxx  |
| TGBOT  | 否  | Telegram推送bot  | 5xxxxxxx:xxxxxxxxx  |
| TGUSERID  | 否  | Telegram推送人id  | 8xxxxxxxxx  |

3. 转到`Actions`创建一个workflow，运行一次，以后每天项目都会自动运行。最后，可以到Run sign查看签到情况，同时也会通过Sever酱发送出去。
## 参考
1. https://github.com/zhjc1124/ssr_autocheckin 用了他的机场签到代码。
2. https://github.com/sirodeneko/genshin-sign 参考其Actions的yml。

