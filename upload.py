
import requests, json


def upload_files():
    header={ 
           "Accept": "*/*",
            "jobId": "455",
            "accessionId": "444"
            }
    files = {'file':open(r'C:\\Users\Administrator\\Documents\\Tencent Files\\2235826534\\FileRecv\\test1.xml','rb')}
    url = 'http://enhancer.ncpsb.org:8090/example/v1/file/upload'
    r = requests.post(url, files=files, headers=header)
    return r


def confirm_files():
    confirm_url = 'http://enhancer.ncpsb.org:8090/example/v1/file/confirmFiles'

    comfirm_header = {
                
                    "Accept": "application/json",
                    "jobId": "455",
                    }
    data={
        'jobId':'455',
        'resultFileList':{
                        "fileList": [
                         "233"
                        ],
                        "fileListLength": 1
                        }
        }
    r = requests.post(confirm_url, data=json.dumps(data), headers=comfirm_header)
    return r


def main():
    res = upload_files()
    print(res.text)
    # res2 = confirm_files() 
    # print(res2.text)


if __name__ == '__main__':
    main()




#     curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'jobId: 122' -d '{"fileList": ["file"], 
# "fileListLength": 1}' 'http://enhancer.ncpsb.org:8090/example/v1/file/confirmFiles'
