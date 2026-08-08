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


# 프롬프트 추가용: 선택 또는 직접 입력
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


# 카테고리 조회용: 현재 등록된 카테고리에서 선택 또는 직접 입력
def select_category_for_search():
    if not prompts:
        return None

    categories = []
    for prompt in prompts:
        if prompt["category"] not in categories:
            categories.append(prompt["category"])

    print("\n카테고리 목록")
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")
    print("0. 직접 입력")

    while True:
        choice = input("조회할 카테고리 번호를 선택하세요: ").strip()

        if choice == "0":
            return input_non_empty("직접 입력할 카테고리명: ")

        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(categories):
                return categories[index]

        print("올바른 번호를 입력하세요.")


def add_prompt():
    title = input_non_empty("제목: ")
    content = input_non_empty("내용: ")
    category = select_category()

    prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(prompt)
    print("프롬프트가 추가되었습니다.")


def show_list():
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    print("\n=== 프롬프트 목록 ===")
    for i, prompt in enumerate(prompts, start=1):
        star = "⭐" if prompt["favorite"] else ""
        print(f"{i}. [{prompt['category']}] {prompt['title']} {star}")


# STEP 6
def show_by_category():
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    print("\n=== 카테고리별 조회 ===")
    selected_category = select_category_for_search()

    if selected_category is None:
        print("등록된 프롬프트가 없습니다.")
        return

    filtered_prompts = []
    for prompt in prompts:
        if prompt["category"] == selected_category:
            filtered_prompts.append(prompt)

    if not filtered_prompts:
        print("해당 카테고리의 프롬프트가 없습니다.")
        return

    print(f"\n=== '{selected_category}' 카테고리 목록 ===")
    for i, prompt in enumerate(filtered_prompts, start=1):
        star = "⭐" if prompt["favorite"] else ""
        print(f"{i}. [{prompt['category']}] {prompt['title']} {star}")


def search_prompts():
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    keyword = input_non_empty("검색어를 입력하세요: ").lower()
    results = []

    for prompt in prompts:
        if keyword in prompt["title"].lower() or keyword in prompt["content"].lower():
            results.append(prompt)

    if not results:
        print("검색 결과가 없습니다.")
        return

    print("\n=== 검색 결과 ===")
    for i, prompt in enumerate(results, start=1):
        star = "⭐" if prompt["favorite"] else ""
        print(f"{i}. [{prompt['category']}] {prompt['title']} {star}")


def show_prompt_detail():
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list()
    choice = input("상세 보기할 번호를 입력하세요: ").strip()

    if not choice.isdigit():
        print("숫자를 입력해주세요.")
        return

    index = int(choice) - 1
    if index < 0 or index >= len(prompts):
        print("올바른 번호를 입력하세요.")
        return

    prompt = prompts[index]
    print("\n=== 프롬프트 상세 보기 ===")
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"내용: {prompt['content']}")
    print(f"즐겨찾기: {'예' if prompt['favorite'] else '아니오'}")


def toggle_favorite():
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list()
    choice = input("즐겨찾기 추가/해제할 번호를 입력하세요: ").strip()

    if not choice.isdigit():
        print("숫자를 입력해주세요.")
        return

    index = int(choice) - 1
    if index < 0 or index >= len(prompts):
        print("올바른 번호를 입력하세요.")
        return

    prompts[index]["favorite"] = not prompts[index]["favorite"]

    if prompts[index]["favorite"]:
        print("즐겨찾기에 추가되었습니다.")
    else:
        print("즐겨찾기가 해제되었습니다.")


# STEP 7
def show_favorite_list():
    favorites = []

    for prompt in prompts:
        if prompt["favorite"]:
            favorites.append(prompt)

    if not favorites:
        print("즐겨찾기된 프롬프트가 없습니다.")
        return

    print("\n=== 즐겨찾기 목록 ===")
    for i, prompt in enumerate(favorites, start=1):
        print(f"{i}. [{prompt['category']}] {prompt['title']} ⭐")


while True:
    show_menu()
    menu = input("메뉴를 선택하세요: ").strip()

    if menu == "1":
        add_prompt()
    elif menu == "2":
        show_list()
    elif menu == "3":
        show_by_category()
    elif menu == "4":
        search_prompts()
    elif menu == "5":
        show_prompt_detail()
    elif menu == "6":
        toggle_favorite()
    elif menu == "7":
        show_favorite_list()
    elif menu == "0":
        print("프로그램을 종료합니다.")
        break
    else:
        print("올바른 메뉴 번호를 입력하세요.")
def search_prompts():
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    keyword = input_non_empty("검색어를 입력하세요: ").lower()
    results = []

    for prompt in prompts:
        title = prompt["title"].lower()
        content = prompt["content"].lower()
        category = prompt["category"].lower()

        if keyword in title or keyword in content or keyword in category:
            results.append(prompt)

    if not results:
        print("검색 결과가 없습니다.")
        return

    print("\n=== 검색 결과 ===")
    for i, prompt in enumerate(results, start=1):
        star = "⭐" if prompt["favorite"] else ""
        print(f"{i}. [{prompt['category']}] {prompt['title']} {star}")
    def show_prompt_detail():
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list()
    choice = input("상세 보기할 번호를 입력하세요: ").strip()

    if not choice.isdigit():
        print("숫자를 입력해주세요.")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(prompts):
        print("올바른 번호를 입력하세요.")
        return

    prompt = prompts[index]

    print("\n=== 프롬프트 상세 보기 ===")
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"내용: {prompt['content']}")
    print(f"즐겨찾기: {'예' if prompt['favorite'] else '아니오'}")
    def toggle_favorite():
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list()
    choice = input("즐겨찾기 추가/해제할 번호를 입력하세요: ").strip()

    if not choice.isdigit():
        print("숫자를 입력해주세요.")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(prompts):
        print("올바른 번호를 입력하세요.")
        return

    prompts[index]["favorite"] = not prompts[index]["favorite"]

    if prompts[index]["favorite"]:
        print(f"'{prompts[index]['title']}'이(가) 즐겨찾기에 추가되었습니다.")
    else:
        print(f"'{prompts[index]['title']}'의 즐겨찾기가 해제되었습니다.")
        
