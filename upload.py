
import requests, json


def applyID():
    header={
        "Accept": "application/json"
    }
    url = "http://enhancer.ncpsb.org:8090/example/v1/file/apply"
    r = requests.get(url,headers=header)
    return r


def upload_files(contents):
    header={ 
           "Accept": "*/*",
            "jobId": str(contents['id']),
            "accessionId": str(contents['accessionId']),
            }
    files = {'file':open(r'C:\\Users\\Administrator\\Documents\\Tencent Files\\2235826534\\FileRecv\\test1.xml','rb')}
    url = 'http://enhancer.ncpsb.org:8090/example/v1/file/upload'
    r = requests.post(url, files=files, headers=header)
    print(r.text)
    rcon = confirm_files(r.json()['id'],list(files.keys()))

    return r


def confirm_files(id,files):
    confirm_url = 'http://enhancer.ncpsb.org:8090/example/v1/file/confirmFiles'

    comfirm_header = {
                    "Accept": "application/json",
                    "jobId": str(id),
                    }
    data={
        'jobId':id,
        'resultFileList':{
                        "fileList": files,
                        "fileListLength": len(files)
                        }
        }
    r = requests.post(confirm_url, data=json.dumps(data), headers=comfirm_header)
    return r


def main():
    resJson = applyID().json()
    print(resJson)
    print('_______________________')
    res = upload_files(resJson)
    print(res.text)


if __name__ == '__main__':
    main()


# curl -H "Content-Type: application/json" -H "Accept: application/json" -H "jobId: 123" -X POST  -d "{\"fileList\":[\"file\"],\"fileListLength\":1}" "http://enhancer.ncpsb.org:8090/example/v1/file/confirmFiles"