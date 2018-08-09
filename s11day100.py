s11day100 

内容回顾：
	1. django请求生命周期？
		- wsgi
		- 中间件
		- 路由
		- 视图 
			- ORM
			- 模板渲染
	2. django提供的功能 
		- 必备
			- 路由 
			- 视图
			- 模板渲染
		- django：
			- ORM：
				...
				...
			- 分页 
			- Form & ModelForm
			- admin 
			- auth
			- session 
			- 中间件 
			- contenttype
			- csrf
			- 缓存（速度块）
	3. restful 
		- restful 规范 
		- django rest framwork 
		- 其他
			- 跨域
				a. 为什么出现跨域？
				b. 如何解决跨域？
					使用cors，即：设置响应头。
					简单请求：
						响应头中设置一个允许域名访问
					复杂请求：
						OPTIONS请求做预检，允许特殊请求方式和请求头 + 允许域名访问。
						真正请求就可以发送过来进行处理 + 允许域名访问。
				c. 跨域 
					www.baidu.com         / www.luffycity.com 
					www.baidu.com         / api.luffycity.com 
					www.baidu.com:8001    / www.baidu.com:8002 
				
				d. 路飞线上代码无跨域（项目部署时，放在同一处）
		
			- vue.js 
				- 前端三大框架：react.js /angular.js / vue.js 
				- vue.js 2版本
				- 组件：
					- axios
					- vuex 
					- router
				- 你觉得vue和jQuery的区别？
					- 双向绑定
					- 单页面应用
		

今日内容：购物车
	1. redis字典 
	
	2. 登陆认证
	
	3. 购物车逻辑 
		- 添加到购物车
		- 删除
		- 编辑
		- 查看 
	
	4. 串讲vue.js 
	
内容详细：
	1. redis字典 
		
		- 安装redis，在内存中进行存取数据。
		- 启动redis服务
			redis-server 
			
		- 虚拟机问题：
			1. 网卡连接方式桥接
			2. iptables 关闭 
				service iptables stop 
			3. 修改redis配置文件
				vim /etc/redis.conf
		
		- 初始redis
			a. redis相当于是一个在内存中创建的大字典。
			b. redis的value有5大数据类型：
				- 字符串
					import redis
					conn = redis.Redis(host='192.168.11.61',port=6379)
					# 设置值
					conn.set('wupeiqi_name','于超')
					# 获取值
					val = conn.get('wupeiqi_name').decode('utf-8')
					print(val)
				- 列表
				- 集合 
				- 有序集合
				- 字典 
	
	2. 购物车逻辑 
	
		问题：
			a. 为什么要把购物车信息放到redis中？
				- 查询频繁
					- 课程是否存在？
					- 价格策略是否合法？
				- 中间状态 
					- 购买成功之后，需要删除。
					- 购物车信息删除
					
			b. 购物车有没有数量限制？
				使用 keys 查看个数做判断
				
			c. 购物车的结构 
				redis = {
					shopping_car_用户ID_课程ID:{
						id:'课程ID',
						name:'课程名称',
						img:'课程图片',
						default_price_id:'默认价格ID',
						price_policy_dict:{
							1: {...},
							5: {...},
						}
					}
				}
		
	
		总结： 
			a. 五大数据类型
			
			b. 列举每种数据类型的操作
				字符串：
					set 
					get 
					
				字典：
					hget
					hgetall
					hset
					hmset 
					hdel 
				
				其他：
					delete 
					expire
					keys 
					flushall()
					
	
	
	
	
作业：
	1. 虚拟机安装上redis，redis服务启动；
	2. 购物车 
		- 添加到购物车
		- 查看购物车信息
		- 删除课程
		- 修改课程 
	注意事项：
		a. 引用同一个地址
							
				user_list = []
				user_dict = {}

				for i in range(1,10):
					temp = {'id':i,'name':'于超%s' %(i,) }
					user_list.append(temp)
					user_dict[i] = temp

				print(user_list)
				print(user_dict)
				user_dict[1]['name'] = "于超超超超超"

				print(user_list)
				print(user_dict)

		b. 对于字典的key，序列化会将数字转换成字符串
		
			info = {1:'alex',2:'于超'}
			new = json.dumps(info)   '{"1":"alex", "2":"于超"}'
			data = json.loads(new)   {"1":"alex", "2":"于超"}
			

























	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	