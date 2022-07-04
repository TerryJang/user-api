# user-api
User Join, Login API

## 최초 환경 설정
 - python 3.9와 mysql이 설치되어 있어야 합니다.

### 1. 패키지 설치
 - 기본설치 : ```pip install -r requirement/base.txt```
 - 기본+테스트 : ```pip install -r requirement/test.txt```

### 2. Mysql DB 스키마 및 테이블 생성
 - sql 폴더 내에 Query를 mysql에서 실행합니다.

### 3. Config 설정
  - config 폴더 내 configuration.yaml 파일을 복사하여 local.yaml 파일을 생성합니다.
  - 연결할 mysql의 host, port, user, password를 입력합니다.

### 4. 서버 실행
 - ```python main.py```

### 5. 테스트 코드 실행
 - ```pytest```


## APIDOC

### 1. 핸드폰 인증코드 받기
 - path : ```GET /user/signup```
 - header: ```{"Content-Type": application/json}```
 - data: ```{"phone": 01012341234}```
 - response: ```{"code": 123456}```

### 2. 핸드폰 인증코드 인증
 - path : ```PATCH /user/signup```
 - header: ```{"Content-Type": application/json}```
 - data: ```{"phone": 01012341234, "code": 123456}```
 - response: ```{}```

### 3. 회원가입
 - path: ```POST /user/signup```
 - header: ```{"Content-Type": application/json}```
 - data: ```{"email": "test@naver.com", "password": "aA12341234!", "name": "test", "nickname": "test", "phone": "01012341234", "code": "818200"}```
 - response: ```{}```

### 4. 로그인
 - path : ```POST /user/login```
 - header: ```{"Content-Type": application/json}```
 - data: ```{"email": "test@naver.com", "password": "aA12341234!"}```
 - response: ```{"token": "token"}```

### 5. 회원정보 조회
 - path : ```GET /user```
 - header: ```{"Content-Type": application/json, "Authorization": token}```
 - data: ```{}```
 - response: ```{"email": "test@naver.com", "name": "test", "nickname": "test", "phone": "01012341234", "created_at": "2022-07-01 00:00:00"}```


### 6. 패스워드 변경
 - path : ```PATCH /user/password```
 - header: ```{"Content-Type": application/json}```
 - data: ```{"email": "test@naver.com", "password": "bB12341234!", "phone": "01012341234", "code": 123456}```
 - response: ```{}```
