print(
'''
Django 项目结构解析
    mysite 
        - mysite  # 目录默认和项目同名，项目配置目录
            __init__.py
            settings.py  # 配置文件
                配置模板路径
                    TEMPLATES = [
                        {
                            'BACKEND': 'django.template.backends.django.DjangoTemplates',
                            'DIRS': ['html'],
                            'APP_DIRS': True,
                            'OPTIONS': {
                                'context_processors': [
                                    'django.template.context_processors.debug',
                                    'django.template.context_processors.request',
                                    'django.contrib.auth.context_processors.auth',
                                    'django.contrib.messages.context_processors.messages',
                                ],
                            },
                        },
                    ]
                配置静态文件
                    STATICFILES_DIRS = (  # STATICFILES_DIRS:名称固定
                        os.path.join(BASE_DIR, 'static'),  # 最后的","必须有
                    )
            urls.py      # url注册文件
            wsgi.py      # wsgiref模块，python自己不写socket需要指定使用哪一个wsgi模块的socket，默认python自带的wsgiref
        - manage.py      # 管理Django程序
            >> python manage.py startapp xx  # django创建app
            >> python manage.py makemigrations
            >> python manage.py migrate
        - app1           # 通过django创建的app1
            - migrations # 目录。修改表结构等会在此目录下记录日志信息
                __init__.py
            __init__.py
            admin.py     # django为我们提供的后台管理
            apps.py      # 配置当前app
            models.py    # 实体类映射ORM
            tests.py     # 测试
            views.py     # 业务代码
''')
