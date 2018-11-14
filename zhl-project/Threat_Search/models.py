from django.db import models
# Create your models here.
class hash_md5(models.Model):
    hash_id = models.CharField(max_length=32)   #哈希值
    hash_type=models.TextField()                #哈希值类型
    state=models.TextField()                    #状态
    time = models.DateTimeField()               # 时间
    source = models.TextField()                 # 来源
    source_state=models.TextField()             #来源状态
    software = models.TextField()               #杀毒软件
    tag = models.TextField()                    #标签
class hash_sha128(models.Model):
    hash_id = models.CharField(max_length=32)  # 哈希值
    hash_type = models.TextField()  # 哈希值类型
    state = models.TextField()  # 状态
    time = models.DateTimeField()  # 时间
    source = models.TextField()  # 来源
    source_state = models.TextField()  # 来源状态
    software = models.TextField()  # 杀毒软件
    tag = models.TextField()  # 标签
class hash_sha256(models.Model):
    hash_id = models.CharField(max_length=32)  # 哈希值
    hash_type = models.TextField()  # 哈希值类型
    state = models.TextField()  # 状态
    time = models.DateTimeField()  # 时间
    source = models.TextField()  # 来源
    source_state = models.TextField()  # 来源状态
    software = models.TextField()  # 杀毒软件
    tag = models.TextField()  # 标签

