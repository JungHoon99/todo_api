# TODO_API
## 소개
- REST API를 활용한 Todo List를 관리할 수 있는 어플리케이션
- Django의 DRF를 활용하여 구축하였습니다.
### Python Package List
    bcrypt==4.0.1
    Django==4.2.3
    djangorestframework==3.14.0
    PyJWT==2.7.0

### 현재 API 목록
- `todos/`
    - `GET` : 전체 todo list 가져오기
    - `POST` : todo 등록하기
- `todos/<int:id>`
    - `GET` : id에 해당하는 todo 값 가져오기
    - `PUT` : todo 수정
- `users/`
    - `POST` : user 회원가입
- `users/<int:id>`
    - `GET` : id를 입력받아 user에 대한 정보 가져오기
- `users/auth`
    - `POST`

----
### 고민 했던 부분들
- GET `users/auth`에서 로그인 관련 기능 구현 과정에서 로그인기능을 get으로 할지 post로 할지에 대한 고민을 하였다. 그래서 찾아보니 get으로 요청은 body에 정보를 담을 수 없기 때문에 url에 아이디와 비밀번호를 요청해야 하기 때문에 보안에 문제가 있을 수 있음으로 post로 구현