import boto3
region = 'ap-northeast-1'

def lambda_handler(event, context):
# 起動中のインスタンスをフィルタしてinstances変数に入れる
    instances = ec2.instances.filter(
      Filters=[{'Name':'instance-state-name', 'Values':['running']})
# インスタンスIDとインスタンスのタイプをプリント
    for instance in instances:
      print(instance.id, instance.instance_type)
# リージョンと停止対象のインスタンスのIDを取得
    ec2 = boto3.client('ec2', region_name=region)
    ec2.stop_instances(InstanceIds=instances)
    print 'stopped your instances: ' + str(instances)
