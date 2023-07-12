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
    - `get` : 전체 todo list 가져오기
    - `post` : todo 등록하기
- `todos/<int:id>`
    - `get` : id에 해당하는 todo 값 가져오기
    - `put` : todo 수정
- `user/`
    - `post` : user 회원가입
- `user/<int:id>`
    - `get` : id를 입력받아 user에 대한 정보 가져오기
- `user/auth`
    - `post`