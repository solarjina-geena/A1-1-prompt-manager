prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다. 초보자도 이해하기 쉽게 글을 작성하세요.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "썸네일 문구 생성기",
        "content": "클릭을 유도하는 강한 문구를 5개 작성하세요.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "생산성 코치 페르소나",
        "content": "당신은 친절하고 차분한 생산성 코치입니다. 단계별로 설명하세요.",
        "category": "페르소나",
        "favorite": False
    }
]

CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]
def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록 보기")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 추가/해제")
    print("7. 즐겨찾기 목록 보기")
    print("0. 종료")
    def input_non_empty(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print("빈 값은 입력할 수 없습니다. 다시 입력하세요.")
def select_category():
    print("\n카테고리 목록")
    for i, category in enumerate(CATEGORIES, start=1):
        print(f"{i}. {category}")
    print("0. 직접 입력")

    while True:
        choice = input("카테고리 번호를 선택하세요: ").strip()

        if choice == "0":
            return input_non_empty("직접 입력할 카테고리명: ")

        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(CATEGORIES):
                return CATEGORIES[index]

        print("올바른 번호를 입력하세요.")
        