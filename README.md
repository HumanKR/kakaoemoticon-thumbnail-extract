# Kakao Emoticon Thumbnail Extract
카톡 이모티콘 썸네일 뽑아주는 그런거에요.

썸네일을 뽑으니까 gif도 안되고 화질도 원본보단 훨씬 낮아요.

그래도 뭐... 쓸만 합니다.

## Disclamer
사용하기전에 저작권에 대해서 한번 생각해보아요

이모티콘 저작권 말이에요

즉 뽑은 이모티콘으로 뭘 하던 **저에게 책임을 묻지 마세요**...

## Requirements
1. 이 프로젝트는 Python 3.8을 기반으로 테스트 하였습니다.
2. 이 프로젝트는 requests 라이브러리가 필수입니다. 무조건 설치하세요.
```
pip install requests
```
3. 불러오기는 미완성입니다. 제대로 동작하지 않을 수 있습니다.

## How to use
### 직접 입력일 경우 
1. 이모티콘 ID를 이런식으로 복사합니다. 쉼표로 갯수를 구분합니다. 갯수는 상관없을겁니다.... 아마도
```
123456,123456,123456,123456
```
2. main.py를 실행시킨 후 직접입력을 입력한뒤 안내에 따라 붙여넣습니다.
3. 이모티콘의 이름을 이런식으로 이모티콘 ID의 순서에 맞게 복사합니다.
```
이요티콘,이요구르트티콘,,감튀티콘
```
만약 "이요구르트티콘"과 "감튀티콘" 사이처럼 아무것도 적지 않고 넘기면 이모티콘 ID를 이름으로 자동으로 넣어집니다.

다 이름을 모를땐 쉼표 갯수에 맞게... 이렇게도 가능합니다.
```
,,,,,,,,,,,,,,,,,,
```
4. zip파일로 추출이 잘 되었는지 확인합니다. 해당 프로젝트 파일 위치에 저장됩니다.

### 불러오기일 경우 

현재로선 직접 입력을 쓰는것이 좋지만... 뭐...
1. main.py와 같은 공간에 "load" 이름의 폴더를 만들어줍니다.
2. 거기에 파일들을 넣되 파일명에 이모티콘 ID만 남깁니다.
3. main.py를 실행시킨 후 불러오기를 입력하면 "load" 폴더에서 파일명을 불러와서 처리합니다.
4. zip파일로 추출이 잘 되었는지 확인합니다. 해당 프로젝트 파일 위치에 저장됩니다.

## Author
이요 / [@IYO1585](http://github.com/IYO1585) / [@iyogurt1585](https://twitter.com/iyogurt1585)
