# 화장품 추천 웹서비스
## AI_12_section3

### 문제정의

올리브영, 랄라블라와 같은 드러그스토어에 갔을때 각 제품마다 여러 브랜드가 있고 각종 부문에서 1위를 했다는 문구가 붙어 있는 제품들이 많다. 브랜드마다 가격도 다르고 세일하는 품목도 달라서 제품 선택에 어려움을 겪는 사람들이 많다고 생각했고 이러한 문제를 바탕으로 원하는 제품, 성별, 나이, 피부타입을 입력하면 화장품을 추천해주는 웹서비스 개발을 목표로 한다.

### 문제 해결과정

1. 화장품 리뷰 어플(글로우픽)에서 사용자 나이, 피부타입, 성별, 제품, 평점 크롤링
2. 리뷰 평점이 3.5 이상인 데이터만 사용
3. 평점이 높은 데이터만 사용하여 사용자가 원하는 제품 카테고리에서 높은 평점을 가진 제품을 추천하는 시스템 구현

### 데이터셋

- '글로우픽' 이라는 화장품 리뷰 어플에서 카테고리별 랭킹 20위권 제품과 리뷰를 쓴 사람들의 정보 데이터
- 주요 컬럼
  - 제품명
  - 브랜드
  - 평균평점
  - 카테고리
  - 사용자 나이
  - 사용자 피부타입
  
### 프로젝트 진행과정

1. 사전기획 및 데이터 크롤링 관련 학습
2. 데이터 수집 및 적재, 분석
3. 분석 모델 관련 학습 및 구현
4. FLASK를 통한 웹서비스 구현

### 파이프라인

<img width="899" alt="스크린샷 2023-07-20 오후 6 31 16" src="https://github.com/Songnahyun/Section3project/assets/49776542/9f77b796-ca7b-4183-93bc-ba60eee9f011">


### 결과정리

- 결정트리 모델 사용
- 예측 정확도는 0.2 정도로 낮은편
- FLASK를 통한 추천 웹서비스 구현
- 사용자가 원하는 제품 카테고리, 나이, 피부타입, 성별을 입력하면 제품 추천

<img width="1297" alt="스크린샷 2022-10-04 오후 11 22 36" src="https://user-images.githubusercontent.com/49776542/193846245-8129a34d-ad68-4157-8d8e-b6b0a3080806.png">
<img width="1091" alt="스크린샷 2022-10-04 오후 11 22 51" src="https://user-images.githubusercontent.com/49776542/193846281-9a26e658-492c-4895-a6f5-b693d9cde708.png">


### 한계점 및 해결방안

- FLASK 에서 많은 시간이 소비되어서 구현하고자 하는 기능을 모두 구현시키지 못했다.
- 웹 서비스 구축에 초점을 맞추다보니 모델 성능이 떨어졌다.
- 데이터 양이 부족하여 추후 데이터를 더 수집하고 모델 성능 향상이 필요하다.
- 웹 서비스 배포까지 진행되면 더 좋을 것 같다.
