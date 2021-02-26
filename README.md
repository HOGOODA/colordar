# colordar
A Django calendar which colorize each day based on the day's diary(Sentimental analysis based model)

Add your Story 에 제목과 내용을 적으면 감정분류(Sentimental analysis) 를 통해 그날의 story 감정을 분석, 캘린더에 7가지 색으로 표현

감정 분류 =['슬픔','공포','분노','혐오','놀람','행복','중립']

# Sentimental Analysis Model
ktrain을 이용한 BERT model로 구성.

추후 수정후 좀 더 보완한 LSTM model 및 ELECTRA를 기반으로 한 다른 모델도 테스트 해볼 예정.
참고로 monologg 님의 KORELECTRA 도 사용해볼 예정. NLP 본인처럼 이제 막 관심을 가진 초보자는 이 분 깃허브 참고해보는 것 추천 (https://github.com/monologg )

현재까지 테스트한 모델 중에선 ktrain BERT model이 가장 성능이 좋았음.
Admin 페이지에서나 데이터베이스에서 입력받은 story 내용을 BERT model이 분석한 결과를 확인 가능.
