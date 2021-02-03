from requests import get
import os

loadPath = "./load/"

def download(url, emticonName):
    with open(emticonName, "wb") as file:
        response = get(url)
        file.write(response.content)
        print('{} 다운로드 완료!'.format(emticon_name[i]))

if __name__ == '__main__':
    mode = input("직접입력? 아님 불러오기? : ")
    if mode == "불러오기":
        emticon_id = os.listdir(loadPath)
    else:
        print("이모티콘 아이디를 입력해주세요!")
        print("여러개라면 ,로 구분!")
        emticon_id = input("아이디는? : ").split(',')

        print(emticon_id)
        print('총 {}개'.format(len(emticon_id)))


        print("이모티콘 이름을 순서대로 입력해주세요!")
        print("여러개라면 ,로 구분!")
        emticon_name = input("이름은? : ").split(',')

    for i in range(0, len(emticon_id)):
        print('{}번째 아이디...').format(i)
        url = "https://item.kakaocdn.net/dw/" + emticon_id[i] + ".thum_pack.zip"
        print(url)

        if emticon_name == []:
            emticon_name.append("")
        if emticon_name[i] == "" or None or "undefined":
            print('{}의 이름이 없습니다! id로 대체됩니다!'.format(emticon_id[i]))
            emticon_name[i] = emticon_id[i]

        print('{} 다운로드 중...'.format(emticon_name[i]))
        download(url, emticon_name[i] + ".zip")
