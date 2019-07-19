# coding = utf-8
import time

def func():
    ls = ['bm://mxn-intersect/14243/output/_SUCCESS',
     'bm://mxn-intersect/14243/output/part-00000',
     'bm://mxn-intersect/14243/output/part-00001',
     'bm://mxn-intersect/14243/output/part-00002',
     'bm://mxn-intersect/14243/output/part-00003',
     'bm://mxn-intersect/14243/output/part-00004',
     'bm://mxn-intersect/14243/output/part-00005',
     'bm://mxn-intersect/14243/output/part-00006',
     'bm://mxn-intersect/14243/output/part-00007',
     'bm://mxn-intersect/14243/output/part-00008',
     'bm://mxn-intersect/14243/output/part-00009',
     'bm://mxn-intersect/14243/output/part-00010',
     'bm://mxn-intersect/14243/output/part-00011',
     'bm://mxn-intersect/14243/output/part-00012',
     'bm://mxn-intersect/14243/output/part-00013',
     'bm://mxn-intersect/14243/output/part-00014',
     'bm://mxn-intersect/14243/output/part-00015'
    ]

    result_path = None
    for ele in ls:
        if ele.endswith('part-00000'):
            result_path = ele.split("//")[-1]
            break
    print(result_path)



if __name__ == '__main__':
    func()
