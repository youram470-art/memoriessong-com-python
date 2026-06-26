HOMEPAGE = "https://memoriessong.com"
DOCUMENTATION = "https://memoriessong.com/docs"
PACKAGE = "memoriessong-com"
REPOSITORY = "https://github.com/youram470-art/memoriessong-com-python"
LOCAL_REPOSITORY = "/Users/mac/Documents/code/foreversong"
CONTENT_PATH = "content"
APP_PATH = "src/app"
FOCUS = "AI keepsake music, memory-song creation, and emotional tribute song workflows"


def hello() -> str:
    return "hello from memoriessong.com"


def get_site_info() -> dict:
    return {
        "name": "Memories Song",
        "domain": "memoriessong.com",
        "homepage": HOMEPAGE,
        "documentation": DOCUMENTATION,
        "package": PACKAGE,
        "repository": REPOSITORY,
        "local_repository": LOCAL_REPOSITORY,
        "content_path": CONTENT_PATH,
        "app_path": APP_PATH,
        "focus": FOCUS,
    }
