# settings.py

...
# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CUSTOM_APPS = [
    'todo',
    'users',
]

THIRD_PARTY_APPS = [
    'django_extensions',
    'django_summernote',
    'django_cleanup',
]

INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS + THIRD_PARTY_APPS

...

# media 경로 설정하기 - static 설정 아래에 추가
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

...

# Summernote 설정
SUMMERNOTE_CONFIG = {
    # HTML 태그 또는 JS를 수정하지 못하도록 iframe 설정
    'iframe': True,

    'summernote': {
        # airMode 비활성화: 툴바를 항상 표시하도록 설정
        'airMode': False,

        # 에디터의 사이즈 정의
        'width': '100%',    # 에디터의 너비를 100%로 설정
        'height': '480',    # 에디터의 높이를 480px로 설정

        # 에디터의 툴바 메뉴 정의
        'toolbar': [
            ['style', ['style']],                      # 스타일 설정
            ['font', ['bold', 'underline', 'clear']],  # 글꼴 설정: 굵게, 밑줄, 지우기
            ['color', ['color']],                      # 색상 설정
            ['para', ['ul', 'ol', 'paragraph']],       # 문단 설정: 글머리 기호, 번호 매기기, 문단
            ['table', ['table']],                      # 표 삽입
            ['insert', ['link', 'picture']],           # 삽입 기능: 링크, 그림
            ['view', ['fullscreen']],                  # 보기 설정: 전체 화면
        ],

        # 에디터 언어 정의
        'lang': 'ko-KR',  # 에디터의 언어를 한국어로 설정

        # 코드미러 설정
        'codemirror': {
            'mode': 'htmlmixed',     # 코드미러의 모드를 htmlmixed로 설정
            'lineNumbers': 'true',   # 코드미러에서 줄 번호를 표시
            'theme': 'monokai',      # 코드미러의 테마를 monokai로 설정
        },
    },

    # 첨부파일 인증 필요 여부 설정
    'attachment_require_authentication': True,

    # 첨부파일 기능 비활성화 설정
    'disable_attachment': False,

    # 첨부파일의 절대경로 URI 사용 설정
    'attachment_absolute_uri': True,
}