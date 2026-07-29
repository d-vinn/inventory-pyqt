<H1>TQ Dessert</H1>

<b>MENU</b>
- 아메리카노 3,500
- 라떼 4,000
- 과일산도 8,000
- 마카롱 3,000
- 딸기 조각케이크 7,500
- 에그타르트 3,000


item table create
store
db_helper.py
app.py
settings.py

customers
show menu
show

✅sql workbench에 item table 만들고,

✅시작화면(desert_app.py) : 안녕하세요, qt 디저트 카페입니다. 주문을 원하시면 주문 시작하기 버튼을 눌러주세요. (가장 상단에는 설정 모드 버튼 있음)  
4. 시작하기 버튼과 연결된 화면(show_menu.py) : 데이터 목록 보여줌, 옆에 수량 표시 기능 있음, 맨 밑에 선택 완료 버튼 있음 -> 수량이 item table과 맞는지 확인하고, 안 맞다면 경고 문구 띄움([menu]의 수량이 [n]개 남았습니다.)  
5. 선택 완료 버튼과 연결된 화면(show_order.py) : 메뉴명 + 수량을 보여주고 해당 내용이 맞다면 맨 밑에 주문 완료 버튼 있음  
6. 주문 완료 버튼과 연결된 화면(show_end.py) : 주문이 완료되었습니다. 감사합니다. 를 띄움  


login은 가장 마지막에 구현!!
USER : 사장님 테이블 (login)
- id -> primary key!
- pw
