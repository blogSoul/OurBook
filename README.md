# OurBook
<p align="center">
<img src="main/static/img/logo.png" width="55%" alt="ourbook">
</p>

## 개요
<a href="https://github.com/kangtegong/OurBook#%EC%9A%94%EC%95%BD"> 1. 요약 </a>   
<a href="https://github.com/kangtegong/OurBook#%EB%AC%B8%EC%A0%9C%EC%9D%98%EC%8B%9D"> 2. 문제의식</a>    
<a href="https://github.com/kangtegong/OurBook#%EC%82%AC%EC%9A%A9%EC%82%AC%EB%A1%80">3. 사용사례</a>   
<a href="https://github.com/kangtegong/OurBook#%EC%82%AC%EC%9A%A9%EA%B8%B0%EC%88%A0-%EB%B0%8F-%EC%84%A4%EC%B9%98">4. 사용기술</a>    
<a href="https://github.com/kangtegong/OurBook#db-%EC%84%A4%EA%B3%84-%EB%B0%8F-%EC%BD%94%EB%93%9C-%ED%95%B4%EC%84%A4">5. DB 설계 및 코드 해설</a>

## 요약

P2P 전공서적/솔루션 공유 플랫폼

## 문제의식 

서울시 전공서적 구매를 위해 소비되는 대학생들의 경제적 지출은 880억에 이르며,   
이렇게 구매된 전공서적은 학기가 종료되면 대부분 방치되고 버려진다.

서울시의 대학생 전공 서적의 구매 규모를 예측해 본다면, 

```
370,000명 (서울시 내 1학년 제외한 재학 대학생 수)
X 40,000원 X 3권 X 2학기 
= 
(연간) 88,800,000,000 원 
```

을 전공서적에 사용하는 데에 들이는 셈이다. 


## 중고거래가 아닌 '공유'플랫폼 필요한 이유

### 중고거래로 전공서적은 많이 쓰이지 않는다

중고 전공서적을 통해 책값의 부담을 줄일 수는 있으나,   
거래에 대한 접근성 부족으로 중고 전공서적 거래가 원활히 일어나고 있지 않다

### 가격은 높지만, 종류는 적다
 
한 학기만 사용하고 방치되는 고가의 전공서적이지만,    
각 과목에 사용하는 전공서적 종류는 크게 다양하지 않다.

### 반드시 사야만 한다

매 학기초 필수적으로 새로 구매해야 하는 전공서적이 존재하나, 
한 학기가 지나가면 잔존가치 급감한다.

## 사용사례 

### 전공 서적 목록
학교 별 (지역 별) 공통된 전공서적을 우선으로    
전공서적 목록을 등록한다.

전공 서적의 목록은
학교 별 API를 통해,    
학생들의 자발적 참여를 통해 획득한다.   
(참여한 학생에겐 솔루션 열람 권한 부여)

### 확보한 서적 대여/양도/판매

### 거래 중개

학교 별로 사전에 설치한 OurBook 거래 지점을 통해   
거래를 중개해 줄 수 있다.

중고 거래의 불편함 중 큰 비중을 차지하는   
'거래 시간 및 장소 맞추기' 문제는   
OurBook은 중개를 통해 일부 수수료를 받는다

### 솔루션 등록 및 열람

솔루션을 등록한 이들에게는 
솔루션 열람권이나   
중개 거래를 1회 무료로 이용 가능하다

## 사용기술 및 설치

### Back-End
django   
django-rest-framework

### Front-End
bootstrap   
React   

### Deployment & Database
AWS RDS   
AWS EC2   
(test)pythonanywhere


## DB 설계 및 코드 해설