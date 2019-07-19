# coding=utf-8
import json
import re
def func():
    s1 = '''
    {"tasks": [{"id": "99", "zone_uuid": "b421d242-7c22-4eb7-b167-c985552b77af", "camera_uuid": "4e9ba0b2-60ec-40c9-b3e5-7b995e6ec2e6", "object_type": "OBJECT_FACE", "feature_version": 24702, "task_object_config": {"rules": [], "crowd_config": null, "scenario_rules": []}, "playback_config": null, "ingress_type": "VIDEO", "task_status": {"status": "ERROR", "error_message": "SOURCE_ERROR read tcp 10.224.6.88:47984->10.9.244.46:8554: i/o timeout", "last_received_time": "2019-07-17T12:52:12.533227404Z"}, "internal_task_uuid": "10002019071712144748101", "created_at": "2019-07-17T12:14:47Z", "updated_at": "2019-07-17T12:52:27Z", "storage_policy": null, "video_parameter": {"stream_type": "Main", "video_format": "VF_H264", "width": 1920, "height": 1080, "frame_rate": 0, "bit_rate_type": "CBR", "bit_rate": 0, "i_frame_interval": 0}}], "page": {"offset": 0, "limit": 100, "total": 1}}
    '''

    js = json.loads(s1)
    print(js.get('tasks')[0].get('id'))


if __name__ == '__main__':
    func()